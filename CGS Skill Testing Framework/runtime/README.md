# Studio Runtime Checks

These checks exercise the installed studio's metadata and helpers using isolated
fixtures. They operate from this project alone. Skills and persona instruction
exercises use the specifications in the parent testing framework.

## Requirements and commands

Follow the project [installation guide](../../INSTALL.md) to create `.venv`
and install [requirements.txt](requirements.txt). Use that environment's Python
for the commands below. Structural scanning excludes `.git`, `.venv`, caches,
and generated framework reports.

Use existing Python 3.11+ with PyYAML, Bash, and Git. Windows launcher cases
also use PowerShell and Git for Windows. Invoke from the studio root:

```text
python "CGS Skill Testing Framework/runtime/check_structure.py" --bash "<Bash executable>"
python "CGS Skill Testing Framework/runtime/run_runtime.py" --bash "<Bash executable>"
python "CGS Skill Testing Framework/runtime/run_runtime.py" --bash "<Bash executable>" --only continuity continuity_extra
python "CGS Skill Testing Framework/runtime/test_project_coherence.py" --bash "<Bash executable>"
python "CGS Skill Testing Framework/runtime/test_runtime_regressions.py"
```

`check_structure.py` checks installed identities, specification paths, metadata,
syntax, workflow support, and literal links. Missing links are listed for review;
an explicitly identified future game output is distinct from a broken installed link.
Shell syntax checks require `--bash`.

`run_runtime.py` runs foundation, design_helpers, assets, story_status,
git_observers, git_extra, continuity, continuity_extra, and worktree checks.
`--only` selects named checks; `git_extra` also runs `git_observers` to prepare
their shared disposable repository. Selection success applies only to that run's
checks. Prior reports do not contribute to the result.

Reports live under the ignored `CGS Skill Testing Framework/results/` directory.
Runtime suites receive unique run directories; structure, coherence, and regression
reports describe their latest invocation. The latter two accept `--output` for
an explicitly chosen report path. Runtime fixture directories are temporary and
their locations are recorded for diagnosis.

## Interpretation

Static inspection establishes structural observations. Executable fixtures
establish the tested helper behavior. Native client dispatch, engines, services,
human evaluation, and game readiness require their own evidence. Missing
dependencies remain unavailable checks; do not install or invent them to claim a pass.
