---
name: create-control-manifest
description: "Create or update scoped CONTROL obligations from accepted decisions and explicit project choices, preserving provenance and integer revisions."
---

# Create Control Manifest

Invoke as `$create-control-manifest`.

Arguments: `[update]`. The task may name selected component scopes; otherwise assess the existing scope or all currently governed components.

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


## Read actual governing inputs

Read the relevant Accepted ADRs, master architecture, full FRAMEWORK, live technical
preferences, current CONTROL and architectural registry. Discover actual ADR records;
exclude master architecture, indexes and review reports. Proposed/Superseded records
are not new governing sources. Resolve stale registry references against their ADRs.

Use verified engine references for applicable API constraints. They are evidence,
not automatic project policy. Missing required version/evidence leaves the affected
rule unassessed. If no applicable governing input exists, report INCOMPLETE rather
than manufacturing rules or declaring readiness.

## Extract and reconcile rules

For each selected component, identify Required patterns, Forbidden approaches and
Guardrails from explicit accepted obligations. Preserve conditional scope, units,
limits, exceptions and provenance. Keep advice as Recommended; do not promote
"consider", engine best-practice suggestions or example budgets into Required.

Merge true duplicates while preserving their sources. Surface conflicting accepted
rules or project choices for resolution; do not silently select the stricter rule
or change an ADR. Block publication of a contradictory governing manifest while
independent analysis can continue.

## Write the manifest

Target: `docs/architecture/CONTROL.md`.

```markdown
# Control Manifest
Manifest Version: [integer]
Last Updated: [date]
Scope: [actual components]
Source revisions: [accepted decisions, framework and choices used]

## [Component / Global scope]
| Rule ID | Obligation | Instruction | Applies when | Source and revision | Verification |
|---|---|---|---|---|---|
| [stable local ID] | Required / Forbidden / Guardrail / Recommended | [specific rule] | [scope] | [provenance] | [method] |

## Unresolved Inputs and Follow-up
[Specific missing evidence or pending decisions, affected components and next activity]
```

Preserve useful existing rule identifiers and unaffected scopes. Initial version is
1. Increment the integer when governing rules, applicability or governing provenance
change. Do not increment for an unchanged rerun or purely editorial correction.
Re-read the baseline before saving; preserve concurrent changes and resolve conflicts.

Verify saved rules against their sources and check that output consumers can identify
the applicable scope/version. Report COMPLETE / INCOMPLETE / NO CHANGE with actual
changes, evidence and limitations. CONTROL creation does not validate a build or
authorize production; later work-item consumers must use its applicable revision.
