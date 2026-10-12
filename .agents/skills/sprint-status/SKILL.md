---
name: sprint-status
description: Report a selected sprint from authoritative story statuses and actual
  planning evidence without modifying progress.
---

# Sprint Status

Invoke as `$sprint-status`. Arguments: `[sprint-number or blank for current]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Resolve an explicit sprint number to its actual plan. For current, use the explicitly identified
current sprint in task/project records; conflicting current declarations require clarification.
Never choose the highest number or replace a requested historical sprint with current YAML.
Read membership and supplied dates/capacity from that plan and matching derived YAML, then resolve
every story and its header Status. `.codex/scripts/story-status.sh` may assist discovery; inspect
its errors and keep scope aligned to selected membership. Unreadable or missing stories remain gaps.

Report Not Started, Ready, In Progress, In Review, Complete/legacy Done and Blocked separately;
unknown/conflicting headers cannot be assigned a default. Report YAML disagreement without changing
stories. Preserve epic-qualified identity and avoid double-counting duplicate references. Current
story progress is not evidence of a historical sprint's completion; use actual period records for
historical claims. In a worktree, label the checkout/commit and excluded unintegrated deliveries.

Calculate calendar days only from supplied valid dates and state the basis. Show observed completion
counts over known membership, with missing records separately; these counts do not measure effort.
Use ON TRACK / AT RISK / BEHIND only when schedule, remaining work and comparable capacity evidence
support that assessment; otherwise use NOT ASSESSED. Age/Last Updated can prompt a question but cannot
prove a stall. No fixed stale-day or burndown thresholds apply without project policy.

Return scope, progress, blockers/dependencies, supported schedule risks, limitations and candidate
next actions. Priority does not make a story Ready. Optional sprints do not determine milestone success.
This is read-only and conversational: status synchronization belongs to an authorized planning/update
operation, completion to `$story-done`, and advancement to `$gate-check`.
