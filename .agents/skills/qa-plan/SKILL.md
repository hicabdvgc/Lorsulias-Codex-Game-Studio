---
name: qa-plan
description: "Author scoped QA plans linking every applicable acceptance criterion to feasible automated, inspection, manual, engine and human evidence."
---

# Qa Plan

Read `.codex/docs/work-preparation.md`, `.codex/docs/code-root-resolution.md` and
`.codex/docs/testing-engine-reference.md`. Live `docs/technical-preferences.md`
and actual project configuration determine selected engine, language, runner,
roots and commands. Library references do not establish installation or selection.
Use existing task authorization. Re-read targets before writes, preserve concurrent
and unrelated work, and inspect promised outputs after saving. Preserve completed
work if a dependent step fails; identify the affected activity.

## Invocation and resolution
`$qa-plan [sprint|sprint-N|feature: system-name|story: path|epic: path]`.
No argument asks for scope; reject unsupported argument shapes.
- Sprint resolves the active sprint from an explicit active/status reference;
  sprint-N resolves that exact plan. Use matching YAML for membership and plan
  metadata, report disagreements and take work progress from referenced stories.
- Feature resolves exact metadata, parent/system links and GDD references. Ambiguous
  matches need a choice; title substrings and modification time are insufficient.
- Story loads the exact project-local story; epic reads its actual story references.
Retain every missing/unreadable reference and its coverage gap. Zero usable stories
or unresolved scope blocks authoring; partial scope may produce an explicitly
incomplete plan. A read-only story-status summary can assist, not replace resolution.

## Load applicable sources
Read complete stories, all acceptance criteria, inputs/outputs, dependencies, actual
governance, GDD/FRAMEWORK requirements, resource/tool contracts, accessibility and
selected platforms. Read existing QA plans by matching scope/revision and covered
criteria; modification time alone does not establish relevance. Use available
qa-lead expertise without assuming dispatch or delegating human evaluation to a
simulation. Executor changes preserve required independence.

## Map evidence at criterion level
Use `.codex/docs/templates/test-plan.md`. Retain story types as descriptive labels;
mixed work retains every applicable evidence method. For each criterion record:
stable story/criterion identity, source, inputs/setup, steps/command, expected result,
evaluation method, responsible evaluator, revision, evidence destination and gaps.
Automated and engine tests use the selected runner's actual locations. Inspection,
manual and human protocols need reproducible conditions, observations/questions
and a decision method. A path, screenshot, vague “feels good” or empty checkbox
alone cannot establish adequate evaluation.

Include where applicable: formula/domain checks, system interfaces, save/load,
selected UX/accessibility interactions, prepared-resource identity/relationships/
format and usable integration, FRAMEWORK addition/modification effects, tool complete
workflow and intended-user evaluation. Choose regression and smoke scope from actual
affected behavior. Unknown units, targets, budgets or standards remain decisions to
resolve. No universal test categories or coverage percentages are imposed.

Identify real prerequisite states separately from the outputs to be created. Plan
required independent review and actual human play/evaluation. Do not claim a plan
was executed, a test file passed, or a story became Ready/Complete. Missing runner,
engine, reviewer or person remains pending and blocks only dependent conclusions.

## Save and handoff
Save `production/qa/qa-plan-[scope-slug]-[date].md`; derive an unambiguous safe slug
from the resolved sprint, feature, qualified story or epic. Header records exact
scope paths/IDs, source revisions, missing members and planned versus executed status.
Reuse an explicitly requested existing output with scoped updates; preserve earlier
results and concurrent changes. Backfill story QA sections only if the request
includes those bounded changes; never change story Status through QA planning.
Inspect saved paths and criterion coverage. Report covered/missing criteria and
review/human dependencies; a partial scope cannot be labeled fully covered. Return
COMPLETE for completed planning, PARTIAL for unresolved required scope. Execution
orchestration uses installed team-qa, smoke-check and story-done with actual execution evidence.
