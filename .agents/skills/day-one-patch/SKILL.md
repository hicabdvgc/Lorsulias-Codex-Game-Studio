---
name: day-one-patch
description: Prepare a day-one patch for a game launch. Scopes, prioritises, implements,
  and QA-gates a focused patch addressing known issues discovered after gold master
  but before or immediately after public launch, with applicable QA evidence and
  a selected recovery plan.
---

# Day-One Patch Preparation

Invoke `$day-one-patch [known-bugs|cert-feedback|all]`; default all.

Read root instructions and the shared contracts linked below. Carry existing bounded task authorization
through saves; clarify consequential unresolved choices. Reread shared files before writes, preserve
concurrent changes and stable identities, and read back promised outputs. Required independent review
and actual human evidence survive executor changes and review-depth choices. Report missing evidence
and preserve partial work; a saved document never establishes approval or execution.

Read `.codex/docs/release-and-operations.md`, `.codex/docs/execution-and-evidence.md`,
`.codex/docs/progression.md`, live `docs/technical-preferences.md`, and the selected release context.
Apply the shared candidate identity, evidence, verdict, write and external-action contracts.

## Resolve the release and patch scope

Read the identified gold/release candidate and actual launch context, canonical release requirements,
relevant Open/Verified Fixed bugs, certification feedback, work criteria and security evidence. Read
explicitly referenced reports; the newest sprint/security file is not authority. The four-section stage
is context, not a Release/Polish precondition or proof of Gold/final acceptance.

Classify proposed fixes by impact, dependency, uncertainty, verification effort and supplied timing/capacity.
Remove unrelated features; use FRAMEWORK small-change/change-propagation criteria. No four-hour limit,
default patch 1.1 deferral or guessed schedule applies. Missing capacity leaves schedule feasibility
unassessed. Route actual emergencies to `$hotfix`; do not disguise required blockers as accepted risks.
An empty selected scope is NO PATCH REQUIRED, not a fabricated patch record.

## Prepare and implement authorized work

Resolve explicit patch version and candidate plus actual roots/commands. Identify fixes, affected
resources/tools/framework integrations, governing Accepted decisions and justified exemptions. Draft
the selected rollback/recovery plan at production/releases/rollback-plan-[version].md with evidence,
actual trigger and selected responsibility or unresolved choices. Existing authorization covers bounded
saves/implementation; clarify consequential choices. Preserve existing files and useful partial results.

Implement the selected fixes with qualified available executors and stable bug/work IDs. A config/data
change still needs applicable checks. Collect actual verification through the adopted bug workflow;
never set the obsolete Fixed — Pending Verification header. Preserve independence/human requirements.

## QA and patch record

Obtain applicable QA assessment of targeted checks versus broader regression, then actual matching
candidate results. Use installed smoke/team-QA interfaces, preserving explicit invocation policies.
PASS WITH WARNINGS can proceed only when all required coverage passes and warnings are advisory under
the selected policy. FAIL or required unavailable evidence blocks readiness regardless of review depth.

Save production/releases/day-one-patch-[version].md with candidate/scope, completed and deferred fixes
(without invented future versions), actual QA/evaluators/limitations, recovery link, readiness and
deployment authorization still needed. Produce required `$patch-notes [version]` from verified change
evidence at the single canonical release path; verify both promised records. Failed notes save leaves
that handoff blocked and preserves the patch record. Preparation never deploys or publishes.

Return PREPARED only when requested patch preparation and required evidence/outputs are complete;
otherwise BLOCKED with partial work and exact missing dependency. Delivery uses the release contract.
Record supplied incident learning through incident-response or a relevant supported retrospective scope.
