---
name: reverse-document
description: "Recover design, architecture or concept observations from existing implementation while distinguishing evidence, historical intent and unverified behavior."
---

# Reverse Document

Invoke as `$reverse-document`.

Arguments: `<design | architecture | concept> <single project-local path>`.

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


## Validate input and scope

Require one valid type and one existing file/directory within the project. Reject
missing, multiple, external or invalid input paths with usage and no writes. Read
relevant text source/configuration and applicable instructions; skip generated,
binary, sensitive or denied files. If no usable evidence remains, report BLOCKED.

## Phase 2: Analyze Implementation

**For design docs (GDD):**
- Identify mechanics, rules, formulas, values, states, dependencies, and handled edge cases.

Detailed extraction:
- Identify mechanics, rules, and formulas.
- Extract gameplay values such as damage, cooldowns, and ranges.
- Find state machines, ability systems, and progression.
- Detect edge cases handled in code.
- Map dependencies and system interactions.

**For architecture docs (ADR):**
- Identify implemented patterns, technical constraints, dependencies, coupling,
  trade-offs, and performance characteristics.
- Do not turn a plausible alternative into decision history. Alternatives not
  evidenced by a contemporaneous artifact or explicitly confirmed by the user
  are labeled `Unknown` or `Possible alternative`; `why not chosen` remains
  `Unknown — not recorded`.

Detailed extraction:
- Identify patterns such as ECS, singleton, observer, or service locator.
- Map technical decisions in threading and serialization.
- Map dependencies and coupling.
- Assess evidenced performance characteristics.
- Record constraints and observed trade-offs.

**For concept docs (prototype analysis):**
- Identify the implemented core mechanic and technical feasibility evidence.
- Load prototype outcome, effort/duration, reuse percentage, tester feedback,
  and quotes only from an existing record or explicit user input. Otherwise use
  `N/A — source unavailable`; never invent a quote, tester count, percentage,
  outcome, or effort estimate.

Detailed extraction:
- Identify the core mechanic and emergent gameplay patterns.
- Note what existing records say worked or did not work.
- Capture technical feasibility evidence.
- Separate observed feel from intended player fantasy.


## Clarify and produce the requested artifact

Show the evidenced behavior and unresolved intent. Ask when missing intent would
change the requested design, otherwise retain explicit Unknown fields and continue
the authorized recovery. Do not force a speculative explanation of why code exists.

| Type | Template | Output |
|---|---|---|
| design | design-doc-from-implementation | System GDD path declared in BREAKDOWN, or an explicitly selected recovery path under design/gdd/ |
| architecture | architecture-doc-from-code | Identifiable Proposed adr-NNNN-[slug].md under docs/architecture/ |
| concept | concept-doc-from-prototype | prototypes/[name]/concept-observations.md |

Templates live under `.codex/docs/templates/`. Resolve target identity without
overwriting an existing governing document implicitly. Use `$architecture-decision`
numbering/dependency conventions for recovered ADRs and record origin separately
from status. Existing implementation does not prove decision acceptance.

Preserve the templates' evidence boundaries and explain framework/resource
integrations that are actually observed. Missing schemas or design history remain
unknown. Only update BREAKDOWN or registry references if the current task includes
those affected entries; do not automatically approve recovered material.

Verify the saved output and report source paths, observations, inferred/user-stated
intent, unresolved discrepancies, and the next design/review activity. Recovered
concept notes must never replace or automatically edit developer-authored CONCEPT.
