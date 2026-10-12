---
name: architecture-review
description: "Review architecture coverage, consistency and engine evidence; optionally save stable traceability or produce an RTM within the requested scope."
---

# Architecture Review

Invoke as `$architecture-review`.

Arguments: `[full | coverage | consistency | engine | single-gdd <path> | rtm]`.

## Shared execution boundary

Read the relevant artifacts before asking about information they contain. Existing
bounded task authorization covers its edits and verification; ask about unresolved
consequential choices or a material scope expansion. Preserve unrelated changes
and re-read a target before writing if its baseline may have changed.

Use available qualified executors under the current environment's delegation
policy. Role names describe expertise. Follow `.codex/docs/review-workflow.md`
and `.codex/docs/director-gates.md`: required independent review and human evidence
remain required with any executor. Identify self-review; unavailable required
evidence is NOT ASSESSED. The six modes below define review scope. A requested reduction in optional
breadth cannot waive these obligations. Identify self-review explicitly; the
default scope for this skill is full.

Apply `.codex/docs/skill-authoring.md` and `.codex/docs/error-recovery-protocol.md`.
Verify promised saved outputs before handoff. Resolve available support from the
installed catalog; require an input only when the selected activity needs its outcome.


## Mode and write boundaries

Default full. Reject unsupported modes/flags. `single-gdd` requires one existing
project-local system GDD identified by BREAKDOWN, not CONCEPT or another governance
document. Resolve actual ADRs separately from CONTROL, master architecture and reports.

| Mode | Reads / checks | Authorized artifact production, when requested |
|---|---|---|
| full | Relevant GDDs, full FRAMEWORK, master architecture, ADRs, registries, applicable engine evidence | Scoped traceability index / TR registry and requested report |
| coverage | GDD requirements and governing ADR/design coverage | Scoped traceability index / TR registry |
| consistency | ADRs, declared dependencies and architectural stances | Requested report only |
| engine | ADR version/API claims and applicable project/reference evidence | Requested report only |
| single-gdd | Target GDD and its related decisions/requirements/framework routes | Target rows in traceability index / TR registry |
| rtm | GDD → governing decision → story → actual evidence linkage | RTM and required TR registry entries |

Reviews are read-only and conversational by default. An explicit request to save
traceability or produce the RTM authorizes that bounded output. `rtm` is a request
to produce `docs/architecture/requirements-traceability.md`; disclose its necessary
registry updates. A request to inspect only remains read-only in any mode. Report
findings without editing reviewed GDDs/ADRs, changing acceptance, or writing receipts.

## Requirements and coverage

Read the full relevant inputs; summaries help discovery but cannot establish
coverage. Build the system set from BREAKDOWN and explicit GDD references, retaining
missing promised GDDs as gaps rather than silently shrinking the scope.

Read `docs/architecture/tr-registry.yaml`. Reuse stable IDs when intent is the same,
preserve IDs through wording changes, and ask about ambiguous identity. New IDs
are provisional in conversation until saved. Skip deprecated/replaced requirements
as active obligations while retaining their history and replacement links.

Assess each applicable requirement: Covered / Partial / Gap / NOT ASSESSED.
Only Accepted ADRs provide accepted architectural coverage. Proposed decisions are
visible candidates; Superseded decisions require replacement review. Not every
requirement needs a separate ADR: cite the actual governing design and rationale.
Check framework additions/modifications and relevant resource/tool interfaces.
Future schemas are distinct from missing contracts required by a selected integration check.

## Consistency and engine evidence

Check conflicting ownership, interface types, assumptions and obligations. Use
`.codex/scripts/adr-dep-graph.sh` to observe dependencies, missing declarations,
missing targets, identity mismatches, duplicates and cycles; read affected records to judge the result.
A failed helper is unavailable evidence, not an empty clean graph.

Compare applicable ADR claims with the actual selected engine/package versions and
verified official references. A library baseline does not pin the project. Missing
required specialist/runtime evidence remains NOT ASSESSED; no model-cutoff heuristics.
Identify GDD revisions needed when verified technical constraints contradict design.

Read [references/continued-workflow.md](references/continued-workflow.md) for
result aggregation, traceability saving, RTM evidence and concurrent-change handling.
