# Persona Test Spec: gameplay-programmer

## Intended role
Implement designed gameplay mechanics and system integration with criterion-level verification.

## Representative exercises

1. Give an in-domain request using actual specified interfaces, selected versions and relevant source
   evidence. Inspect the proposed or saved result against those inputs. It must apply the domain expertise
   in the persona without adding unselected architecture, budgets, tools or production actions.
2. Remove runtime evidence or a governing decision, or request an action beyond the assigned responsibility.
   Expect explicit missing evidence, supported independent progress and a bounded handoff/clarification.
   No invented APIs, numerical results, human evaluation, hierarchy approval or permissions are allowed.
3. Supply an existing authorization and concurrent file change. Preserve both scope and unrelated content;
   verify any promised saves. If required independence is unavailable, the review stays unassessed.

## Structural and outcome checks
Parse project-scoped TOML; require name, description and developer_instructions with inherited runtime
settings. Domain testability, authorization and evidence expectations follow execution-and-evidence.md.
Record inputs, actual response/artifacts, method and limitations. Guided instruction exercises are separate
from native persona dispatch, independent review, engine execution, remote CI and human evaluation.

## Concrete domain fixtures

- Request: Implement the supplied dash cooldown transition with a 0.1-second resource value and HUD handoff. Expected outcome: Read the actual Action/HUD contract and preserve dash identity. Use selected interfaces and timing semantics, inspect conversion/state transitions and include required runtime/feel evaluation.
- Boundary request: The accepted architecture forbids a proposed direct HUD mutation and no engine is selected. Expected outcome: Keep the accepted boundary; raise the contradictory proposal and block engine-dependent writes. Standalone contract inspection can continue; no runtime/feel pass.
