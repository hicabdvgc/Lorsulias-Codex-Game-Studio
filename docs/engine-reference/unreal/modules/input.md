# Unreal input

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Capabilities and choices

Enhanced Input uses Input Actions, Mapping Contexts, Modifiers and Triggers. Contexts can be added/removed at runtime, and their priority matters when actions overlap. Confirm the plugin and player/input ownership in the actual project.

## Application and verification

Model a gameplay-to-menu transition: add/remove the appropriate contexts, define priority and restore focus. Check hold/tap triggers, remapping and controller changes. Do not assume the template input setup satisfies the game’s commitments.

## Evidence and use

- [unreal-input official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
