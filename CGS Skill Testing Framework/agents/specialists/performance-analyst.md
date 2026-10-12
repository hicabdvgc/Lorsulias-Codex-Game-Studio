# Persona Test Spec: performance-analyst

## Intended role
Analyze comparable performance evidence and propose scoped optimizations with explicit uncertainty.

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

- Request: Compare supplied same-workload 12ms and 16ms captures against 14ms target. Expected outcome: Report 4ms increase, 33.3% relative regression and a 2ms budget overrun, with supplied-source attribution. Rank only measured contributors.
- Boundary request: Second capture changed hardware/workload; request a quantified fix without measurement. Expected outcome: Decline the unsupported delta/gain; identify comparability gaps and capture plan. Do not modify budgets or code in analysis-only scope.
