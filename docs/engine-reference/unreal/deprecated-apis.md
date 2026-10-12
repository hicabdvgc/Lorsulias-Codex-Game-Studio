# Unreal deprecation checks

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Verified scope

The 5.8 release notes identify removal of the NNERuntimeORTDml NPU interface. Do not infer that Sound Cues, Blueprint gameplay or conventional replication are obsolete simply because newer systems exist. Identify the exact API, engine/plugin version, compiler warning or official deprecation entry before proposing a replacement.

## Applying a replacement

Identify callers and serialized data, explain the semantic difference, change only affected uses, and verify behavior/builds. When evidence is unavailable, preserve the uncertainty and block the affected compatibility conclusion.

## Evidence and use

- [unreal-upgrade official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
