# Architecture Traceability Index

Target: `docs/architecture/architecture-traceability.md`.
Produced by an explicitly authorized `$architecture-review` save. Conversation-only
reviews do not update this file. Preserve entries outside the reviewed scope.

## Document Status
- Reviewed inputs and revisions: [specific GDDs, FRAMEWORK, architecture and ADRs]
- Review scope / reviewer / date: [actual values]
- Saved by: [actual writer]
- Evidence location: [saved record if any, otherwise describe this review's evidence here]
- Engine / package versions: [relevant selected versions, or not applicable]

## Traceability Matrix
| Req ID | Source / system | Requirement | ADR(s) and status | Coverage | Evidence / gap |
|---|---|---|---|---|---|
| [existing TR-ID or explicitly provisional candidate] | [GDD section] | [requirement] | [Accepted / Proposed / Superseded] | [Covered / Partial / Gap / NOT ASSESSED] | [reason] |

Only applicable Accepted decisions establish governing coverage. An identified
proposal remains visible without being counted as accepted coverage. A documented
requirement that needs no ADR can cite its actual governing design with the reason.
TR IDs become durable when saved to the registry; preserve identity across rewording.

## Integration and Decision Findings
[Framework operations, shared interfaces, conflicts, missing dependencies,
affected components, and required corrections. Prioritize by actual impact.]

## Story and Evidence Links (RTM scope)
| TR-ID | Governing decision | Story | Automated / manual / human evidence | Evidence state |
|---|---|---|---|---|
| [ID] | [reference] | [path or not yet authored] | [reference or pending] | [not executed / actual result / missing] |

Story and test absence before their authoring stage is future work. For a requested
implementation verification, missing required evidence remains unassessed. A test
file's existence cannot establish a passing run.

## Result and Follow-up
[PASS / CONCERNS / FAIL / NOT ASSESSED for the declared scope, evidence-backed
findings, and next activity. Saving the index neither accepts decisions nor passes a gate.]
