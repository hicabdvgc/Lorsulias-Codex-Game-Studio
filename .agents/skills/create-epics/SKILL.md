---
name: create-epics
description: "Group design, framework, resource and tool outcomes into traceable epics; preserve existing stories and indexes."
---

# Create Epics

Read `.codex/docs/work-preparation.md` for governing inputs, status authority,
criterion-level evidence, review, authorization and recovery rules. Apply them to
the selected scope. Read the package CONTRACT.md when present for its handoff.

## Invocation and scope
`$create-epics [system-name | layer:<project-defined-group> | all] [--review full|lean|solo]`.
Reject malformed arguments. Use a valid explicit review-depth flag; otherwise use
focused (lean) review. Depth never waives required checks.
No argument lists exact BREAKDOWN systems for scope selection. Layer selection needs
an actual project grouping; explain absent/ambiguous mappings instead of imposing one.

## Load and group outcomes
Read `design/gdd/BREAKDOWN.md`, mapped GDDs and relevant `docs/FRAMEWORK.md`,
`docs/architecture/ARCHITECTURE_MASTER.md`, accepted ADRs, scoped CONTROL and TR
registry. Read resource/tool contracts and actual slice findings where applicable.
MILESTONE constraints apply if already defined; final MILESTONE is later in the
workflow. Missing required design or slice information stays visible in draft status.

Load full relevant requirements and enough surrounding rules to preserve meaning;
do not require a Summary heading, eight sections or a fixed layer scheme. Identify
each outcome's producing/consuming systems and actual dependencies. Several systems
may share an epic; one system may contribute distinct outcomes to several epics.
Avoid duplicating the same requirement as independent work. Dependency cycles or
ambiguous ownership need resolution, not a guessed implementation order.

For each outcome trace the precise source, applicable active TR ID and accepted
decisions. List missing required traceability/decisions and engine evidence. N/A
requires a reason; absence of a field does not establish inapplicability.

## Review and author
Present grouped outcomes, boundaries, dependencies, open decisions and applicable
PR-EPIC planning assessment. Pass complete drafts and their planned paths to the
actual qualified reviewer. Saving an identified draft can precede review; required
missing review prevents Ready. Optional depth affects only additional consultation.
No mandatory producer spawn or per-epic approval is implied by existing authorization.
Do not infer capacity or milestone dates. Unresolved scope tradeoffs remain user decisions.

Save `production/epics/[epic-slug]/EPIC.md` and update `production/epics/index.md`:

```markdown
# Epic: [coherent outcome]
> Status: [Not Started / Ready / Blocked]
> Systems/GDDs: [identities and paths]
> Architecture Module / Layer: [actual grouping or N/A]

## Overview
[Intended result, scope boundary and framework operation.]
[Readiness basis and unresolved assessment gaps.]
## Governing ADRs
| ADR / reasoned N/A | Decision and status | Covered scope |
|---|---|---|
## GDD Requirements
| Source requirement / active TR where applicable | Outcome | Governing coverage / gap |
|---|---|---|
## Dependencies and Resource/Tool Handoffs
[Actual inputs, planned outputs and affected consumers.]
## Definition of Done
[Relevant outcomes and evidence; no preset criterion count.]
## Stories
[Preserve existing story table; newly authored epic can state not yet decomposed.]
```

Keep index columns Epic, Layer/group, Systems, ADRs, Stories and Status, adapting
labels only where the project's existing index requires it. Resolve target slugs
within the epic root. Before saving, reread existing EPIC/index and preserve story
tables, IDs and unrelated edits. Update a matched epic instead of appending duplicates.
Report exact saved paths and unresolved coverage; COMPLETE describes requested
authoring, not approval of blocked outcomes. No stories or implementation are created.
Next: `$create-stories [epic]`; slice/gate execution uses installed `$vertical-slice` and `$gate-check`.
