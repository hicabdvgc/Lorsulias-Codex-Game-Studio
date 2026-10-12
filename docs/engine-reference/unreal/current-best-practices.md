# Unreal project practice

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Apply to the selected project

Define actor/component/UObject lifetimes and C++/Blueprint boundaries from requirements. Keep gameplay authority and presentation separate where the design needs it. Verify modules, plugins and cooked assets against selected targets. Use measured profiles to choose optimizations; no fixed frame budget or mandatory GAS/Common UI adoption follows from these guides. Engine-editor inspection is required before detailed claims about binary assets.

## Evidence-driven workflow

Read the system GDD and FRAMEWORK, identify interfaces and resource needs, compare viable options, and document only selected choices. Record official API evidence and separately execute builds/experiments when available. Missing tools leave the related runtime check pending. Consult the relevant topic module rather than imposing an engine-wide architecture.

## Evidence and use

- [unreal-networking official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.8)
- [unreal-ui official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-user-interfaces-with-umg-and-slate-in-unreal-engine?application_version=5.8)
- [unreal-gameplay-ability-system official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
