# Vertical Slice Report: [Concept / run]

Date: [actual date]
Build/revision and runtime location: [identifiable output]
Scope and learning question: [intended experience and feasibility question]
Sources: [developer CONCEPT, relevant GDD/FRAMEWORK, UX, accepted decisions and resource/tool contracts]

## Scope built
Describe included systems, representative quality, deliberate shortcuts and omissions. Identify actual
outputs and incomplete work. Record changed scope and its authorization. No fixed playtime applies.

## Framework and integration evidence
| Operation | Added or modified result | Affected systems/resources/tools | Method and actual evidence | Result/limitations |
|---|---|---|---|---|
| Addition | [actual operation] | [consumers] | [revision, input, action, observation] | [pass/fail/unassessed] |
| Modification | [actual operation] | [consumers] | [revision, input, action, observation] | [pass/fail/unassessed] |

## Build observations
Record actual effort/elapsed time only when measured, plus dependencies and pipeline surprises.
Estimates for later work require comparable scope/capacity; leave unsupported forecasts explicit.

## Playtest and usability
Link actual sessions under production/playtests/ or explicit legacy paths. Identify participants,
build/platform/input, protocol, observations, confusion/success/experience findings and limitations.
Separate observed facts from interpretations. Unperformed human checks stay pending.

## Relevant measurements
| Selected goal/metric and units | Supplied target or unknown | Actual result and method | Limitation |
|---|---|---|---|
| [relevant criterion] | [basis] | [actual evidence] | [gap] |

## Recommendation and decisions
PROCEED / PIVOT / KILL / NOT ASSESSED: [evidence against the question and required outcomes].
Preserve failures alongside missing evidence. Identify actual reviewers and required independence.
Record consequential developer decisions separately from recommendations. Include lessons learned,
retention/refactoring/disposal decisions, affected GDD/ADR/framework changes and follow-up verification.

## Handoff
Use slice experience for epics/stories and readiness, then `$gate-check vertical-slice` for the hard gate.
Finalize MILESTONE afterwards. Missing required human/framework evidence prevents progression. A saved
report or PROCEED recommendation does not independently advance the phase or require rewriting all code.
