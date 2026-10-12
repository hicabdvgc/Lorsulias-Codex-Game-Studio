# Detailed System Authoring and Revision

## Explain behavior before implementation

- **Overview:** state what the system does, the player's interaction, and why its
  boundary exists. Separate behavior requirements from unchosen implementation.
- **Player fantasy:** describe the relevant intended experience and its concept/study basis.
- **Core rules and states:** define conditions, actions, results, transitions,
  interruptions and interactions. Distinguish the producer/consumer of shared values.
- **Formulas:** when rules are numerical, state variables, units, valid domains,
  output ranges, tuning intent, boundary cases and worked examples. Check arithmetic
  and relevant extremes. Label untested balance targets as hypotheses.
- **Edge cases:** specify the outcome when inputs are absent, limits are reached,
  actions overlap, or relevant state changes. Cover actual mechanics, not hypothetical systems.
- **Dependencies:** link the exact owning rule/interface, direction and change effect.
  Update affected reciprocal references when authorized; otherwise report the needed edit.
- **Tuning:** identify meaningful parameters, ownership and justified ranges. A proposed
  range is not a measured safe range until evidence supports that claim.
- **Presentation/UI/feel:** specify relevant information, feedback and interaction.
  Use selected accessibility commitments if available. Performance/latency targets
  need project rationale; observed feel needs an actual human session.
- **Acceptance:** define a usable evaluation method for each required outcome,
  including calculations, inspection, execution or human observation as appropriate.

## Framework and resource integration

Walk an addition and a modification through the applicable framework routes.
Describe ownership, input/output contracts, affected systems and validation.
Record resource properties, relationships, presentation needs and unresolved type
questions. Later RES_TYPE/templates constrain the later integration revision;
their absence is expected in initial design and cannot block that draft.

## Shared facts and authorized writes

Read `design/registry/entities.yaml` before recording cross-system facts. Preserve
the owning source, append actual consumers, and identify conflicting values rather
than silently choosing one. Update only relevant facts within the authorized scope.
Existing unrelated entries remain unchanged; reread before saving and resolve any
conflicting concurrent edit. The registry is an index of design facts, not RES_TYPE.

Preserve stable system identifiers and approved content during retrofit. Insert
missing applicable information and repair demonstrated contradictions. Update the
BREAKDOWN path and design state to match actual work: authoring normally yields
In Design or In Review, not Approved or Implemented without their required evidence.

## Review and recovery

Run an author self-check against the design's actual requirements. Requested gate
reviews use their defined vocabularies and evidence. Keep independent design review
separate from the authoring role; follow the runtime's delegation rules. If an
independent reviewer is unavailable, report that review NOT ASSESSED and leave its
dependent approval pending. A fresh context is useful but does not guarantee an
unbiased or independent review merely by being labeled a new session.

On interruption, preserve completed sections and leave a manual checkpoint with
the system, written paths, open decisions and next activity. Do not claim automatic
session files or memory. Verify promised outputs before a downstream handoff.
