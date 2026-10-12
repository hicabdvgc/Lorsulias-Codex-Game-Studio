# Context Management and Recovery

Maintain `production/session-state/active.md` when checkpoint writing is within the task, using
the session-state template. Reread the current file before each update and preserve concurrent or
unrelated notes. Keep exactly one STATUS region and one CHECKPOINT region, in that order, followed
by optional narrative. Refresh the regions rather than append repeated history. Legacy unstructured
notes remain readable manually; migrate them only within authorized scope and preserve their content.

`.codex/scripts/session-state.py` is the shared read-only region parser used by lifecycle handlers
and `$studio-status`; invoke it with the available Python runtime and optional `--root <studio>`.
It returns JSON status, focus fields, checkpoint and limitations. Each region is bounded to 4096
UTF-8 bytes to keep recovery injection small. Oversized/malformed regions are reported without
injecting a misleading truncated checkpoint. Narrative is never injected automatically. Read the
referenced substantive files to verify current work; a checkpoint or Run result is not completion
evidence and cannot replace story/QA records. Missing notes do not prevent recovery from the task.

SessionStart injects available bounded context, declared stage and observational discovery on
startup/resume/clear. After compaction, source=compact injects only recovery context and stage;
it does not repeat the full gap scan. Stop records a turn-stop event, not session shutdown or task
success. PreCompact records available observations; PostCompact reports recovery availability.
Only SessionStart supplies additional developer context. Audit events record actual event IDs and
UTC timestamps under ignored production/session-logs/. Git status describes the checkout and is
not attributed to this session. Hooks never infer the task from recent commits or parse transcripts.

Automatic context delivery depends on the active client's hook loading and event support. A direct
script test does not demonstrate live dispatch. No custom status display or personal/cross-project
memory is installed. Manual checkpoints remain usable if hooks cannot run. Required human or
independent reviews stay required through recovery and executor changes.

Invoke `bash .codex/scripts/rotate-session-state.sh --dry-run` to preview narrative rotation and
omit --dry-run for an authorized rotation. Rotation preserves both bounded regions, creates a
content-identified archive under production/session-logs/, rechecks the source, then replaces only
the narrative with an archive reference. An archive/replacement failure reports exactly what was
saved; completed archives remain recoverable. A cooperative lock prevents simultaneous rotations;
a changed source stops replacement. Rotation validates the exact original bytes through the shared
region parser before archiving, then compares those bytes again before replacement. Do not edit
active.md concurrently with rotation. No hook
rotates or deletes notes. A stale lock is reported for manual inspection, never broken automatically.

For delegation, supply relevant objective, constraints, inputs/revisions, expected outputs and write
boundaries. Context inheritance depends on the runtime; verify rather than assume it. Use only
compaction/session controls actually exposed by the active client.
