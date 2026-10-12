---
name: define-milestones
description: "Author or update project-defined MVP, Alpha, Beta and Gold expectations, playtest questions and progression criteria."
---

# Define Milestones

Read `.codex/docs/work-preparation.md` for governing inputs, status authority,
criterion-level evidence, review, authorization and recovery rules. Apply them to
the selected scope. Read the package CONTRACT.md when present for its handoff.

## Invocation and scope
Invoke `$define-milestones` with the requested project decisions or a scoped update
description. Read existing `production/milestones/MILESTONE.md` before asking for
known information. Use `.codex/docs/templates/milestone-definition.md`.

## Establish the basis
Read developer-authored CONCEPT, relevant BREAKDOWN/GDDs, FRAMEWORK, architecture,
prepared resource/tool interfaces, accessibility commitments, existing epics/stories
and actual slice findings. Epics/stories precede final milestone definitions; do not
make milestone creation their prerequisite. Keep proposed and accepted decisions distinct.

Final authoring follows the vertical-slice hard gate: actual play, coherent system
integration and demonstrated framework additions/modifications must support it.
Identify the supplied gate decision and evidence. Missing required evidence permits
an explicitly incomplete draft, not a settled definition or a production-ready claim.
No new gate automation or receipt machinery is supplied here.

## Author expectations
For MVP, Alpha, Beta and Gold, establish:
- Included outcomes and the expected completeness/polish for this particular game.
- What needs to be learned from playing that version; actual participant/activity,
  observation and comparison/decision basis needed to answer those questions.
- Applicable system/resource/tool integration, quality and accessibility criteria.
- Dependencies, unresolved decisions and conditions for progression.
Use supplied decisions and ask about consequential missing choices. Do not invent
content completeness percentages, bug budgets, playtest counts, dates, capacity,
owners or sprint subdivisions. Optional selected targets state their units and basis.

For a scoped update, retain other milestones and stable referenced work. Identify
affected epics/stories, QA/sprint plans and designs/framework/resources. Update those
only when included in authorization; otherwise return exact follow-up impacts.

## Save and report
Save only the authoritative MILESTONE file within task scope. Reread before saving,
preserve concurrent decisions and read back the result. Return maturity, selected
decisions, unresolved work, evidence basis and affected consumers. COMPLETE means
the requested authoring is fulfilled; an incomplete draft is explicitly PARTIAL.
Neither status means any milestone was achieved. Actual production/playtests and
milestone-review orchestration remain later work. Sprints are optional.
