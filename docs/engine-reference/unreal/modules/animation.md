# Unreal animation

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Capabilities and choices

Skeletal Meshes and animation assets underpin character animation. Animation Blueprints control blending and behavior. Keep animation state inputs, gameplay ownership and event timing explicit; selected assets and skeleton compatibility determine actual integration work.

## Application and verification

Trace locomotion and an interrupted action through animation state and gameplay state. Check imported skeletons, transitions and any root-motion assumptions. Inspect runtime results before declaring responsiveness or performance adequate.

## Evidence and use

- [unreal-animation official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
