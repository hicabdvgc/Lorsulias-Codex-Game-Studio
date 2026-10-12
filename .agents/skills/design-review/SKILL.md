---
name: design-review
description: "Review a system design for initial completeness or declared framework/resource integration, using actual evidence and conversational findings."
---

# Design Review

Invoke as `$design-review`.

Arguments: `[path-to-design-doc] [--depth full|lean|solo]`. The task specifies initial, framework, resource, or combined integration scope; default is initial design review.

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


## Scope and read-only boundary

Return findings in conversation by default. An explicitly authorized bounded report
save carries through and must be read back; it does not approve the reviewed document.
Do not modify the GDD, change its status or write automatic review receipts. Require one unambiguous project-local
system GDD; ask if its path or scope cannot be determined. Record the reviewed
revision, scope, actual reviewer and whether this is independent or self-review.

Read the full relevant design, CONCEPT, full BREAKDOWN, and FRAMEWORK:
- **Initial:** preliminary FRAMEWORK is sufficient; future schemas remain open design needs.
- **Framework integration:** requires full FRAMEWORK and the relevant completed system designs.
- **Resource integration:** requires the actual declared resource contracts/type templates
  for the system. Their locations come from supplied references, not invented globs.
- **Combined:** perform both integration checks. Missing required inputs leave that
  check NOT ASSESSED while independent checks continue.

## Evaluate the content

Compare behavior, states, dependencies, shared facts, edge cases and evaluation
methods to the intended system. Numerical rules need units/domains, boundary
behavior and examples; a narrative or presentation system need not invent formulas.
Use `.codex/scripts/gdd-structure-check.sh` with explicit GDD paths for heading
observations if helpful. Presence is not completeness; unavailable helper execution
does not prevent direct reading.

Check whether the system can support the declared framework addition/modification
routes. For resource integration, trace a representative resource's required
properties and relationships into the consuming behavior. Report discrepancies
with precise source references and the affected next activity.

Preserve qualitative acceptance when its human evaluation is defined. A criterion
such as intended clarity needs a participant/scenario and observation method;
it need not be replaced by an invented numeric threshold.

## Specialist review and result

Full depth includes relevant specialist perspectives with findings and disagreements
kept visible. Use qualified available reviewers; a named persona being absent cannot
silently waive required expertise or independence. No fixed set of disciplines is
required for every system.

Return scope/revision, reviewer, findings, required corrections, recommendations,
inapplicable/unassessed checks, and a verdict: APPROVED / NEEDS REVISION / MAJOR
REVISION NEEDED / NOT ASSESSED. Known design failures retain the appropriate revision
verdict even if another check is unassessed; otherwise missing required evidence
yields NOT ASSESSED. APPROVED requires all applicable required checks satisfied.
State which scope was approved; initial approval says nothing about later resource
integration or implementation. Use installed `$review-all-gdds` for scoped cross-GDD orchestration.

Resource integration uses root `RES_TYPE.md`, the applicable `resource_templates/` TYPE_TEMP definitions and `res_lib/` entries. Read `.codex/docs/resource-preparation.md` and, for tool dependencies, `.codex/docs/tool-development.md`. Initial design does not require these future outputs; later integration assesses their actual contracts, relationships and evidence.
