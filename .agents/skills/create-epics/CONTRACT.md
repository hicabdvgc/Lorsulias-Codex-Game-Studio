# $create-epics — Handoff contract

## Purpose and prerequisites
Group selected system/framework/resource/tool outcomes into dependency-aware epics.
Resolve full BREAKDOWN and relevant GDDs/FRAMEWORK, applicable architecture, accepted
ADRs, scoped CONTROL and durable TR sources. Use actual slice findings where relevant;
final MILESTONE is not a universal prerequisite. Named/all-system selection remains;
layer selection requires an actual project-defined grouping. Missing inputs may
support a labeled non-ready draft, never fabricated readiness.

## Outputs and permitted changes
Create/update `production/epics/[epic-slug]/EPIC.md` and the affected rows of
`production/epics/index.md`. Retain existing epic identities, story tables and index
columns. EPIC records Status, scope/system/GDD links, applicable governance,
requirements, inputs/outputs, dependencies, completion methods and story references.
Preserve existing story files. Design, ADR, TR and CONTROL sources remain read-only.
Resolve review obligations using PR-EPIC; unavailable required review stays explicit.

## Handoff
`$create-stories` consumes the resolved epic and real sources; an epic document's
existence does not establish its readiness. A returned path must have been saved
and inspected. No implementation, universal layer order or automatic story creation
is part of this contract.

## Shared guarantees
Apply `.codex/docs/work-preparation.md`. Existing authorization carries through
bounded saves. Re-read shared files before writing, preserve stable identities and
concurrent work, inspect saved outputs and report partial failures without discarding
completed work. Reviews are conversational unless a bounded report save is requested.
Required independent review and human evaluation cannot be waived by depth/executor.
Source templates, directories and layer labels do not create project requirements.
CONTROL revisions are integers. Proposed ADRs cannot govern Ready work. Applicable
TR references must resolve to saved active entries; justified N/A is possible for
all work types. Unknown evidence remains explicit, never a placeholder identifier.
