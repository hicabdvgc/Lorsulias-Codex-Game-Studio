# Interaction Pattern Library: [Game Title]

> **Status**: Draft | Stable | Under Revision
> **Author**: [assigned responsibility]
> **Last Updated / Version**: [project revision]
> **Engine / UI Framework**: [selected choices from live technical preferences]
> **Template**: Interaction Pattern Library

Complete the sections relevant to this design; identify omitted topics and their
reason when the reader would otherwise expect them. Examples are illustrative.
Use developer CONCEPT, applicable GDD/FRAMEWORK decisions and `docs/ACCESSIBILITY.md`.
Read live `docs/technical-preferences.md` for selected technical choices. Link resource
requirements to RES_TYPE/TYPE_TEMP when defined; record unresolved needs in early
design. This design document does not substitute for a resource schema or delivered
resource. Save and accept within actual task authorization and required evidence.

Use `design/ux/interaction-patterns.md` as the shared output. See the
[guidance index](guidance/interaction-pattern-library-guide.md) for worked examples.
Screen-specific behavior may be specified locally; a claimed shared pattern must
resolve to a complete persisted entry. Saving a draft does not accept it.

## How to Use This Library
Find relevant existing patterns before creating one. Record selected behavior,
provenance, known consumers and actual evaluation. Preserve stable pattern identity
when wording changes. Document replacement/retirement and affected screen updates.
Re-read before shared edits and preserve concurrent changes.

Document status describes this library revision. Individual entries use Draft,
Stable or Deprecated: Stable requires the recorded project acceptance and actual
implementation/evaluation evidence; a design-only pattern can remain Draft.

## Pattern Catalog Index
| Pattern name / identity | Category | Purpose | Used in | Status | Evidence / entry |
|---|---|---|---|---|---|
| [Selected pattern] | [Category] | [Purpose] | [Actual consumers] | [Status] | [Link] |

## Standard Control Patterns
[Add only needed controls. Candidate examples include Button variants, Toggle,
Slider, Dropdown / Select, List Item, Grid Item, Modal Dialog, Confirmation Dialog,
Toast / Notification, Tooltip, Progress Bar, Input Field, Tab Bar and Scroll Container.]

## Game-Specific UI Patterns
[Add patterns required by actual game systems, such as Inventory Slot or Dialogue Box.]

## Navigation Patterns
[Selected screen transitions, focus, cancellation and return-state behavior.]

## Feedback and Loading Patterns
[Applicable loading, empty, error and recovery behavior.]

### Reusable entry structure
- **Name / identity and status**: [preserve existing identity].
- **Purpose; when to use / alternatives**: [fit and limitations].
- **Used in / source decisions**: [consumers and provenance].
- **States and transitions**: [trigger, resulting behavior, interruption/recovery].
- **Inputs**: [selected mappings and focus behavior].
- **Visual/audio/haptic feedback**: [selected requirements and rationale].
- **Data/interface/resource contracts**: [ownership, TYPE_TEMP or unresolved needs].
- **Accessibility/localization**: [applicable commitments and selected locales].
- **Implementation notes**: [verified selected engine/package evidence, or unresolved].
- **Evaluation and evidence**: [design inspection, actual execution and human use].

## Animation Standards
[Selected timing, interruption and applicable reduced-motion behavior; no default durations.]

## Sound Standards
[Link relevant design/audio/sound-bible.md decisions; resolve conflicting cues.]

## Open Questions
[Decisions, evidence gaps, affected consumers and responsible person.]
