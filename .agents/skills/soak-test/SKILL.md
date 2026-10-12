---
name: soak-test
description: Prepare a reproducible extended-session protocol and analyze supplied
  observations without implying an unperformed run.
---

# Soak Test

Invoke as `$soak-test`. Arguments: `[target] [duration, e.g. 30m or 2h] [focus: memory | stability | balance | all]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Resolve target, positive duration with units and focus. Examples are not a duration whitelist or
default budget. Ask for material missing choices; reject invalid/ambiguous arguments before writes.
Read actual game/build/platform, relevant systems, configured metrics/budgets, prior comparable
sessions and known issues. Missing budgets limit assessment without inventing thresholds.

Create a protocol tailored to the selected focus: baseline conditions, representative repeatable
activity, relevant checkpoints, what to measure/observe, failure/early-stop handling and post-session
comparison. Memory includes measured usage and workload; stability includes crashes, hangs, corrupt
state and resource exhaustion; balance/fatigue requires real play observations against supplied goals.
Include engine-specific capture instructions only when verified for the selected tools/version.
No source-code scan can establish a leak or an observed out-of-memory condition.

Save the requested protocol to production/qa/soak-test-[target]-[session].md, retaining actual duration,
focus, environment/revision, baseline, timestamped checkpoint log, early termination and result fields.
A newly generated protocol is **NOT RUN**, with empty observations and no sign-off. Do not overwrite a
previous session. For supplied actual results, record performed duration, measurements/observations,
limitations and **PASS / PASS WITH CONCERNS / FAIL / NOT ASSESSED** against applicable requirements.
Early termination leaves unperformed duration/checks explicit. Required missing observations prevent
PASS. Real execution, human evaluation and fixes are separate scoped activities; verify saved output.
