# Common Ui

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Documentation scope

Unreal 5.8 Common UI documentation. Confirm installed versions and compatibility separately.

## Integration

Common UI supplies UI input routing, shared actions, controller data and styled widgets. Its quickstart requires CommonGameViewportClient or a subclass for routing. Configure input/controller assets for the actual supported devices.

## Example assessment

Trace opening a modal, click/back handling, focus and return to gameplay. Verify context priority and device changes. Do not assume enabling the plugin completes routing or makes every UMG widget accessible.

## Evidence and use

- [unreal-common-ui official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/common-ui-quickstart-guide-for-unreal-engine?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
