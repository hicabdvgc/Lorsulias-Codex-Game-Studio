---
name: adopt
description: Audit existing project interfaces and produce a scoped, evidence-based
  adoption plan.
---

# Adopt an Existing Project

Invoke `$adopt [full|gdds|adrs|stories|infra]`; default full. Reject unsupported selectors.

Read root instructions and the shared contracts linked below. Carry existing bounded task authorization
through saves; clarify consequential unresolved choices. Reread shared files before writes, preserve
concurrent changes and stable identities, and read back promised outputs. Required independent review
and actual human evidence survive executor changes and review-depth choices. Report missing evidence
and preserve partial work; a saved document never establishes approval or execution.

Read `.codex/docs/workflow-catalog.yaml`, `.codex/docs/progression.md`, live
`docs/technical-preferences.md` and relevant current artifacts. The four section IDs are
conceptualization, development-schematics, pre-implementation, implementation. Report the declared
section separately from available outcomes and missing prerequisites. Preserve unknown/legacy stage
values until their interpretation is explicitly resolved; counts/existence cannot establish progress.
Story Status fields own progress; selected sprint YAML is derived. Active scope needs an explicit or
unique existing reference, never modification time. There is no review-mode file to create.

## Inspect compatibility

Root instructions and live preferences define the project. Resolve actual roots through
code-root-resolution.md; include nested packages and non-Git projects. Inspect artifacts in the selected
scope and identify their actual downstream consumers. Read each consumer's current interface before
classifying a difference. Harmless heading/layout variation is not automatically a blocker.

- gdds: preliminary/full BREAKDOWN and FRAMEWORK maturity, identifiable systems, boundaries,
  dependencies, applicable interactions, integration and unresolved resource needs. Early GDDs need
  no future schemas. Later integration needs applicable RES_TYPE/TYPE_TEMP and library evidence.
- adrs: decision identity/status/provenance, explicit dependencies, accepted stances, durable TR
  references, master architecture and integer CONTROL. Proposed decisions do not govern readiness.
- stories: stable epic/story IDs, authoritative Status, inputs versus created outputs, criterion-level
  evidence and applicable Accepted ADR/TR/CONTROL or justified N/A; inspect derived sprint conflicts.
- infra: catalog/artifact locations, live preferences/actual roots, registries, resources/tools,
  applicable test routes, recovery format and selected stage. Missing optional infrastructure is not
  a universal blocker. Shared registries retain stable IDs and concurrent content.

For an identified infrastructure project, the optional `.codex/scripts/project-coherence.sh
--project <actual root> --root <studio>` observer can compare live preferences with
readable metadata. Read `.codex/docs/project-coherence.md`; retain unknowns and nonzero
execution errors. It launches no command and establishes neither readiness nor a completed migration.

## Produce a migration plan

For each actual gap show the observed source, consumer affected, practical impact, proposed bounded
repair, prerequisites and verification. Classify BLOCKING only where the affected activity cannot work;
use HIGH/MEDIUM/LOW for other evidenced impacts. Keep unresolved assessment explicit. Avoid unsupported
time estimates, universal section counts and automatic Ready/status promotion.

Order repairs by actual dependencies. Reuse installed authoring/retrofit skills: accepted decisions
must remain accepted only with their evidence; document format repair never accepts a decision.
Optional stage changes still use progression rules. Do not create review-mode configuration.

Save the requested plan to docs/adoption-plan-[date].md, preserving previous plans. On a same-day
collision, reread and update the same requested scope or resolve a distinct path. Return exact saved
path, highest-impact next activity and unresolved inputs. The plan does not execute migrations or
rewrite project documents. A read-only audit request remains conversational without a plan save.
