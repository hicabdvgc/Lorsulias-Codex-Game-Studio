# Godot navigation

Library baseline: **4.7.2**. Documentation checked **2026-10-08**.

## Capabilities and choices

NavigationAgent2D/3D assists path queries, following and avoidance; it does not replace the actor movement implementation. Set target_position using global coordinates. Navigation layers and path query settings affect routes; avoidance and reachability are separate concerns.

## Application and verification

Describe an agent moving through a door: path request, next waypoint, actor movement, arrival/unreachable handling and avoidance response. Check map synchronization, blocked destinations and narrow passages with the actual actor shape and movement rules.

## Evidence and use

- [godot-navigation official documentation](https://docs.godotengine.org/en/4.7/tutorials/navigation/navigation_using_navigationagents.html)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
