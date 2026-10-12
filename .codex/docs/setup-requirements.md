# Setup Requirements

Follow [INSTALL.md](../../INSTALL.md) to set up the whole project and its local
Python environment, activate it in Codex, and check discovery before testing.

Open the studio as the intended project root. Opening a parent workspace does
not establish that the client loaded this directory's skills, personas, or
configuration. Project hooks need a trusted/enabled project in a supporting
client; inspect actual loading and event dispatch in that client.

## Runtime requirements

| Capability | Requirement |
|---|---|
| Bash hooks and shell observers | Bash; Windows launchers use Git for Windows and its `bin/bash.exe`. |
| JSON event parsing and agent logs | Working Python 3 or jq. |
| Command-pattern and patch-path inspection | Working Python 3. |
| Git observers and worktree operations | Working Python and Git; Git operations require an actual repository. |
| Lifecycle, session, artifact, and coherence Python helpers | Python 3.9 or newer. |
| Artifact observation and SessionStart artifact discovery | PyYAML available to the selected Python runtime. |
| Optional Godot observer | An already selected compatible Godot runtime and actual project. |
| Studio runtime test suite | Python 3.11+, PyYAML, Bash, and Git; Windows launcher cases also use PowerShell. |
| Optional skill-creator validator | An available validator and its own dependencies. |

Choose source/test roots with the actual engine. The studio does not install
engines, languages, services, or testing dependencies automatically. See
[runtime checks](<../../CGS Skill Testing Framework/runtime/README.md>) for the
separate studio-maintenance commands and their evidence boundaries.

## Python selection

Hooks first try an executable supplied through `LORSULIA_HOOK_PYTHON`, then
the studio's `.venv/Scripts/python.exe` on Windows or `.venv/bin/python` on
macOS/Linux, then working `python3`, `python`, and `py -3`. They test JSON parsing before selecting
a command. An application alias or stale launcher is insufficient. Keep any
machine-specific executable path in the launching environment.

The `native_path` helper converts script/root paths for native Windows Python
without changing personal shell configuration. A missing parser or runtime
leaves the affected observation unassessed.

## Verify the selected setup

Check actual shell/runtime versions and supported event schemas. Test handlers
with sample JSON and inspect their output and exit status. Use
`CGS_HOOK_DRY_RUN=1` for log-free inspection or isolated fixtures for log writes.
Direct script execution establishes handler behavior; confirm native dispatch
with an actual client event before claiming integration.

Read [artifact observation](artifact-observation.md),
[run and observe](run-and-observe.md), [continuity](context-management.md), and
[lifecycle contracts](hooks-reference/lifecycle-contract.md) when those
capabilities are used.
