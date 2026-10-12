# Unity animation

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Capabilities and choices

Animation clips describe property changes; Animator Controllers organize states, transitions and blending. Separate animation presentation from authoritative gameplay rules and decide how root motion or animation events participate in the system.

## Application and verification

For an idle/move/action controller, identify parameter producers and transition/interrupt rules. Check restart, exit, blending and off-screen behavior with imported clips. A well-formed controller does not establish perceived responsiveness.

## Evidence and use

- [unity-animation official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/AnimationOverview.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
