---
name: dev-story
description: Implement a prepared story across code, resources, tools or integration,
  and verify its applicable criteria without closing the story.
---

# Dev Story

Invoke as `$dev-story`. Arguments: `[story-path]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


## Resolve and prepare

Resolve an explicit story path first. Without one, use an unambiguous task-context story;
a session checkpoint is a candidate to check for staleness. Otherwise list actual Ready
stories using `.codex/scripts/story-status.sh` and ask which to implement. A summary does
not establish readiness. In a linked checkout also read `.codex/docs/worktree-workflow.md`.

Read the whole story, governing source requirements, applicable GDDs/FRAMEWORK, Accepted
ADRs and their dependencies, active saved TRs, scoped `docs/architecture/CONTROL.md` rules,
live preferences and relevant resource/tool contracts. Verify actual status and dependencies
before implementation or progress writes. Compare the integer CONTROL revision and inspect
changed rules. Reconcile conflicting registry/source text instead of selecting one silently.
Subjective criteria need feasible observable human protocols, not invented numeric targets.
Use `$story-readiness` for unresolved assessment; existing readiness does not survive a
material prerequisite change without checking it. The skill's CONTRACT.md defines the handoff.

## Implement the bounded result

Identify actual files and integration consumers, implementation steps and completion methods.
Carry the existing request's authorization; clarify unresolved decisions or material expansion.
Set story Status to In Progress, then synchronize its applicable derived sprint entry.

Choose available expertise by task: gameplay for mechanics, AI for behavior/pathfinding,
networking for protocol/authority, engine for runtime infrastructure, UI for interactions,
and resource/tool executors for their outputs. Use selected engine specialists when their
expertise is needed and delegation is authorized; there is no universal spawn requirement.
Assign non-overlapping writes if work is delegated and supply precise source paths, rules,
outputs and criteria. Missing engine/root information blocks dependent engine writes, while
independent prepared-data work may continue if its contracts are sufficient.

Implement using real interfaces and existing patterns. Keep shared values and resources in
locations required by the selected contracts; avoid inventing universal data-driven rules.
Create appropriate tests/protocols alongside the output where required, using actual test
roots and selected runners. Exercise affected integration and resource relationships. Use
`.codex/docs/run-and-observe.md` for runtime-visible changes and the tool-development procedure
for complete tool workflows and intended-user evaluation. Preserve work when a later check fails.

## Verify and hand off

Run the affected configured checks. Record every criterion's method, revision, result and
remaining evidence. No test file, smoke report or delegated claim suffices without inspecting
its relevant result. Report files changed, deviations, engine/reference gaps and one of:
**Implemented and Verified / Implemented Not Verified / Partial / Blocked**.

Leave the story In Progress. Recommend the applicable `$code-review`, `$test-evidence-review`
and `$story-done` checks; do not claim they ran. If in a worktree, include the fixed base,
delivery SHA or PENDING COMMIT, actual branch-local verification and integration needs.
Git commit/push and automatic session-state creation are not implied by implementation.
