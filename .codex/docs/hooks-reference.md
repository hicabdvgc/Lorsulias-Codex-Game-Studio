# Installed Hooks

The registry `.codex/hooks.json` contains eleven handlers:

| Event | Matcher | Handler | Observable effect |
|---|---|---|---|
| PreToolUse | `^Bash$` | validate-command-safety.sh | Inspects command text for retained prohibited patterns; exit 2 on a match |
| PreToolUse | `^Bash$` | validate-commit.sh | Checks staged resource JSON and observes selected staged content |
| PreToolUse | `^Bash$` | validate-push.sh | Observes literal push context; does not run tests |
| PostToolUse | `^apply_patch$` | validate-skill-change.sh | Returns a skill-test reminder for changed skill-package paths |
| PostToolUse | `^apply_patch$` | validate-assets.sh | Observes JSON syntax in res_lib/ and assets/data/; reports findings without undoing edits |
| SubagentStart | Any | log-agent.sh | Appends agent name/ID and a UTC start event |
| SubagentStop | Any | log-agent-stop.sh | Appends a stop event; does not establish task success |

| SessionStart | startup/resume/clear/compact | session-start.sh | Supplies bounded recovery; startup/resume/clear also call detect-gaps.sh |
| Stop | Any | session-stop.sh | Records turn-stop event, not task completion/session shutdown |
| PreCompact | auto/manual | pre-compact.sh | Records bounded checkpoint and checkout observations |
| PostCompact | auto/manual | post-compact.sh | Reports recovery availability; SessionStart compact supplies context |

`hook-lib.sh` is shared support, not a registered handler. detect-gaps.sh remains an explicit observer
and is called inside SessionStart, without duplicate registration. Rotation remains explicit only.
Lifecycle scripts require working Python 3.9+; SessionStart discovery also requires the existing
artifact observer's PyYAML dependency. Parser/runtime failures are NOT ASSESSED. Event audit JSON
files are local and ignored. Native loading/dispatch remains a separate verification target.
See context-management.md and hooks-reference/lifecycle-contract.md.

Launchers search upward from the session working directory for the studio helper.
They work from the studio root or its subdirectories without requiring Git metadata.
The helper anchors output paths to its own studio root. Windows uses PowerShell
to locate Git for Windows and its bin/bash.exe. Shell commands quote the discovered
paths; no user-specific absolute path is stored in the shared registry.

## Prerequisites and limits

See [setup-requirements.md](setup-requirements.md). JSON input needs working Python
or jq. Command-pattern and patch-path inspection require Python. An unavailable
parser or invalid payload is reported as NOT ASSESSED; it never establishes a
successful check. These advisory gaps do not change the active permission policy.

The command checker retains source checks for destructive Git/deletion patterns,
sudo, chmod 777, and simple .env shell reads/redirections. It is supplemental:
arbitrary scripting, aliasing, command construction, and tools outside the matcher
are not fully covered. No filesystem deny profile is installed by this project.
Hook processing never executes the command text it inspects.

Set CGS_HOOK_DRY_RUN=1 to suppress audit-log writes during inspection. Logs are
local and gitignored; a start/stop pair is lifecycle evidence only.

Project hook loading and trust follow the active client; a file or direct script
test does not prove live event dispatch. Consult [official hooks documentation](https://learn.chatgpt.com/docs/hooks)
and [input/output contracts](hooks-reference/hook-input-schemas.md).

## Explicit design observation helpers

`.codex/scripts/gdd-structure-check.sh <system-GDD> [...]` requires callers to
supply the actual GDD scope. It prints JSON-quoted paths and PRESENT/ABSENT heading
labels (including aliases); it does not infer content completeness or approval.

`.codex/scripts/adr-dep-graph.sh [ADR-directory]` defaults to `docs/architecture`.
It scans `adr-NNNN-title.md` records, reports identities, status, declared edges,
missing/malformed dependency sections, filename/heading identity mismatches, duplicate identities, missing/unaccepted
targets, self-dependencies and cycle members. Explicit Depends On: None differs
from an absent declaration. Read full records before judging acceptance, and
scope blockers to the target's dependency closure.

Both scripts share `.codex/hooks/hook-lib.sh` only for root/runtime resolution.
They require Bash and working Python (`LORSULIA_HOOK_PYTHON` can identify it for
the process), work outside Git and from nested directories, and handle Windows
spaces/apostrophes. Relative paths are studio-relative; absolute project-local
Windows paths are supported. Exit 0 means observations completed, including
findings; exit 2 means invocation/read/runtime failure, possibly a partial scan.
Neither script writes files or logs, accepts hook JSON, or is registered as a
lifecycle hook. A failed scan is unavailable evidence, never a clean result.

## Explicit story-status observer

`.codex/scripts/story-status.sh [epic-directory]` defaults to production/epics/.
It observes direct epic story files and their header Status before the first H2
content section, excluding fenced examples and comments. Supported Markdown header
forms are Status: X, **Status:** X, > **Status**: X and - **Status**: X. Case variants
and a trailing period are tolerated; legacy Done is reported without rewriting it.
Groups retain IN_REVIEW, IN_PROGRESS, TODO, BLOCKED, OTHER and NO_STATUS, with
MALFORMED/CONFLICT for invalid or multiple declarations and DONE for completed rows.
COMPLETE counts declared status only. Group order never selects a next task.
Unknown/malformed observations are findings (exit 0), not readiness/completion proof.
EMPTY identifies successful discovery with no stories. Missing scope, discovery/read
errors or missing runtime return exit 2, with any partial observations identified.
This helper shares the Bash/Python/root/path requirements above, accepts a relative
studio path or absolute project-local Windows directory, and writes no files/logs.
It is not registered as a lifecycle hook. Sprint status/synchronization consumers
must still resolve membership and use the actual stories; execution and navigation consumers use the same interface. Retrospectives also remain manually invoked.

## Artifact and Git observers

Read [artifact observation](artifact-observation.md) for artifact-check and explicit detect-gaps behavior, and [run and observe](run-and-observe.md) for the optional selected-project Godot helper. The Git pre-tool handlers require working Python/Git and inspect supported literal command forms; read their hooks-reference documents for staged-content checks and limitations. None of these observers establishes a whole-build or progression pass.
