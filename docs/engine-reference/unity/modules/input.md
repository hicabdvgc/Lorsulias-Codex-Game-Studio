# Unity input

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Capabilities and choices

Unity 6.6 supports the Input System package and the legacy Input Manager. Official documentation marks the latter deprecated. Match the chosen package version, configured input handling and UI integration; existing legacy usage requires a scoped migration assessment.

## Application and verification

Identify actions, device bindings, control schemes, focus and callback lifetime. Exercise rebinding, device change and UI/gameplay conflicts. Do not convert projects merely because new-input guidance exists.

## Evidence and use

- [unity-input official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/Input.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
