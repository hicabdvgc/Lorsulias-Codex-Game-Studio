# Unreal breaking changes

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Upgrade assessment for 5.8

Read release notes and the 5.8.3 hotfix against the actual source version and
enabled modules. For example, 5.8 removes the NPU execution interface from
NNERuntimeORTDml; affected integrations need a supported alternative. New Windows
ARM64 game-target support is Experimental and does not imply an ARM64 Editor.

Keep Gameplay Cameras experimental status visible. Evaluate Blueprint assets,
C++/module compile changes, plugins, cooking and representative target behavior
before concluding migration succeeded. Record errors separately from functional
findings and retain a recoverable pre-upgrade project state.


## Evidence and use

- [unreal-upgrade official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
