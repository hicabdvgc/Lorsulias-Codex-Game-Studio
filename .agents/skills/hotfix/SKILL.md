---
name: hotfix
description: "Implement an urgent bounded fix, verify actual results and coordinate authorized delivery or recovery using the project’s Git or non-Git route."
---

# Hotfix Workflow

Invoke `$hotfix [bug-id|description]`.

Read root instructions and the shared contracts linked below. Carry existing bounded task authorization
through saves; clarify consequential unresolved choices. Reread shared files before writes, preserve
concurrent changes and stable identities, and read back promised outputs. Required independent review
and actual human evidence survive executor changes and review-depth choices. Report missing evidence
and preserve partial work; a saved document never establishes approval or execution.

Read `.codex/docs/release-and-operations.md`, `.codex/docs/execution-and-evidence.md`,
`.codex/docs/progression.md`, live `docs/technical-preferences.md`, and the selected release context.
Apply the shared candidate identity, evidence, verdict, write and external-action contracts.

## Resolve and investigate

For a bug ID, require one matching production/qa/bugs/BUG-NNNN-slug.md and preserve its identity. In
description mode, clarify missing impact/reproduction/build information; do not claim an original bug.
Use recorded severity and actual urgency. S1/S2 emergency work may use this route; redirect ordinary
nonurgent work through bug/work-item procedures with REDIRECTED. Do not invent severity from markers.

Read affected GDD/FRAMEWORK, resource/tool contracts, Accepted ADR/TR/scoped integer CONTROL or
justified N/A. Resolve actual code/data/tool roots and commands. Identify the smallest supported fix
and dependent integrations; use propagate-design-change where applicable. Preserve useful partial work.

For Git, inspect branch/dirty state, actual release base and existing hotfix branch before operations.
Missing/ambiguous refs, conflicting branch or dirty-work risk requires resolution. Do not guess main,
develop or a release tag, switch user work, or automatically merge two branches. A supplied non-Git
workspace can be used with explicit candidate/recovery identity. Operations require existing authority.

## Implement and verify

Use the incident-response template within the existing designated bug/hotfix record or
production/qa/hotfix-[date]-[short-name].md. Record facts separately from causal hypotheses, actual
changes, candidate, selected recovery procedure/trigger, evidence and remaining decisions.

Implement the bounded code/resource/tool/integration change using qualified available executors.
Identify required targeted and regression checks based on affected criteria and actual interfaces.
Run available checks and obtain required independent/human evidence. A qualified QA assessment selects
matching smoke or targeted team-QA scope; unavailable required assessment or evidence is HOTFIX BLOCKED.
Missing a persona does not waive its required work or create a sign-off.

## Release and follow through

Retain the bug header Open during implementation. Use `$bug-report verify BUG-NNNN` with actual
evidence to reach Verified Fixed, then its authorized close route for Closed. Unavailable verification
preserves status; failed verification cannot claim fixed. Keep incident/deployment state separate.

Prepare the required release checks for the candidate through the shared release contract. Deployment,
Git promotion, external messaging and rollback each need corresponding authorization. Confirm actual
delivery and required post-deploy verification; a pre-deploy pass does not establish deployed success.
On a observed recurrence, record evidence through the bug workflow and assess recovery. Preserve
completed work on a failed handoff. HOTFIX READY TO DEPLOY is preparation; HOTFIX COMPLETE requires the
requested delivery/verification, otherwise report HOTFIX BLOCKED with remaining dependency.

Patch notes are an optional authorized post-release handoff. Incident follow-up uses its actual record
or a relevant supported sprint/milestone retrospective; there is no forced review deadline or scheduler.
