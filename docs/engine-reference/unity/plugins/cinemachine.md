# Cinemachine

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Documentation scope

Cinemachine 3.1.7 documentation; Unity 6.6 core-package behavior. Confirm installed versions and compatibility separately.

## Integration

The 6.6 editor supplies Cinemachine 3 as a core package. Upgrading from 2.x changes data and APIs, including the namespace to Unity.Cinemachine. Preserve references during the official data upgrade and inspect broken references afterward.

## Example assessment

Replace obsolete namespace examples with `using Unity.Cinemachine;`. Use the documented component replacements rather than blind textual class substitution. Validate blends, priorities, tracking and custom extensions in representative scenes. Verify migration against the actual project and installed package.

## Evidence and use

- [unity-cinemachine official documentation](https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachineUpgradeFrom2.html)
- [unity-upgrade official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/UpgradeGuideUnity66.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
