# Unreal navigation

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Capabilities and choices

Navigation meshes derive from level collision and support cost-based paths. Generation modes include Static, Dynamic and Dynamic Modifiers Only. RVO and Detour Crowd are available avoidance approaches; pick an approach from actual agent and world needs.

## Application and verification

Specify supported agent dimensions, links, area costs and runtime geometry changes. Test a blocked route, link traversal and crowd passage. Distinguish a reachable path from successful actor movement and avoidance.

## Evidence and use

- [unreal-navigation official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/navigation-system-in-unreal-engine?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
