# Unity project practice

Library baseline: **6000.6.4f1 (Unity 6.6 Update)**. Documentation checked **2026-10-08**.

## Apply to the selected project

Inspect ProjectVersion and package locks before recommending APIs. Separate serialized configuration, runtime state and asset ownership. Match input, UI and rendering choices to requirements. Profile allocations and costly update paths before adopting pooling or DOTS. Cinemachine 3 is a core package in 6.6; its documentation snapshot is not a substitute for the editor package manifest. Preserve working uGUI content when its features satisfy the project.

## Evidence-driven workflow

Read the system GDD and FRAMEWORK, identify interfaces and resource needs, compare viable options, and document only selected choices. Record official API evidence and separately execute builds/experiments when available. Missing tools leave the related runtime check pending. Consult the relevant topic module rather than imposing an engine-wide architecture.

## Evidence and use

- [unity-upgrade official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/UpgradeGuideUnity66.html)
- [unity-ui official documentation](https://docs.unity3d.com/6000.6/Documentation/Manual/UIToolkits.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
