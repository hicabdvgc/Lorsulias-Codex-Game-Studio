# Unreal networking

Library baseline: **5.8.3**. Documentation checked **2026-10-08**.

## Capabilities and choices

Replication synchronizes data and calls between clients and servers. Unreal documentation covers default networking, Iris and Replication Graph; selection depends on the project and verified support. Separate persistent replicated state from transient commands/events.

## Application and verification

Describe owner/authority, property updates, RPC direction and late-join behavior for a mechanic. Exercise latency/loss and reconnect where relevant. A single local play session cannot verify these conditions.

## Evidence and use

- [unreal-networking official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.8)

The cited documentation supports the described capability, API or change. Project
compatibility and performance require the selected editor, package versions and
target platform. Examples are illustrative and have not been run in an engine.
Read `docs/technical-preferences.md` for project choices; this library does not
select, install or migrate them. Record unavailable evidence as NOT ASSESSED.
