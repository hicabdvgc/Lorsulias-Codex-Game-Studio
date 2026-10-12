# Godot animation

Library baseline: **4.7.2**. Documentation checked **2026-10-08**.

## Capabilities and choices

Use AnimationPlayer to author/import animations and AnimationTree for blending and transitions. Keep gameplay state ownership explicit when animation events affect rules. Blend spaces in 4.7 use sync_mode rather than the old boolean sync property; recheck transitions after an upgrade.

## Application and verification

For a character with idle/run clips, specify which system supplies speed, the blend parameter, interruption rules and reset behavior. Check entering/leaving each state, looping and pause. Confirm that visual transitions agree with the GDD before treating them as correct.

## Evidence and use

- [godot-animation official documentation](https://docs.godotengine.org/en/4.7/tutorials/animation/animation_tree.html)
- [godot-upgrade official documentation](https://docs.godotengine.org/en/4.7/tutorials/migrating/upgrading_to_godot_4.7.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
