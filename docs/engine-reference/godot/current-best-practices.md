# Godot project practice

Library baseline: **4.7.2**. Documentation checked **2026-10-08**.

## Apply to the selected project

Choose scene/node boundaries from lifecycle and reuse. Define Resource ownership, signal connections and async cleanup. Check rendering/export choices before relying on an effect. Typed GDScript, C# and GDExtension serve different needs; select from project constraints, tooling and measured workload. Godot 4 C# web export remains unavailable in the checked 4.7 C# guide; .NET editor/SDK and other platform limitations need explicit verification.

## Evidence-driven workflow

Read the system GDD and FRAMEWORK, identify interfaces and resource needs, compare viable options, and document only selected choices. Record official API evidence and separately execute builds/experiments when available. Missing tools leave the related runtime check pending. Consult the relevant topic module rather than imposing an engine-wide architecture.

## Evidence and use

- [godot-csharp official documentation](https://docs.godotengine.org/en/4.7/tutorials/scripting/c_sharp/c_sharp_basics.html)
- [godot-gdscript official documentation](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_basics.html)
- [godot-gdextension official documentation](https://docs.godotengine.org/en/4.7/engine_details/engine_api/gdextension/index.html)
- [godot-shader official documentation](https://docs.godotengine.org/en/4.7/tutorials/shaders/shader_reference/shading_language.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
