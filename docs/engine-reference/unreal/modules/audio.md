# Unreal audio

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Capabilities and choices

Unreal’s Audio Mixer supports Sound Cues, Sound Classes and Sound Mixes as well as newer audio features. MetaSounds is an option for procedural/sample-sensitive work; the presence of newer tooling does not establish that existing Sound Cues must be discarded.

## Application and verification

Compare a fixed cue with a procedural requirement, define routing/concurrency/ownership and test pause, transitions and settings. Separate source-supported features from measured latency and listener observations.

## Evidence and use

- [unreal-audio official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-in-unreal-engine-5?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
