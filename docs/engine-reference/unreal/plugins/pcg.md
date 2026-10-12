# Pcg

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Documentation scope

Unreal 5.8 PCG documentation. Confirm installed versions and compatibility separately.

## Integration

PCG uses graphs and point/attribute data for procedural content generation. The framework plugin must be enabled; sampling static meshes may need Geometry Script Interop. Individual PCG features can have separate maturity/platform constraints.

## Example assessment

Record seed and input ownership, bounds, generation timing, cleanup and generated-asset responsibilities. Re-run a representative graph after input changes and inspect repeatability and resource costs. Documentation of PCG does not select it for this game.

## Evidence and use

- [unreal-pcg official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
