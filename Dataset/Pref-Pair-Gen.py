"""
AICR Step D — Preference Pair Generation
-------------------------------------------
Reads ground_truth.json + the actual snippet files, classifies each
(task, tool) entry into Tier 1 / 2 / 3, then calls a strong model via
OpenRouter to generate chosen/rejected review pairs for training.

SETUP:
  pip install openai --break-system-packages
  export OPENROUTER_API_KEY="your-key-here"

OUTPUT:
  preference_pairs.jsonl  -- one JSON object per line:
    {"task_id": ..., "tool": ..., "tier": ..., "prompt": ...,
     "chosen": ..., "rejected": ..., "rejected_style": ...}
"""

import os
import re
import json
import time
from pathlib import Path
from openai import OpenAI

# --- CONFIG ---
GROUND_TRUTH_PATH = Path("C:\\Users\\MCA\\Desktop\\response_generated\\results\\ground_truth.json")
SNIPPETS_ROOT = Path("C:\\Users\\MCA\\Desktop\\response_generated")
OUTPUT_PATH = Path("C:\\Users\\MCA\\Desktop\\preference_pairs.jsonl")

GENERATOR_MODEL = "anthropic/claude-haiku-4.5"     # the strong model used to WRITE chosen/rejected pairs
TIER2_SAMPLE_CAP = 20                 # max number of repetitive None-handling entries to include

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="use_your_own_key",
)


def load_ground_truth():
    with open(GROUND_TRUTH_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_snippet(task_id, tool):
    path = SNIPPETS_ROOT / tool / f"{task_id}_{tool}.py"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def is_none_only_failure(entry):
    """True if this entry's only failure is specifically about None input."""
    if entry["failed"] != 1:
        return False
    notes = entry["notes"].lower()
    return "none" in notes and ("test 3" in notes or "none input" in notes or "none length" in notes)


def classify_tier(entry):
    label = entry["label"]
    if label == "hard_fail":
        return 1
    if label in ("clean_pass", "fragile_pass"):
        return 3
    if label == "edge_case_fail":
        if entry["failed"] > 1:
            return 1
        if is_none_only_failure(entry):
            return 2
        return 1  # single failure, but not None-related -> still a distinct/interesting bug
    return 1  # fallback, shouldn't normally hit this


def build_entries(ground_truth):
    """Flattens ground_truth.json into a list of per-tool entries with tier labels."""
    entries = []
    for task_id, task_data in ground_truth.items():
        task_description = task_data["task_description"]
        for tool in ("claude", "gpt", "cursor"):
            if tool not in task_data:
                continue
            result = task_data[tool]
            entry = {
                "task_id": task_id,
                "tool": tool,
                "task_description": task_description,
                "label": result["label"],
                "passed": result["passed"],
                "failed": result["failed"],
                "notes": result["notes"],
            }
            entry["tier"] = classify_tier(entry)
            entries.append(entry)
    return entries


def sample_tier2(entries, cap):
    """Keep all Tier 1 and Tier 3 entries; sample Tier 2 down to `cap`,
    spread across different task_ids for domain diversity."""
    tier1 = [e for e in entries if e["tier"] == 1]
    tier3 = [e for e in entries if e["tier"] == 3]
    tier2 = [e for e in entries if e["tier"] == 2]

    tier2_sorted = sorted(tier2, key=lambda e: e["task_id"])
    if len(tier2_sorted) > cap:
        step = len(tier2_sorted) / cap
        sampled_tier2 = [tier2_sorted[int(i * step)] for i in range(cap)]
    else:
        sampled_tier2 = tier2_sorted

    return tier1 + sampled_tier2 + tier3


GENERATION_PROMPT = """Given this code snippet (written to solve: "{task_description}"):

{snippet_code}

Testing revealed: {notes}
Result: {label} ({passed} passed, {failed} failed out of {total})

Write TWO code reviews as JSON with keys "chosen" and "rejected":

"chosen": First, in 1-2 sentences, validate what is reasonable or
well-structured about the approach. Then give specific, actionable
critique that references the actual code (variable/function names) and
the specific failure above. If the result is a clean pass, say so briefly
and note no issues were found - do not invent a problem.

"rejected": Write a review in this style: {rejected_style}

Respond with ONLY valid JSON, no markdown fences, no extra text.
Format: {{"chosen": "...", "rejected": "..."}}
"""

REJECTED_STYLES = {
    1: [
        "Blunt criticism-first, no acknowledgment of anything reasonable about the approach.",
        "Generic praise-padding ('Great job! Just a few small things...') with vague, non-actionable suggestions.",
        "Vague feedback that doesn't reference the actual failure or any specific code detail.",
    ],
    2: [
        "Vague feedback that doesn't reference the actual failure or any specific code detail.",
    ],
    3: [
        "A review that HALLUCINATES a plausible-sounding bug or issue that does NOT actually exist in this clean/passing code.",
    ],
}


def generate_pair(entry, snippet_code, rejected_style):
    total = entry["passed"] + entry["failed"]
    prompt = GENERATION_PROMPT.format(
        task_description=entry["task_description"],
        snippet_code=snippet_code,
        notes=entry["notes"],
        label=entry["label"],
        passed=entry["passed"],
        failed=entry["failed"],
        total=total,
        rejected_style=rejected_style,
    )

    response = client.chat.completions.create(
        model=GENERATOR_MODEL,
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = response.choices[0].message.content.strip()
    raw = re.sub(r"^```json\s*|\s*```$", "", raw.strip())

    try:
        parsed = json.loads(raw)
        return parsed.get("chosen"), parsed.get("rejected")
    except json.JSONDecodeError:
        print(f"  [WARN] Could not parse JSON for {entry['task_id']}_{entry['tool']}, skipping.")
        return None, None


def main():
    ground_truth = load_ground_truth()
    entries = build_entries(ground_truth)
    selected = sample_tier2(entries, TIER2_SAMPLE_CAP)

    print(f"Total entries: {len(entries)}")
    print(f"Selected after tiering/sampling: {len(selected)} "
          f"(Tier1={sum(1 for e in selected if e['tier']==1)}, "
          f"Tier2={sum(1 for e in selected if e['tier']==2)}, "
          f"Tier3={sum(1 for e in selected if e['tier']==3)})")

    written = 0
    with open(OUTPUT_PATH, "w", encoding="utf-8") as out_f:
        for entry in selected:
            snippet_code = load_snippet(entry["task_id"], entry["tool"])
            if snippet_code is None:
                print(f"  [SKIP] snippet not found for {entry['task_id']}_{entry['tool']}")
                continue

            styles = REJECTED_STYLES[entry["tier"]]

            for style in styles:
                print(f"[{entry['task_id']}_{entry['tool']} | tier {entry['tier']}] generating pair...")
                chosen, rejected = generate_pair(entry, snippet_code, style)
                if chosen and rejected:
                    record = {
                        "task_id": entry["task_id"],
                        "tool": entry["tool"],
                        "tier": entry["tier"],
                        "prompt": f"Review this code:\n\n{snippet_code}",
                        "chosen": chosen,
                        "rejected": rejected,
                        "rejected_style": style,
                    }
                    out_f.write(json.dumps(record) + "\n")
                    written += 1
                time.sleep(1)

    print(f"\nDone. Wrote {written} preference pairs to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()