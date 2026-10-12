# Technical Preferences

<!-- Template for docs/technical-preferences.md; copy and fill only confirmed choices. -->
<!-- All agents reference this file for project-specific standards and conventions. -->

## Engine & Language

- **Engine**: [TO BE CONFIGURED — run $setup-engine]
- **Engine Version**: [TO BE CONFIGURED — project selection, not library baseline]
- **Installed Version Evidence**: [NOT ASSESSED until observed or supplied]
- **Language**: [TO BE CONFIGURED]
- **Rendering**: [TO BE CONFIGURED]
- **Physics**: [TO BE CONFIGURED]

## Input & Platform

<!-- Written by $setup-engine. Read by $ux-design, $ux-review, $test-setup, $team-ui, and $dev-story -->
<!-- to scope interaction specs, test helpers, and implementation to the correct input methods. -->

- **Target Platforms**: [TO BE CONFIGURED — e.g., PC, Console, Mobile, Web]
- **Input Methods**: [TO BE CONFIGURED — e.g., Keyboard/Mouse, Gamepad, Touch, Mixed]
- **Primary Input**: [TO BE CONFIGURED — the dominant input for this game]
- **Gamepad Support**: [TO BE CONFIGURED — Full / Partial / None]
- **Touch Support**: [TO BE CONFIGURED — Full / Partial / None]
- **Platform Notes**: [TO BE CONFIGURED — any platform-specific UX constraints]

## Naming Conventions

- **Classes**: [TO BE CONFIGURED]
- **Variables**: [TO BE CONFIGURED]
- **Signals/Events**: [TO BE CONFIGURED]
- **Files**: [TO BE CONFIGURED]
- **Scenes/Prefabs**: [TO BE CONFIGURED]
- **Constants**: [TO BE CONFIGURED]

## Performance Budgets

- **Target Framerate**: [TO BE CONFIGURED]
- **Frame Budget**: [TO BE CONFIGURED]
- **Draw Calls**: [TO BE CONFIGURED]
- **Memory Ceiling**: [TO BE CONFIGURED]

## Testing

- **Framework**: [TO BE CONFIGURED]
- **Minimum Coverage**: [TO BE CONFIGURED]
- **Required Tests**: [TO BE CONFIGURED from actual requirements]

## Forbidden Patterns

<!-- Add patterns that should never appear in this project's codebase -->
- [None configured yet — add as architectural decisions are made]

## Allowed Libraries / Addons

<!-- Add approved third-party dependencies here -->
- [None configured yet — add as dependencies are approved]

## Architecture Decisions Log

<!-- Quick reference linking to full ADRs in docs/architecture/ -->
- [No ADRs yet — use $architecture-decision to create one]

## Engine Specialists

<!-- Written by $setup-engine when engine is configured. -->
<!-- Read by $code-review, $architecture-decision, $architecture-review, and team skills -->
<!-- to identify a qualified available specialist for engine-specific validation. -->

- **Primary**: [TO BE CONFIGURED — run $setup-engine]
- **Language/Code Specialist**: [TO BE CONFIGURED]
- **Shader Specialist**: [TO BE CONFIGURED]
- **UI Specialist**: [TO BE CONFIGURED]
- **Additional Specialists**: [TO BE CONFIGURED]
- **Routing Notes**: [TO BE CONFIGURED]

### File Extension Routing

<!-- Skills use this table to select the right specialist per file type. -->
<!-- If a row says [TO BE CONFIGURED], report missing routing; a qualified available executor may handle the work. -->

| File Extension / Type | Relevant Specialist |
|-----------------------|---------------------|
| Game code (primary language) | [TO BE CONFIGURED] |
| Shader / material files | [TO BE CONFIGURED] |
| UI / screen files | [TO BE CONFIGURED] |
| Scene / prefab / level files | [TO BE CONFIGURED] |
| Native extension / plugin files | [TO BE CONFIGURED] |
| General architecture review | Primary |

## Source, Test, and Resource Integration Locations

- **Project / Code Roots**: [TO BE CONFIGURED from the actual engine project]
- **Test Roots and Commands**: [TO BE CONFIGURED; actual project/module test roots, runner/version, commands and report locations]
- **Resource Import Mapping**: [TO BE CONFIGURED when resource contracts are defined]

## Authority and Evidence

This document records selected project choices. Reference libraries describe their
own versioned coverage; installed runtime observations are separate evidence.
Unset choices remain unknown. Available personas do not grant tools, permission,
or independent review. Resolve conflicting project configuration before changing a pin.

Resource structure is governed by root `RES_TYPE.md` and per-type definitions in `resource_templates/`. Prepared resources use `res_lib/`; selected tools use `tools_lib/`. Record loose-source and import destinations in the relevant type definition and reference them here when useful; avoid a second editable mapping. These library locations do not select formats, engines or game budgets.

Testing support: `$test-setup`, `$test-helpers` and `$qa-plan` use the selected choices above. See `.codex/docs/code-root-resolution.md` and `.codex/docs/testing-engine-reference.md`. The studio skeleton and reference library do not choose a project root, installed runner or CI route.
