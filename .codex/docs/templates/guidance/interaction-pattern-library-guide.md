> Adapted from Claude Code Game Studios. The material below consists of worked
> design examples and candidate considerations, not selected project requirements.
> Apply only relevant patterns and inputs. Numeric values, default states, layouts,
> control mappings and feedback rules describe the example; choose actual values
> from the project contracts. Accessibility follows `docs/ACCESSIBILITY.md`.
> Data ownership follows accepted architecture; event-only writes are not imposed.
> Read only the relevant sections while using the corresponding Codex template.

> Authoring guidance for interaction-pattern-library.md. Load only the part covering the section currently being authored — not the whole file at once.

# Interaction Pattern Library — Guidance Index

The guidance for this template is split by major section so consumers can load
one part at a time. Read the file matching the section you are currently
authoring — only the relevant portions.

| Template Section | Guidance File |
|------------------|---------------|
| Standard Control Patterns (Button variants, Toggle, Slider, Dropdown / Select, List Item, Grid Item, Modal Dialog, Confirmation Dialog, Toast / Notification, Tooltip, Progress Bar, Input Field, Tab Bar, Scroll Container) | `.codex/docs/templates/guidance/interaction-pattern-library-guide-standard-controls.md` |
| Game-Specific UI Patterns (Inventory Slot, Ability / Skill Icon, Health / Resource Bar, Dialogue Box, Context Action Prompt, Damage Number) | `.codex/docs/templates/guidance/interaction-pattern-library-guide-game-specific.md` |
| Navigation Patterns + Feedback and Loading Patterns (Screen Push / Pop / Replace, Focus Management, Escape / Cancel, Loading State, Empty State, Error State) | `.codex/docs/templates/guidance/interaction-pattern-library-guide-navigation-feedback.md` |

Each guidance file contains the full reference specification for its patterns —
When to Use / When NOT to Use rationale, illustrative state tables and design rationale; timing, audio and accessibility choices remain project-selected. Use
them as the worked-example source when filling the corresponding skeleton stubs
in the template. The Pattern Catalog Index, Animation Standards, Sound
Standards, and Open Questions sections remain in the template itself.
