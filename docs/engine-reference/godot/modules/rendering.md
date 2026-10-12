# Godot rendering

Library baseline: **4.7.2**. Documentation checked **2026-10-08**.

## Capabilities and choices

Godot has Forward+, Mobile and Compatibility rendering methods with different feature/hardware support. Forward+/Mobile use RenderingDevice with supported modern graphics drivers; Compatibility uses OpenGL. Pick from platform and effect requirements, then verify the renderer feature table.

## Application and verification

List the required effects and targets before selecting a method. Compare representative lighting/material scenes on target hardware. In 4.7 LinearToSRGB visual shaders no longer clamp on Forward+/Mobile; add intentional clamping only when the effect requires it.

## Evidence and use

- [godot-rendering official documentation](https://docs.godotengine.org/en/4.7/tutorials/rendering/renderers.html)
- [godot-upgrade official documentation](https://docs.godotengine.org/en/4.7/tutorials/migrating/upgrading_to_godot_4.7.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
