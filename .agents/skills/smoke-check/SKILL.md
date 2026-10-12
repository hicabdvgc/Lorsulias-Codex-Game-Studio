---
name: smoke-check
description: Execute a scoped critical-path smoke check with actual configured runners
  and observations, preserving unavailable coverage.
---

# Smoke Check

Invoke as `$smoke-check`. Arguments: `[sprint | quick] [--platform pc|console|mobile|all]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


## Select scope

Accept at most one positional selector and one platform selector; unknown flags, extra selectors
or unsupported positional system names return usage before execution. Without a selector use the
explicit current build/scope or ask. Sprint resolves actual selected membership and stories;
quick uses a stated limited critical path. Platform selectors filter configured targets; all
means all selected targets, not every possible device. Missing choices remain unresolved.

Read actual test/launch roots and commands from live preferences and project evidence, applicable
GDD/FRAMEWORK, QA plan, resource contracts and story criteria. Use `.codex/docs/testing-engine-reference.md`
and verified selected-version docs for Godot, Unity or Unreal. No guessed runner path or universal
keyboard/mouse route applies. An absent tests folder does not prevent a relevant manual check;
missing required infrastructure leaves its dependent coverage unavailable.

## Execute and observe

Run the selected authorized automated checks, retaining command, revision, scope, output and exit
status. Inspect assertions/results and runtime errors; a clean launch alone is insufficient.
Check representative critical-path startup, selected input/navigation, core interaction, persistence
and resources only where applicable. Use `.codex/docs/run-and-observe.md` for actual runtime states.
Obtain human observations for applicable controls, usability, feel/audio/accessibility. Ask for
missing actual results in a concise group; never infer a manual pass from absent bug reports.
Check coverage against selected criteria; quick mode leaves omitted coverage explicit.

Return **PASS / PASS WITH WARNINGS / FAIL / NOT ASSESSED** with per-check results. PASS requires
all required checks in the named scope. Warnings may concern advisory checks only; failed required
checks mean FAIL, and unavailable required checks prevent PASS. Retain both failures and gaps.
Save the requested smoke record under production/qa/smoke-[scope]-[date].md, checking for session
collisions and preserving prior evidence. A request to run and report smoke authorizes that bounded
record. Read it back; an unsaved promised report blocks a consumer requiring that record. QA may
rely only on matching revision/scope evidence. No story or stage status changes follow this skill.
