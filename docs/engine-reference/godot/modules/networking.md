# Godot networking

Library baseline: **4.7.2**. Documentation checked **2026-10-08**.

## Capabilities and choices

Godot provides high-level multiplayer through SceneTree/MultiplayerAPI and lower-level transports. The high-level API includes RPCs and peer authority concepts. Choose transport and authority from platform and game requirements; do not assume desktop networking availability on browser exports.

## Application and verification

Define ownership and validation of a movement or inventory command, the state replicated, peer identity and disconnect behavior. Exercise host/client start, late join and adverse delivery conditions in a real network test before a multiplayer pass.

## Evidence and use

- [godot-networking official documentation](https://docs.godotengine.org/en/4.7/tutorials/networking/high_level_multiplayer.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
