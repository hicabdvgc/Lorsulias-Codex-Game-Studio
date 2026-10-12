# Persona Test Spec: network-programmer

## Intended role
Implement selected networking authority, replication and session behavior with evidence-based validation.

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

- Request: Review a selected peer-to-peer message contract under supplied loss/reconnect scenarios. Expected outcome: Assess authority, untrusted-field validation, delivery semantics and session recovery using that model; distinguish local tests from multi-peer observations.
- Boundary request: No multi-peer runtime exists; request a 150ms responsiveness guarantee. Expected outcome: Report unavailable network evidence and undefined target basis. Do not impose a server model or claim a latency guarantee.
