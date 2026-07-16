**AICR — AI-Generated Code Review Assistant**


**Dataset Creation**

*Overview*

AICR fine-tunes an LLM (Qwen2.5-Coder-3B-Instruct, via SFT + DPO) to review AI-generated code with a validate-then-critique structure — acknowledging what's reasonable about an approach before raising specific, verifiable issues. Unlike generic code review, feedback correctness here is grounded in actual test-derived evidence, not subjective judgment.
This section documents how the training dataset was built.


*Methodology*

1. Task design. 30 coding task prompts were written across four categories: data parsing/processing, backend/API-style logic, algorithmic problems, and utility functions with common edge cases. Prompts were deliberately kept casual and underspecified — the way a developer would actually phrase a request to an AI coding assistant — with no edge-case hints, so failure modes would surface naturally rather than being prompted for.

2. Snippet generation. Each of the 30 tasks was submitted to three AI coding tools — Claude, GPT, and Cursor — producing 90 real, independently-generated Python snippets (one per task per tool). Each tool received the same casual wrapper prompt in a fresh session, with no shared context between tasks.

3. Ground truth via testing. For each task, a shared test suite (5 test cases: normal usage, empty/None input, boundary values, and malformed input) was written against the original task requirement, not tailored to any one tool's implementation. All 90 snippets were run against their task's test suite inside an isolated virtual environment, producing an objective, reproducible pass/fail record for every snippet — not a subjective code review.
Each result was labeled:

```

clean_pass — all test cases passed
fragile_pass — passed, but with risky/non-defensive patterns
edge_case_fail — passed normal cases, failed on an edge case
hard_fail — failed on the basic/normal case itself

```

Results were stored in results/ground_truth.json, with human-readable notes explaining the specific cause of each failure.

4. Notable findings from testing:

All three tools (Claude, GPT, Cursor) independently made the same mistake on the UTC-to-local-timezone task — calling pytz.timezone('UTC') instead of the correct pytz.UTC, causing a hard failure on the normal case, not just an edge case.
On version-string comparison, Claude and GPT both mishandled differing segment lengths ("1.2" vs "1.2.0"), while Cursor handled it correctly.
The large majority of edge-case failures across all three tools were due to unhandled None input — expected, since no task prompt requested defensive None-handling, but a consistent and notable pattern across tools regardless.

5. Preference pair generation. Since a large share of results converged on the same repetitive failure type (unhandled None input), raw ground-truth results were not used unfiltered for training — that would have taught the model one narrow lesson rather than a general reviewing skill. Instead, results were split into three tiers:
TierDescriptionEntries used1Distinct, non-repetitive bugs (hard failures, multi-failure cases, or edge cases unrelated to None-handling)28 (all included)2Repetitive None-input-only failures20 (sampled from 54, spread across task types for diversity)3Clean or fragile passes8 (all included — used to train against false-positive/hallucinated review feedback)
For each selected entry, a strong LLM (Claude Sonnet 4.6, supplemented manually for a small remainder) generated a chosen review (validate-then-critique, grounded in the actual test result) and one or more rejected reviews (blunt criticism-first, generic praise-padding, vague/non-specific feedback, or — for clean passes — a hallucinated bug that doesn't exist).
Tier 1 entries received 3 rejected variants each; Tier 2 and Tier 3 entries received 1 each.
Final dataset: 111 preference pairs, saved in preference_pairs.jsonl with fields task_id, tool, tier, prompt, chosen, rejected, rejected_style.


Test suites intentionally probed beyond what the casual task prompts specified (e.g., None-input handling), as a deliberate stress-testing choice — this is why None-related failures dominate raw results, and why the dataset was tiered before training rather than used as-is.

---

Dataset scale (112 pairs) is appropriate for narrow behavioral fine-tuning (structure/style conformance) via LoRA/QLoRA, not for teaching new domain knowledge — this is a small-scale experiment, not a large-scale training run.
A small number of Tier 2/3 pairs were generated manually (via chat) rather than through the automated pipeline, due to API credit limits — content followed the identical prompt template, but this is disclosed for transparency.

---

Next: Stage 1 (SFT) and Stage 2 (DPO) fine-tuning on Qwen2.5-Coder-3B-Instruct.