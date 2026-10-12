# UX Specification: [Screen / Flow Name]

> **Status**: Draft | In Review | Approved | Implemented
> **Author**: [assigned person or agent]
> **Last Updated**: [date]
> **Platform Target / Input Methods**: [selected scope; source: live technical preferences]
> **Related GDDs / FRAMEWORK**: [identities, sections and operation responsibilities]
> **Related ADRs**: [applicable accepted decisions; label proposals separately]
> **Accessibility Commitments**: [applicable docs/ACCESSIBILITY.md requirements]

> **Template**: UX Spec
> **Related UX Specs**: [entry/exit neighbors and shared patterns]

Complete the sections relevant to this design; identify omitted topics and their
reason when the reader would otherwise expect them. Examples are illustrative.
Use developer CONCEPT, applicable GDD/FRAMEWORK decisions and `docs/ACCESSIBILITY.md`.
Read live `docs/technical-preferences.md` for selected technical choices. Link resource
requirements to RES_TYPE/TYPE_TEMP when defined; record unresolved needs in early
design. This design document does not substitute for a resource schema or delivered
resource. Save and accept within actual task authorization and required evidence.

Use this template for a discrete screen/flow; persistent gameplay overlays use the
HUD template. Read [UX authoring guidance](guidance/ux-spec-guide.md) for relevant
worked examples. Examples do not select platforms, architecture, budgets or commitments.

## 1. Purpose & Player Need
[Player goal, why this screen is needed, and intended experience.]

## 2. Player Context on Arrival
[Trigger, prior activity, carried information/state, urgency and relevant journey.]

## 3. Navigation Position
[Hierarchy or navigation graph; modal/overlay behavior; game pause behavior.]

## 4. Entry & Exit Points
| Trigger / action | Source / destination | Transition | Data carried or committed | Failure / cancellation |
|---|---|---|---|---|
| [Entry or exit] | [Identity] | [Behavior] | [Data] | [Applicable handling] |

## 5. Layout Specification
### 5.1 Wireframe
[Sketch, ASCII layout or linked visual when useful.]
### 5.2 Zone Definitions
| Zone | Contents and purpose | Layout / size basis | Overflow / scaling |
|---|---|---|---|
| [Zone] | [Information] | [Selected rule] | [Behavior] |
### 5.3 Component Inventory
| Component | Type / purpose | Zone | Shared pattern or local behavior | Resource needs |
|---|---|---|---|---|
| [Component] | [Purpose] | [Zone] | [Identity/link] | [Type/reference or unresolved] |
### 5.4 Information Hierarchy
[What needs attention first and why; focus on entry where the selected input needs it.]

## 6. States & Variants
| State | Trigger | Visual / behavioral changes | Recovery / next state |
|---|---|---|---|
| [Applicable state] | [Trigger] | [Behavior] | [Outcome] |
[Include loading only with async work/delay; empty, error, locked or other states
follow actual behavior. Explain relevant inapplicability.]

## 7. Interaction Map
### 7.1 Navigation Inputs
| Selected input | Context | Action | Feedback | Destination / cancellation |
|---|---|---|---|---|
| [Input] | [State/focus] | [Action] | [Selected feedback] | [Outcome] |
### 7.2 Action Inputs
| Action | Selected inputs | Preconditions | Response | Data / integration effect |
|---|---|---|---|---|
| [Action] | [Mappings] | [State] | [Feedback] | [Contract] |
### 7.3 State-Specific Behaviors
[Restrictions, focus/input changes, retries and cancellation where applicable.]

## 8. Data Requirements
| Data | Owning system | Read/write interface | Update trigger | Format / TYPE_TEMP | Missing handling |
|---|---|---|---|---|---|
| [Data] | [Owner] | [Accepted interface] | [Trigger] | [Contract] | [Behavior] |
[Follow actual accepted architecture. This template does not impose event-only writes.]

## 9. Events Fired
| Player action | Existing event/call or none | Payload | Receiver | Result |
|---|---|---|---|---|
| [Action] | [Accepted contract] | [Data] | [Owner] | [Behavior] |
[Do not invent telemetry or new architecture to populate this table.]

## 10. Transition & Animation
| Transition | Trigger | Timing / interruption | Feedback | Applicable reduced-motion behavior |
|---|---|---|---|---|
| [Transition] | [Trigger] | [Selected values and basis] | [Response] | [Commitment] |

## 11. Input Method Completeness Checklist
[For each selected input, trace required actions, focus/navigation, cancellation,
remapping and interruption/disconnection behavior where applicable. Unselected
inputs are outside scope; unknown authoritative input prevents a complete check.]

## 12. Screen-Level Accessibility Requirements
| Commitment | Affected element/interaction | Design response | Evaluation method | Evidence |
|---|---|---|---|---|
| [Project requirement] | [Element] | [Response] | [Human or executable check] | [Pending/result] |

## 13. Localization Considerations
| Text/resource | Selected locales | Placeholder / identity | Layout constraints | RTL/overflow behavior |
|---|---|---|---|---|
| [Resource] | [Locales] | [Contract] | [Selected constraint] | [Applicable behavior] |
[Use actual content, fonts and selected languages; no English or expansion-percent default.]

## 14. Acceptance Criteria
| Outcome | Method and representative case | Expected result | Actual evidence |
|---|---|---|---|
| [Functional, integration, performance or experiential outcome] | [Feasible method] | [Criterion] | [Pending until assessed] |
[Design review, implementation tests and human evaluation are distinct.]

## 15. Open Questions
| Question / missing evidence | Affected activity | Responsible person | Resolution |
|---|---|---|---|
| [Issue] | [Dependency] | [Assigned] | [Pending/decision] |
