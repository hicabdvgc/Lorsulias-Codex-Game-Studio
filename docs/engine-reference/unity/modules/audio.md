# Unity audio

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Capabilities and choices

AudioSource emits sound and AudioListener receives it; spatial settings and filters affect playback. Mixer routing and source ownership should follow the intended interaction. Scene geometry alone does not automatically produce physically accurate echoes.

## Application and verification

Trace one looping ambience and one transient feedback sound through spawn, pause, scene transition and cleanup. Check settings/mix, spatial behavior and project-required alternatives to audio. Use actual capture/listening evidence for playback claims.

## Evidence and use

- [unity-audio official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/AudioOverview.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
