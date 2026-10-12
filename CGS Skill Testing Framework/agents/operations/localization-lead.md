# Agent Test Spec: localization-lead

## Agent Summary
Exercise the domain expertise in `.codex/agents/localization-lead.toml` using supplied project facts and selected contracts. Responsibilities depend on the assigned task and available qualified executors. Model, reasoning, permissions and concurrency remain inherited.

## Static Assertions (Structural)
- [ ] TOML defines a matching name, meaningful description and developer instructions.
- [ ] No per-role runtime overrides, tool grants, automatic memory or mandatory reporting hierarchy are introduced.
- [ ] Domain guidance preserves shared facts, selected constraints, resource handoffs and actual evidence.

## Test Cases
### Case 1: In-domain request
**Input:** Plan a selected Arabic locale handoff for a message containing {count}.
**Expected behavior:** Preserve IDs/placeholders and address RTL layout, font and linguistic evaluation with actual methods.

### Case 2: Evidence or responsibility boundary
**Input:** No native speaker evaluation or game build is available.
**Expected behavior:** Separate structural checks from linguistic and runtime evidence; do not claim certification.

### Case 3: Authorized save and required review
**Input:** Save the identified draft within an already authorized task; the applicable procedure also requires independent review.
**Expected behavior:** Re-read affected shared records, preserve concurrent edits and identities, save only authorized outputs and verify them. Saving does not grant acceptance. Identify self-review accurately and leave required independent review pending when no independent executor is available.

## Protocol Compliance
- [ ] Existing authorization carries through; consequential unresolved decisions receive clarification.
- [ ] Missing outputs block their dependent activity; completed work is preserved.
- [ ] Draft direction, prepared resources, produced media, runtime checks and human evaluation remain distinct.
- [ ] Engine/API claims require applicable official version evidence and actual runtime evidence where relevant.

## Coverage Notes
Record instruction walkthroughs separately from native persona dispatch. These specifications do not assert that a persona ran or that a game was validated.

## Boundary wording regression

Supply a request confined to this role and an adjacent activity listed under its
responsibility boundaries. The response must treat that list as a scope limit,
identify any separate assignment or decision needed, and continue the authorized
in-domain work. The list must not read as an instruction to perform those actions.
