# Architecture Decision Handoff Contract

Adapted from the Claude architecture-decision contract.

## Inputs

A decision subject, or unique existing ADR for retrofit/accept; relevant design,
FRAMEWORK, master architecture and accepted stance context; technical preferences
and versioned evidence where the decision depends on an engine. Acceptance also
requires actual authorization and all applicable dependency/review evidence.

## Outputs and guarantees

- New `docs/architecture/adr-NNNN-[slug].md`: Proposed, with the decision, rationale,
  consequences, explicit Depends On declarations, design/requirement links,
  framework/resource effects and evaluation criteria. Use the adapted ADR template.
- Retrofit: identified missing/incorrect portions repaired; valid unrelated content retained.
- Acceptance: uniquely identified decision set Accepted with provenance; applicable
  registry stances synchronized; explicitly replaced decisions/states retain history.
- Conversation: actual mode/status, reviewed evidence, saved paths, unresolved
  checks, affected CONTROL/traceability consumers and next activity.

Verify every promised file after saving. Proposed stances are candidates, not
governing rules. A technical review result is distinct from acceptance authority.

## Permitted changes

Only the target ADR and explicitly included design-sync, acceptance-registry and
supersession files. Re-read before writes to preserve concurrent work. Do not
change stories, install engines, update persona settings or create review receipts.
If interrupted, preserve completed work, identify any incomplete acceptance/registry
handoff and prevent consumers treating that partial operation as fully synchronized.

## Consumers

Architecture review reads decision status, dependencies, technical evidence and
requirement links. CONTROL derives obligations only from applicable Accepted
decisions and explicit project choices. Installed work-item procedures consume those
contracts where applicable to the requested work. No absent runner or automated status propagation
is promised by this contract.
