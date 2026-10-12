# Unity deprecation checks

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Verified scope

The 6.6 guide marks dynamic batching obsolete and Progressive CPU Lightmapper deprecated. Removed legacy Rendering Debugger APIs require the documented replacement implementation. Built-in rendering is deprecated but remains supported through the stated LTS lifecycle; uGUI remains available. Deprecated, removed and discouraged are different states.

## Applying a replacement

Identify callers and serialized data, explain the semantic difference, change only affected uses, and verify behavior/builds. When evidence is unavailable, preserve the uncertainty and block the affected compatibility conclusion.

## Evidence and use

- [unity-upgrade official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/UpgradeGuideUnity66.html)
- [unity-rendering official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/render-pipelines.html)
- [unity-ui official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/UIToolkits.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
