# Godot breaking changes

Library baseline: **4.7.2**. Documentation checked **2026-10-08**.

## Changes to inspect when upgrading 4.6 to 4.7

- Animation blend spaces replace the boolean sync setting with sync_mode. Re-evaluate transition synchronization.
- Mouse/keyboard device constants replace the assumption that device ID 0 identifies them.
- Packed-array element writes no longer invoke the enclosing property setter. Review change-notification logic.
- Jolt WorldBoundaryShape3D plane distance changes sign convention; inspect existing boundaries.
- The macOS minimum becomes 11. Check actual export requirements.

These are selected changes, not a complete migration checklist. Compare all
intervening upgrade guides for the project's source version, plus patch notes.
Save the current project and verify relevant behavior before accepting migration.


## Evidence and use

- [godot-upgrade official documentation](https://docs.godotengine.org/en/4.7/tutorials/migrating/upgrading_to_godot_4.7.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
