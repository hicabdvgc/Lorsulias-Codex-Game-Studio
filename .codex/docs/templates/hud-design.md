# HUD Design: [Game Name]

> **Status**: Draft | In Review | Approved | Implemented
> **Author**: [assigned person or agent]
> **Last Updated**: [date]
> **Platform Target / Input Methods**: [selected scope; source: live technical preferences]
> **Related GDDs / FRAMEWORK**: [identities, sections and operation responsibilities]
> **Related ADRs**: [applicable accepted decisions; label proposals separately]
> **Accessibility Commitments**: [applicable docs/ACCESSIBILITY.md requirements]

> **Template**: HUD Design

Complete the sections relevant to this design; identify omitted topics and their
reason when the reader would otherwise expect them. Examples are illustrative.
Use developer CONCEPT, applicable GDD/FRAMEWORK decisions and `docs/ACCESSIBILITY.md`.
Read live `docs/technical-preferences.md` for selected technical choices. Link resource
requirements to RES_TYPE/TYPE_TEMP when defined; record unresolved needs in early
design. This design document does not substitute for a resource schema or delivered
resource. Save and accept within actual task authorization and required evidence.

Read [HUD guidance](guidance/hud-design-guide.md) for relevant worked examples.
Select the actual gameplay contexts; combat, maps, health bars and subtitles are
conditional. Preserve information needed by the player under the selected conditions.

## 1. HUD Philosophy
[Purpose, intended attention load, diegetic/screen-space relationship and rationale.]

## 2. Information Architecture
| Information | Player decision served | When needed | Delivery / visibility | Owning system |
|---|---|---|---|---|
| [Information] | [Need] | [Context] | [Chosen method] | [GDD] |

## 3. Layout Zones
### 3.1 Zone Diagram
[Diagram or linked visual for selected displays.]
### 3.2 Zone Specification Table
| Zone | Placement/scaling | Selected safe-area rule and source | Elements | Overlap behavior |
|---|---|---|---|---|
| [Zone] | [Rule] | [Requirement or unresolved] | [IDs] | [Resolution] |

## 4. HUD Element Specifications
### 4.1 Element Overview Table
| Element | Zone | Visibility trigger | Data owner/interface | Update trigger | Priority | Resource/pattern |
|---|---|---|---|---|---|---|
| [Element] | [Zone] | [Rule] | [Contract] | [Trigger] | [Selected rule] | [Reference] |
### 4.2 Element Detail Blocks
For each applicable element specify its visual communication, states, data range
and missing handling, input behavior if interactive, feedback, accessibility
commitments, and evaluation. Reuse named patterns or define local behavior fully.

## 5. HUD States by Gameplay Context
| Actual context | Visible/hidden elements | Changed behavior | Transition / interruption |
|---|---|---|---|
| [Context] | [Elements] | [Rules] | [Behavior] |

## 6. Information Hierarchy
[Resolve concurrent information and conflicts by the actual player decisions and
project requirements. Identify critical cues and alternative communication.]

## 7. Visual Budget
| Selected constraint | Basis | Measurement/evaluation | Actual result |
|---|---|---|---|
| [Constraint or unresolved] | [Requirement] | [Method] | [Pending/result] |

## 8. Feedback & Notification Systems
[Triggers, queuing/merging/interruption and persistence for relevant feedback;
resolve simultaneous cues with audio and UX decisions.]

## 9. Platform Adaptation
[Selected inputs, display sizes, safe areas and scaling. Verify applicable platform
claims using actual requirements; do not infer certification from this template.]

## 10. Accessibility — HUD Specific
[Map docs/ACCESSIBILITY.md commitments to affected elements. Consider non-color
information, text/readability, motion, subtitles and player controls where applicable.
Record evaluation methods and human evidence requirements.]

## 11. Tuning Knobs
| Knob | Selected value/range and unit | Intended effect | Owning contract | Evaluation |
|---|---|---|---|---|
| [Knob] | [Value or unresolved] | [Effect] | [GDD/type] | [Method] |

## 12. Acceptance Criteria
[Trace each relevant information, interaction, integration and experiential outcome
to a feasible check. Distinguish design adequacy, observed runtime and human use.]

## 13. Open Questions
[Missing decisions/evidence, affected activity, responsible person and resolution.]
