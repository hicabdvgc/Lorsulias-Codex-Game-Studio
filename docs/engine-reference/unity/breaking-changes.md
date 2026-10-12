# Unity breaking changes

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Changes to inspect when upgrading 6.5 to 6.6

- Cinemachine 3 becomes a core package. Existing dependencies use the editor's version; Cinemachine 2 content/API needs migration checks.
- Dynamic batching is obsolete. Reassess optimization choices using actual profiles.
- Legacy Rendering Debugger DebugState/DebugUIDrawer APIs become compile errors. The upgrade guide describes serialized display settings and widget Create behavior.
- Progressive CPU Lightmapper is deprecated; a backend change needs visual comparison.
- Serialized YAML formatting can change. Review upgrade-generated asset diffs separately from intended edits.

Use the complete official upgrade guide for affected platforms/packages and all
intervening versions. Documentation refresh alone changes no game or package lock.


## Evidence and use

- [unity-upgrade official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/UpgradeGuideUnity66.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
