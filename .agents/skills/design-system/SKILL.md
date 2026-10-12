---
name: design-system
description: "Author or retrofit a system GDD using full BREAKDOWN and preliminary FRAMEWORK, with explicit behavior, integrations, resource needs and evaluation."
---

# Design System

Invoke as `$design-system`.

Arguments: `<system-name> [--review full|lean|solo]`. Preserve the source retrofit workflow when the named GDD already exists.

## Shared execution boundary

Read the relevant artifacts before asking about information they contain. Existing
bounded task authorization covers its edits and verification; ask about unresolved
consequential choices or a material scope expansion. Preserve unrelated changes
and re-read a target before writing if its baseline may have changed.

Use available qualified executors under the current environment's delegation
policy. Role names describe expertise. Follow `.codex/docs/review-workflow.md`
and `.codex/docs/director-gates.md`: required independent review and human evidence
remain required with any executor. Identify self-review; unavailable required
evidence is NOT ASSESSED. Review-depth flags change optional breadth, never these
obligations. `full` adds applicable specialist/gate reviews; `lean` is focused;
`solo` identifies self-review. Default to focused review when unspecified.

Apply `.codex/docs/skill-authoring.md` and `.codex/docs/error-recovery-protocol.md`.
Verify promised saved outputs before handoff. Resolve available support from the
installed catalog; require an input only when the selected activity needs its outcome.


## Select the system and preserve existing work

Require one unambiguous system entry in `design/gdd/BREAKDOWN.md`, declared Full,
and `docs/FRAMEWORK.md` at least Preliminary. Read CONCEPT, the full target GDD if
present, relevant dependency GDDs, studies, shared facts and applicable accepted ADRs.
Use live technical preferences and verified engine evidence only for relevant
feasibility questions. Initial GDD authoring does not require resource schemas,
ACCESSIBILITY, master architecture, MILESTONE, stories or tests that are future outputs.

Resolve the declared project-local GDD path; do not derive an external path from
an arbitrary system name. An existing GDD enters revision/retrofit, preserving
valid content and historical evidence. If the requested changes are ambiguous,
show the specific alternatives before editing. Missing core input yields BLOCKED
and names the activity that supplies it; do not invent a replacement concept.

## Develop the design

Use `.codex/docs/templates/game-design-document.md`. Establish the system's
purpose, boundary, desired player experience, core rules, states, interactions,
formulas where relevant, edge behavior, dependencies, tuning and evaluation.
Read [references/continued-workflow.md](references/continued-workflow.md) for the
detailed authoring, shared-fact and recovery procedure.

Resolve substantive design decisions as they arise. An authorized design task
does not need a confirmation after every heading. Passing sections remain intact;
do not invent content to fill irrelevant headings or impose a fixed section order.

## Final result

Verify the saved GDD, authorized shared-fact changes and BREAKDOWN link/status.
Report the actual revision, unresolved decisions and review still needed. Author
self-check can make the draft ready for independent `$design-review`, but cannot
claim that independent review occurred or mark implementation complete. The current
agent may perform other qualified responsibilities only within the runtime policy.

Resource integration uses root `RES_TYPE.md`, the applicable `resource_templates/` TYPE_TEMP definitions and `res_lib/` entries. Read `.codex/docs/resource-preparation.md` and, for tool dependencies, `.codex/docs/tool-development.md`. Initial design does not require these future outputs; later integration assesses their actual contracts, relationships and evidence.
