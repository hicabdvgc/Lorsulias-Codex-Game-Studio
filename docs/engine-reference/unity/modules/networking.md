# Unity networking

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Capabilities and choices

Unity’s Multiplayer Center assists package/service selection. Choose networking from game requirements and the existing architecture, then identify the exact transport/netcode/service versions. GameObject and ECS networking choices need their own evidence; no networking stack is preselected here.

## Application and verification

Specify authority, synchronized state, commands, late join, disconnection and hosting requirements. Measure latency/bandwidth under representative conditions. Package recommendations and local simulation are insufficient evidence of production network behavior.

## Evidence and use

- [unity-networking official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/multiplayer.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
