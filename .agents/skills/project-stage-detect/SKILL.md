---
name: project-stage-detect
description: Observe declared workflow section, available outcome evidence and gaps
  without changing project state.
---

# Project Stage Detect

Invoke as `$project-stage-detect`. Arguments: `[role filter: programmer | designer | producer]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Read `.codex/docs/progression.md` and the actual workflow catalog. Validate an optional role filter;
without one report the overall scope. Read production/stage.txt if present, preserving its first
nonempty declared value. Missing, legacy, conflicting or unknown values are unresolved; do not map
other stage vocabularies silently onto this workflow or create a marker.

Inspect catalog outcome evidence and actual project roots. The optional `.codex/scripts/artifact-check.sh`
reports declared-path discovery only; `.codex/hooks/detect-gaps.sh` supplies bounded observations
through SessionStart and can also be invoked explicitly. Missing helper/runtime leaves that inspection unavailable. Read the actual
content/maturity needed for relevant steps and distinguish manual activities and pending skills.
No artifact count, file date or presence of epics establishes Production or a passing checkpoint.

Use `.codex/docs/templates/project-stage-report.md` to structure the conversational report: declared
section, observed current activities, fulfilled/failed/unassessed outcomes, discrepancies, blockers,
manual responsibilities and available support. A role filter changes recommendations, not required
outcomes. Identify candidates for `$gate-check` or concrete authoring work without declaring advancement.
This mode stays read-only: no stage file, session state, saved report or inferred status writes.
