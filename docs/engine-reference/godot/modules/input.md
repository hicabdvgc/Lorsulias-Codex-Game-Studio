# Godot input

Library baseline: **4.7.2**. Documentation checked **2026-10-08**.

## Capabilities and choices

Input events suit discrete actions; polling the Input singleton suits ongoing state. Define named actions in InputMap and decide which layer consumes them. In 4.7 mouse/keyboard device identity uses InputEvent.DEVICE_ID_MOUSE and DEVICE_ID_KEYBOARD; assuming device 0 means keyboard is invalid.

## Application and verification

With an InputMap action named `confirm`, a discrete event check is:

```gdscript
func _unhandled_input(event: InputEvent) -> void:
    if event.is_action_pressed("confirm"):
        get_viewport().set_input_as_handled()
        # Invoke the project's confirmation command here.
```

Check remapping, key repeat, focus and UI/gameplay consumption. The placeholder comment deliberately does not invent a project function.

## Evidence and use

- [godot-input official documentation](https://docs.godotengine.org/en/4.7/tutorials/inputs/input_examples.html)
- [godot-upgrade official documentation](https://docs.godotengine.org/en/4.7/tutorials/migrating/upgrading_to_godot_4.7.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
