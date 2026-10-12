# Godot deprecation checks

Library baseline: **4.7.2**. Documentation checked **2026-10-08**.

## Verified scope

The 4.7 migration guide replaces blend-space sync with sync_mode. Update the actual blend-space configuration and check transitions. Input device constants are a changed assumption, not a reason to rewrite all input handling. Use the selected class reference before calling any replacement API; no complete deprecation inventory is claimed here.

## Applying a replacement

Identify callers and serialized data, explain the semantic difference, change only affected uses, and verify behavior/builds. When evidence is unavailable, preserve the uncertainty and block the affected compatibility conclusion.

## Evidence and use

- [godot-upgrade official documentation](https://docs.godotengine.org/en/4.7/tutorials/migrating/upgrading_to_godot_4.7.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
