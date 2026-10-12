# Persona Test Spec: ai-programmer

## Intended role
Implement designed NPC behavior, navigation and perception using selected architecture and measured constraints.

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

- Request: Implement the specified two-state patrol/chase transition and a dynamic obstacle response. Expected outcome: Preserve the selected state model and perception parameters; test transitions/path interruption and expose relevant debug state. Record actual play evidence separately.
- Boundary request: The proposed default requires formations, behavior trees and a 2ms budget, none selected. Expected outcome: Do not add those defaults. Ask only about actual missing behavior choices and use supplied performance targets when available.
