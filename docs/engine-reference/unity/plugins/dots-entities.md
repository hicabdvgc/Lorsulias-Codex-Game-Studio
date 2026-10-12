# Dots Entities

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Documentation scope

Entities 1.4.8 documentation. Confirm installed versions and compatibility separately.

## Integration

Entities implements ECS and is often combined with Entities Graphics, Unity Physics or Netcode for Entities. Those are separate package choices. Baking converts authoring data; queries/system ordering and job dependencies determine runtime behavior.

## Example assessment

For many moving entities, specify component data, update order, structural changes and command-buffer boundaries. Compare performance and memory against the existing implementation; verify native-container lifetime and companion package compatibility before adopting ECS.

## Evidence and use

- [unity-dots-entities official documentation](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/index.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
