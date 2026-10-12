# Install Lorsulia's Codex Game Studio

Install the complete studio folder as a local Codex project. This follows the
ChatGPT Game Studios template's folder-based setup. The folder contains the
workflow, project scaffold, skills, personas, hooks, templates, and test framework.

## 1. Choose the project folder

Use the existing studio folder, or copy its complete contents into an empty
folder for another game. Include hidden `.agents`, `.codex`, and `.github`
directories. When copying an existing installation, omit `.git`, `.venv`, caches,
and generated test reports; create the new project's environment separately.

For public distribution, use a clean copy of the reusable project files. Keep
local Git history, virtual environments, session logs/checkpoints, integration
journals, generated test results, credentials and personal editor overrides out
of that copy. Retain the testing framework's catalog, specifications, templates
and reusable checks because the studio's maintenance skills depend on them.
The `.gitkeep` files preserve empty scaffold directories in a Git checkout.

The project root is the directory containing this file and `AGENTS.md`.
Open that directory directly in Codex. Opening a parent directory does not load
skills from all of its child projects.

## 2. Prepare the runtimes

Use a current Codex desktop app, CLI, or IDE extension that supports project
skills, custom agents, and hooks. For the complete maintenance suite, install
Python 3.11 or newer, Git, and Bash. Windows uses Git for Windows and PowerShell.
See [setup requirements](.codex/docs/setup-requirements.md) for capability-specific
dependencies. Engine installation follows the game's selected technology later.

From the studio root, create an isolated Python environment and install the
declared dependency:

### Windows PowerShell

```powershell
py -3 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r 'CGS Skill Testing Framework/runtime/requirements.txt'
& .\.venv\Scripts\python.exe -c 'import sys, yaml; print(sys.version); print(yaml.__version__)'
git --version
$studioGit = (Get-Command git.exe -ErrorAction Stop).Source
$studioBash = Join-Path (Split-Path (Split-Path $studioGit -Parent) -Parent) 'bin/bash.exe'
& $studioBash --version
```

If `py -3` points to a missing installation, substitute an existing Python 3.11+
executable in the first command:

```powershell
& 'C:\path\to\python.exe' -m venv .venv
```

Use Git for Windows' `bin/bash.exe`; Windows' `System32/bash.exe` may invoke WSL.
The hook launcher derives Bash from `git.exe`, so that command must resolve to
the Git for Windows installation in the environment running Codex.

### macOS or Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r 'CGS Skill Testing Framework/runtime/requirements.txt'
.venv/bin/python -c 'import sys, yaml; print(sys.version); print(yaml.__version__)'
git --version
bash --version
```

Some Python distributions supply `venv` separately. Install the distribution's
venv support if creation reports it missing.

Hooks automatically try the project's `.venv` before global Python launchers.
An explicit `LORSULIA_HOOK_PYTHON` still takes priority. Activation scripts and
global PATH changes are unnecessary for these hooks. Use the explicit `.venv`
Python path for test commands. Recreate `.venv` after moving the project or
removing/upgrading the Python installation used to create it.

## 3. Enable Git when starting from a folder

If this folder has no Git repository, run:

```text
git init
```

This enables a repository boundary and local Git inspection. Worktree and branch
integration require an initial commit and actual branch history; create that
baseline when ready to begin those tests. No remote is required for local use.

## 4. Open and activate the studio in Codex

In the Windows desktop app, use **Add new project** or **Ctrl+O**, then select
the studio root. Start subsequent studio chats from that project. Your existing
parent-workspace chat keeps its original working directory.

The CLI can open a local session at the same root:

```text
codex -C "<absolute path to the studio>"
```

`codex app "<absolute path to the studio>"` can request desktop opening when
that CLI recognizes the installed app. If it offers an installer despite an
already running app, use the app's folder picker instead of reinstalling it.

Review and trust the project through the client's normal project-trust flow.
Project configuration and hooks require an active trusted project layer.
Inspect `.codex/hooks.json` and its referenced scripts. In the CLI, `/hooks`
shows discovered hooks and lets you trust their current definitions. Use the
corresponding hook controls where available in your desktop client. Updated
definitions may require review again. Opening the folder alone does not prove
that hooks are enabled or dispatched.

The studio keeps model, reasoning, permissions, and concurrency choices inherited
from your effective Codex settings. Its project configuration enables hooks.

## 5. Verify discovery before skill testing

In a fresh chat opened at the studio root:

1. Confirm the working directory is this folder and the root `AGENTS.md` is loaded.
2. Look for project skills such as `$start`, `$help`, and `$skill-test` in the
   client's skill selector. The studio contains 76 skills; personal and plugin
   skills may appear alongside them.
3. Check that the project persona definitions under `.codex/agents/` are
   available to the client. There are 49 definitions. Their presence on disk
   and a successful parse do not establish a successful agent invocation.
4. Inspect the 11 registered project hook handlers across eight event groups, their source
   path, enabled/trust state, and any loading errors. Check actual event output
   when testing native integration.

   SessionStart calls the gap observer internally; it is not a second registered
   SessionStart handler.
5. Invoke `$help` or `$studio-status` for a first read-only orientation. Use
   `$start` when ready to begin the game workflow.

Codex discovers project skills from `.agents/skills` along the current directory's
repository ancestry, and custom agents from project `.codex/agents` files.
See the official [skill discovery documentation](https://learn.chatgpt.com/docs/build-skills),
[custom agent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents),
and [hook loading and trust documentation](https://learn.chatgpt.com/docs/hooks).
The Windows folder-opening controls are documented in the
[Windows app guide](https://learn.chatgpt.com/docs/windows/windows-app).

## 6. Run the installed checks

Windows PowerShell, from the studio root:

```powershell
$studioPython = Join-Path (Get-Location) '.venv/Scripts/python.exe'
$studioGit = (Get-Command git.exe -ErrorAction Stop).Source
$studioBash = Join-Path (Split-Path (Split-Path $studioGit -Parent) -Parent) 'bin/bash.exe'
& $studioPython 'CGS Skill Testing Framework/runtime/check_structure.py' --bash $studioBash
& $studioPython 'CGS Skill Testing Framework/runtime/run_runtime.py' --bash $studioBash
& $studioPython 'CGS Skill Testing Framework/runtime/test_project_coherence.py' --bash $studioBash
& $studioPython 'CGS Skill Testing Framework/runtime/test_runtime_regressions.py'
```

On macOS/Linux use `.venv/bin/python` and the path returned by `command -v bash`.
Reports go to the ignored `CGS Skill Testing Framework/results/` directory.
The [runtime README](<CGS Skill Testing Framework/runtime/README.md>) explains
partial runs and dependencies. The [testing framework](<CGS Skill Testing Framework/README.md>)
and `$skill-test` define skill/persona evaluation procedures.

Structural checks, executable helper fixtures, skill/persona exercises, and
native hook events provide different evidence. Record each result when it is
actually observed. Installation does not complete any game workflow gate.
