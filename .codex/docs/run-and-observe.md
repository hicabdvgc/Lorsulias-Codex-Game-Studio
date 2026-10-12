# Run and Observe

Adapted from Claude Code Game Studios. Use for actual runtime-visible work in `$dev-story`,
`$vertical-slice`, `$smoke-check` and team evaluation. Read code-root-resolution.md and the live
technical preferences first. Resolve selected game, build, startup state, executable and actual
launch/test commands. Skeleton folders do not establish the engine project.

Define the required observation against the criterion: scene/state, inputs, expected behavior,
platform, resource dependencies and appropriate capture or human method. Launch only within the
authorized scope, reach the relevant state and inspect actual results. A successful process start,
headless parse or screenshot cannot prove interaction, audio, feel or human usability. Use available
runtime/computer tools only; when absent, provide the precise manual protocol and retain NOT ASSESSED.
Record exact command, build/revision, environment, observed state, inputs, result and limitations.

Use the selected project's verified launch/capture route. Do not assume fixed window size, frame
count, timeout, bootstrap save path, automatic screenshots or a universal MSYS flag. Preserve existing
project state and capture only intended evidence; terminate only the process started for the check
when appropriate. Handle early exits/hangs as observed results. Save requested evidence to the actual
QA/report location and verify it before handoff. Report OBSERVED, NOT VERIFIED or justified N/A per
criterion. Actual human sign-offs remain distinct.

## Optional Godot GDScript observer

`.codex/scripts/godot-parse-check.gd` loads/reloads explicit res://...gd paths under the selected
project. Invoke the selected Godot executable with `--headless --path <actual-project-root>
--script <absolute-studio-helper-path> -- res://<actual-script>.gd`; quote paths for the shell in use.
The helper may be outside a nested game root. Verify support with that executable's `--help` and
version. No engine is installed by this workflow. Godot C# compilation and other engines use their
selected build/check routes; this helper does not cover them.

Input is validated before loads. It reports load/reload errors and can_instantiate separately.
A non-instantiable/abstract script is not automatically a parse failure. Exit 0 means the supplied
load/reload operations succeeded, 1 means a failure, and 2 means invalid input. Inspect engine stderr
as well; this result does not prove a game launch or every dependency/startup callback. Project
imports/class caches, plugins and runtime setup may affect loading. Do not assert autoload availability
from callback timing. An explicitly needed import is a separate authorized operation and can change
caches; launching/reloading can execute project code. Use isolated copies when those effects matter.

Official API/command references reviewed 2026-10-08 (Godot 4 stable documentation lane; actual selected
and installed versions still require verification): [Script reload and can_instantiate](https://docs.godotengine.org/en/stable/classes/class_script.html),
[ResourceLoader load/cache modes](https://docs.godotengine.org/en/stable/classes/class_resourceloader.html),
[OS user arguments](https://docs.godotengine.org/en/stable/classes/class_os.html),
and [command-line options](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html).
No Godot runtime execution is claimed by this documentation check. Unity/Unreal selected runner
instructions remain in testing-engine-reference.md; use official selected-version launch documentation
before retaining a new command example. No generic cross-engine launch adapter is supplied.
