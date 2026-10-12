---
name: code-review
description: Review selected implementation against applicable design, accepted architecture,
  project standards and actual verification evidence.
---

# Code Review

Invoke as `$code-review`. Arguments: `[one-or-more-source-paths] [optional-story-path]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Require at least one identifiable implementation target; clarify an absent target. Resolve
files and actual roots, then read relevant story/GDD/FRAMEWORK requirements, accepted decisions,
CONTROL, coding standards and scoped instructions. Empty/unreadable targets yield NOT ASSESSED.
Proposed, missing or superseded governing decisions cannot establish accepted compliance;
report their state and effect. A justified absence of an applicable ADR is distinct from a gap.

Inspect correctness and edge cases, boundaries and dependency direction, ownership/lifetimes,
error handling, resource/import contracts, concurrency and testability as relevant. Apply SOLID
or other patterns when they help assess actual project obligations; do not impose a universal
layering or fixed standards checklist. Inspect hardcoded design values only against selected
configuration/resource boundaries. Consider game-loop allocations, loading, save compatibility,
input/accessibility and multiplayer authority where present. Static performance concerns are
hypotheses until measured. Review tests/protocols and actual results for every applicable type.

Use available qualified engine/QA expertise when needed and authorized; missing required expert
or independent evidence remains unassessed. Verify technical claims for selected engine/package
versions using official references; library baselines do not prove installed compatibility.

Return findings tied to exact paths/locations with consequence, evidence and a proportionate
correction; distinguish required changes from suggestions and relevant positive observations.
Use **APPROVED / APPROVED WITH SUGGESTIONS / CHANGES REQUIRED / NOT ASSESSED**, keeping failures
visible alongside gaps. A passing conclusion requires all applicable required checks. Default
review is conversational and read-only; a requested report save is bounded and does not approve
story closure or merging. Implementing fixes requires a request covering those changes.
