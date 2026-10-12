# Godot physics

Library baseline: **4.7.2**. Documentation checked **2026-10-08**.

## Capabilities and choices

Select Area bodies for detection, static bodies for immovable collision, rigid bodies for simulated motion and character bodies for controlled movement. 2D and 3D APIs are related but distinct. Godot physics is not guaranteed deterministic; repeatable gameplay rules must not assume identical physics simulation.

## Application and verification

Record body/shape ownership, layers/masks, trigger versus collision behavior, timing and response. Check tunneling, resting contact and overlapping triggers applicable to the mechanic. Recheck Jolt/SoftBody and WorldBoundary behavior when moving from 4.6 to 4.7.

## Evidence and use

- [godot-physics official documentation](https://docs.godotengine.org/en/4.7/tutorials/physics/physics_introduction.html)
- [godot-upgrade official documentation](https://docs.godotengine.org/en/4.7/tutorials/migrating/upgrading_to_godot_4.7.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
