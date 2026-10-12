# Unity rendering

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Capabilities and choices

Compare URP, HDRP, custom SRP and existing Built-in content using required features and hardware. The 6.6 manual marks Built-in deprecated, with maintenance through the Unity 6.7 LTS lifecycle; deprecation does not mean immediate removal. Dynamic batching is obsolete in 6.6.

## Application and verification

Check material/shader compatibility and representative scenes in the chosen pipeline. Use supported profiling and draw-call strategies rather than copying obsolete dynamic-batching advice. Recheck baked-light appearance if changing the lightmapper.

## Evidence and use

- [unity-rendering official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/render-pipelines.html)
- [unity-upgrade official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/UpgradeGuideUnity66.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
