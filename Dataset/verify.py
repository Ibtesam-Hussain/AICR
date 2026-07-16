
import json
from pathlib import Path

GROUND_TRUTH_PATH = Path("C:\\Users\\MCA\\Desktop\\response_generated\\results\\ground_truth.json")
PREFS_PATH = Path("C:\\Users\\MCA\\Desktop\\preference_pairs.jsonl")
TIER2_SAMPLE_CAP = 20

def is_none_only_failure(entry):
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
        return 1
    return 1

def sample_tier2(entries, cap):
    """MUST match the original generation script's sampling exactly."""
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

with open(GROUND_TRUTH_PATH) as f:
    ground_truth = json.load(f)

all_entries = []
for task_id, task_data in ground_truth.items():
    for tool in ("claude", "gpt", "cursor"):
        if tool not in task_data:
            continue
        result = task_data[tool]
        entry = {
            "task_id": task_id, "tool": tool,
            "label": result["label"], "passed": result["passed"],
            "failed": result["failed"], "notes": result["notes"],
        }
        entry["tier"] = classify_tier(entry)
        all_entries.append(entry)

# apply the SAME sampling the generation script used
selected = sample_tier2(all_entries, TIER2_SAMPLE_CAP)

done = set()
if PREFS_PATH.exists():
    with open(PREFS_PATH) as f:
        for line in f:
            rec = json.loads(line)
            done.add((rec["task_id"], rec["tool"]))

missing_by_tier = {1: [], 2: [], 3: []}
for entry in selected:
    key = (entry["task_id"], entry["tool"])
    if key not in done:
        missing_by_tier[entry["tier"]].append(entry)

for tier, entries in missing_by_tier.items():
    print(f"\n--- Tier {tier} missing ({len(entries)}) ---")
    for e in entries:
        print(f"  {e['task_id']} / {e['tool']} | notes: {e['notes']}")