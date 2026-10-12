# Unity physics

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Capabilities and choices

Unity’s built-in object-oriented 3D physics integrates PhysX. Keep its Rigidbody/collider/joint model separate from 2D and DOTS physics APIs. Match movement and simulation timing to the chosen system; avoid transplanting examples between systems.

## Application and verification

Define collision layers, body type, movement owner and response. Check fast motion, contacts, triggers and joints relevant to the mechanic; measure actual target performance before proposing fixed budgets.

## Evidence and use

- [unity-physics official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/PhysicsOverview.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
