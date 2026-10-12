# Unreal physics

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Capabilities and choices

Chaos provides rigid-body simulation, constraints and additional systems. Networked physics has separate replication modes and requires an authority/correction design. Select only the physics features needed; experimental or platform-specific extensions need explicit evidence.

## Application and verification

Record body/collision/constraint rules, simulation timing and interactions with animation or networking. Test a representative stress/contact case and inspect actual simulation/debug evidence before setting performance expectations.

## Evidence and use

- [unreal-physics official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-in-unreal-engine?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
