# Lifecycle Inputs, Outputs and Limits

Verified against https://learn.chatgpt.com/docs/hooks on 2026-10-08.
The wrappers read JSON stdin; event name must match the handler. SessionStart source is
startup/resume/clear/compact; PreCompact/PostCompact trigger is auto/manual. Supplied session_id
and turn_id are strings; Stop stop_hook_active, when supplied, is boolean. Never parse the transcript.

SessionStart emits hookSpecificOutput with hookEventName and additionalContext. PostCompact and
PreCompact use supported continue/systemMessage fields; plain stdout is ignored for those events.
Stop emits JSON continue:true and does not request another turn. Invalid input or unavailable Python
reports NOT ASSESSED and nonzero execution failure. Valid recovery absence/malformed notes are
observations, not hook-execution success evidence for the underlying task.

Root and runtime resolution reuse hook-lib.sh, native_path and existing Windows launchers. Event IDs
are JSON data, never executable code or filesystem paths. Only Stop/PreCompact/PostCompact append
event files under ignored production/session-logs/; CGS_HOOK_DRY_RUN=1 suppresses them. PreCompact
includes bounded checkpoint and checkout observations without attributing changes to the session.
SessionStart has no file writes. source=compact does not invoke detect-gaps again.

Hook loading/trust/event support depends on the active client. A direct wrapper or Windows launcher
test cannot establish native dispatch. No SessionEnd, automatic rotation, status-line, automatic
task selection, cross-chat memory or review-skipping mechanism is registered.
