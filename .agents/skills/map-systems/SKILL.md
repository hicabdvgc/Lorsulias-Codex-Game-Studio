---
name: map-systems
description: "Create or revise preliminary/full BREAKDOWN and route the next selected system into detailed design."
---

# Map Systems

Invoke as `$map-systems`.

Arguments: `[next | system-name] [--review full|lean|solo]`. A decomposition request may specify Preliminary or Full maturity in its task text.

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


## Resolve scope and inputs

No positional argument creates or revises `design/gdd/BREAKDOWN.md`. Preserve its
declared maturity unless the request changes it; a new breakdown starts Preliminary.
Ask when a requested maturity is ambiguous. `next` and a system name only select
from an existing readable BREAKDOWN; they never fall back to decomposition.
Reject unknown flags, conflicting modes, ambiguous system names, or an unreadable
inventory with BLOCKED and no writes.

Read the developer's CONCEPT, relevant root `game_ref/` studies and actual human
observations, MDA analysis and applicable engine findings. Identify missing required
preparation evidence. A draft can expose gaps, but cannot claim full preparation.
Preliminary breakdown does not require FRAMEWORK. Full breakdown uses developed
framework principles; the preliminary FRAMEWORK document can be authored alongside it.

## Decompose and connect

1. Extract systems explicitly motivated by the concept; identify inferred systems separately.
2. For each system explain its purpose, owned behavior, inputs/outputs and why it is separate.
3. Map dependencies, shared facts, interaction direction, and boundaries that need a decision.
4. Inspect dependency cycles. A bidirectional gameplay interaction needs an explicit
   protocol/ownership arrangement; it is not automatically an invalid architecture cycle.
5. Propose a useful design order and project-defined priorities. Do not force layers,
   category counts, MVP definitions, or estimate schedules without supporting evidence.
6. For Full maturity, check how each boundary supports the developed addition/modification routes.

Use `.codex/docs/templates/systems-index.md`. Preserve stable system IDs, existing
GDD paths and evidenced statuses. A system GDD is identified by its BREAKDOWN entry;
CONCEPT, BREAKDOWN, optional aids and review documents are not system GDDs.
Resolve consequential boundary choices, then save the authorized inventory and
report changed systems, maturity, dependencies, gaps and proposed next design.

## Review and next-system handoff

Use TD-SYSTEM-BOUNDARY, CD-SYSTEMS and PR-SCOPE where applicable to the requested
review; use their current gate vocabularies. Insufficient capacity evidence leaves
a schedule/scope assessment NOT ASSESSED rather than optimistic by default.

`next` selects the first eligible undesigned system in the declared design order;
report ambiguity if none is determinable. Named mode selects the unique matching
entry. `$design-system` requires Full BREAKDOWN and preliminary FRAMEWORK. If those
are absent, identify framework preparation through the development-framework
template as the next activity. Honor any supplied authorization to proceed with
the selected design; do not silently loop through all remaining systems.
