# Engine reference library

This library supports Godot, Unity and Unreal. Official release pages and the
linked topic documentation were checked on 2026-10-08. Each VERSION.md identifies
the exact library baseline and its sources. Live project selections belong to
`docs/technical-preferences.md`; installed versions require separate evidence.

| Family | Library baseline | Version and topic entry points |
|---|---|---|
| Godot | 4.7.2 stable | [Version](godot/VERSION.md), [practice](godot/current-best-practices.md) |
| Unity | 6000.6.4f1 / 6.6 Update | [Version](unity/VERSION.md), [packages](unity/PLUGINS.md) |
| Unreal | 5.8.3 stable | [Version](unreal/VERSION.md), [plugins](unreal/PLUGINS.md) |

Each family includes animation, audio, input, navigation, networking, physics,
rendering and UI modules, plus breaking-change and deprecation guidance. Package
guides identify their documentation version separately. Availability is not a
project selection or evidence that a plugin is installed.

For a technical check, identify the exact claim and selected version, consult its
official source, and distinguish documentation evidence from runtime evidence.
Recheck mismatched versions and evolving APIs. No model-cutoff risk category or
old verification date establishes correctness. Missing evidence leaves the
affected check unassessed. Refresh records only what was actually examined.

The references are selective working guidance, not exhaustive engine manuals or
compatibility certification. `$setup-engine refresh` updates documentation;
`upgrade` prepares a scoped migration assessment and requires actual execution
before any migration-success claim.
