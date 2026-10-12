# Installed Hook Inputs and Outputs

Handlers read one JSON object from stdin. Unknown fields are tolerated. Common
fields include cwd, session_id, hook_event_name, and optional turn_id. The registered
event/matcher supplies routing. See [official documentation](https://learn.chatgpt.com/docs/hooks).

## Command inspection

```json
{"hook_event_name":"PreToolUse","tool_name":"Bash","tool_input":{"command":"git status"}}
```

The command checker reads tool_input.command. A detected prohibited pattern exits
2 with a reason on stderr. Non-matching command text exits 0. Python unavailability
returns a NOT ASSESSED context message. Command text is inspected, never executed.

## Skill-change reminder

```json
{"hook_event_name":"PostToolUse","tool_name":"apply_patch","tool_input":{"command":"*** Begin Patch\n*** Update File: .agents/skills/example/SKILL.md\n*** End Patch"}}
```

Path extraction supports the documented patch payload plus direct path/file_path/
paths values. A relevant skill path yields JSON with systemMessage and
hookSpecificOutput containing hookEventName=PostToolUse and additionalContext.
Other paths produce no reminder. This handler does not validate the skill or undo
the completed patch. Missing Python leaves this check explicitly unassessed.

## Agent lifecycle

```json
{"hook_event_name":"SubagentStart","agent_type":"producer","agent_id":"agent-example"}
```

SubagentStop uses the same identity fields. Both log the event in the studio's
production/session-logs/agent-audit.log and return {"continue":true}. Missing
identity values are labeled unknown. CGS_HOOK_DRY_RUN=1 suppresses writes.

Malformed/non-object input or absence of both structured parsers emits NOT ASSESSED
on stderr and stops that handler without performing its action. This is an
advisory unassessed result, not proof of passing. Filesystem/logging errors
return a nonzero process status. Event handling in the client is version-specific.

## Asset syntax observer

`validate-assets.sh` uses PostToolUse apply_patch paths or patch text and the event cwd, resolving within the studio. It checks existing JSON files only under res_lib/ and assets/data/. See [post-edit asset validation](post-merge-asset-validation.md) for supported input forms, unavailable-runtime and malformed-input behavior. Findings are observational; this post-edit handler cannot reverse an edit.

## Git observers

validate-commit.sh and validate-push.sh consume the PreToolUse Bash command plus required event cwd. They parse a supported literal Git invocation and inspect the actual repository without executing that command. Supported command details, JSON feedback, failure codes and limitations are in pre-commit-code-quality.md and pre-push-test-gate.md. Both require Python 3.9+ and Git. Native-path conversion in hook-lib.sh supports Windows environments with automatic MSYS argument conversion disabled. Artifact/gap observers retain explicit CLI interfaces; SessionStart calls bounded gap discovery without separately registering those observers.

## Session and compaction lifecycle

See [lifecycle-contract.md](lifecycle-contract.md) for SessionStart, Stop, PreCompact and
PostCompact inputs, event-specific JSON outputs, actual log effects, failure handling and limits.
The shared parser also serves studio-status. Rotation is explicit and has no lifecycle registration.
