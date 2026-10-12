# Testing runner references

Documentation checked: **2026-10-08**. These are reference lanes, independent of
the engine-library baseline, the game's selected version and installed packages.
Recheck the actual project's versions before generating or running code. No engine,
runner dependency, credential or production CI workflow is installed by this studio.

## Godot / GDScript / GdUnit4
The [GdUnit4 compatibility table](https://github.com/godot-gdunit-labs/gdUnit4/blob/master/README.md)
lists released **v6.2.0** for Godot 4.5 through 4.7.1. Verify the actual addon release
against the selected engine; Godot C# requires its own explicitly verified route.
The [command reference](https://godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/cmd/)
documents the addon’s runtest launcher and `res://addons/gdUnit4/bin/GdUnitCmdTool.gd`.
Use `-a` for selected suites and `-rd` for reports; inspect the actual generated
HTML/JUnit report. Documented exits are 0 (success), 100 (failures), 101 (warnings).
Latest documentation must be reconciled with the installed release's help/API.
Preserve quoted paths and use process-scoped runtime selection when needed.
The [maintainer's action guide](https://github.com/godot-gdunit-labs/gdunit4-action/blob/master/README.md)
documents the v1 action lane. Any selected CI must specify the actual Godot/addon
versions, paths, runner and reporting settings; the guide does not select CI.

## Unity / C# / Unity Test Framework
The official **com.unity.test-framework 1.4.6**
[command reference](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/reference-command-line.html)
documents `-runTests -batchmode -projectPath <project> -testResults <xml>` and
`-testPlatform EditMode` or `PlayMode`. Pass paths as individually quoted arguments.
Inspect NUnit-format results and discovered tests; exit status alone is insufficient.
Use [test assembly guidance](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/workflow-create-test-assembly.html)
with the project's real assemblies. The documented package version is not a claim
of compatibility with every Unity editor; inspect manifest/lock and package support.
[NUnit range assertions](https://docs.nunit.org/articles/nunit/writing-tests/constraints/RangeConstraint.html)
support inclusive `Assert.That(value, Is.InRange(min, max))`; verify the installed
NUnit version and operand types. The [GameCI v4 test-runner guide](https://game.ci/docs/github/test-runner/)
documents `game-ci/unity-test-runner@v4`, projectPath/testMode/artifactsPath and
license-dependent prerequisites. Selecting this route requires actual credentials,
runner/platform support and repository configuration; none is presumed here.

## Unreal / C++ / Automation Framework
The official **Unreal 5.8** [run-tests guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/run-automation-tests-in-unreal-engine)
documents Editor Tools > Test Automation and console selection via
`-ExecCmds="Automation RunTest MySet.MySubSet;Quit"`, with
`-ReportExportPath="<output path>"` for JSON/HTML reports. Supply the actual editor,
project and test prefix; verify completion in the report rather than assuming a
zero process exit means all tests ran. See the
[Automation Framework overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine).
Registration macros, module dependencies, world setup and CI invocation must be
verified for the selected installed engine and target before generating examples.
No generic headless adapter, hosted runner or CI credentials are supplied.

## Evidence boundary
Documentation review is static evidence. Runtime discovery, compilation, execution,
report parsing and CI execution are separate checks. Report unverified APIs and
unsupported engine/language/framework combinations; do not silently substitute.
Record selected versions, verification date, working directory, exact arguments,
tested revision, discovered tests, actual results and limitations with each run.
