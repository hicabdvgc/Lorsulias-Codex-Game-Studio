---
name: create-architecture
description: "Author or revise the master architecture from system designs and the full framework, with explicit ownership, interfaces, decision gaps and evidence."
---

# Create Architecture

Invoke as `$create-architecture`.

Arguments: `[full | layers | data-flow | api-boundaries | adr-audit] [--review full|lean|solo]`.

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


## Load the applicable context

Default to full. Reject unsupported modes. Read full BREAKDOWN, relevant GDDs,
full FRAMEWORK and live technical preferences. Read current master architecture,
actual ADRs, architectural registry and applicable verified engine references.
Do not treat CONTROL, reports, traceability files or templates as ADRs.

For a focused revision, read the selected subject and the dependencies needed to
check it; preserve other content. Missing required design/framework input means
BLOCKED for completed architecture. A requested exploratory draft may expose the
gaps without claiming readiness. Engine-independent analysis can continue while
version-sensitive decisions remain NOT ASSESSED.

## Produce the arrangement

For full authoring, work through:
1. System-to-component mapping based on actual responsibilities and constraints.
2. Ownership of state, interfaces and implementation work; identify qualified
   responsibilities without imposing a fixed reporting organization.
3. Data/control flow, lifecycle, resource consumption and failure behavior.
4. Interface boundaries with inputs, outputs, ownership, relevant errors and dependencies.
5. Addition/modification routes from FRAMEWORK through the actual components.
6. Existing accepted decisions, conflicting proposals, missing decisions and evidence.

`layers` focuses on arrangement/boundaries; it does not require layers. `data-flow`
and `api-boundaries` focus on those contracts. `adr-audit` identifies coverage,
conflicts and required decisions without writing new ADRs or changing acceptance.
Do not require one ADR per system or arbitrarily classify gaps by a fixed layer.

## Save and hand off

Write `docs/architecture/ARCHITECTURE_MASTER.md` with document status/revision,
inputs, system/component map, ownership, flows, interfaces, framework/resource
effects, accepted decision references, gaps, and open questions. Retain existing
useful diagrams and detail. Focused requests change only the affected portions.

Run the applicable TD-ARCHITECTURE and LP-FEASIBILITY review where required
by the task; unavailable required review is explicit. A draft can be saved within
authorization while remaining incomplete. Report COMPLETE or INCOMPLETE for the
declared authoring scope, saved paths, evidence, and remaining decisions.

Use `$architecture-decision` to propose identified decisions, explicit acceptance
for settled decisions, `$architecture-review` for review/traceability, and
`$create-control-manifest` for scoped rules. These are separate activities unless
the current task authorizes them. Do not jump to production or a milestone gate.
