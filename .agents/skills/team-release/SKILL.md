---
name: team-release
description: 'Orchestrate the release team: coordinates release-manager, qa-lead,
  devops-engineer, and producer to execute a release from candidate to deployment.'
---

# Release Coordination

Invoke `$team-release [version|next]`.

Read root instructions and the shared contracts linked below. Carry existing bounded task authorization
through saves; clarify consequential unresolved choices. Reread shared files before writes, preserve
concurrent changes and stable identities, and read back promised outputs. Required independent review
and actual human evidence survive executor changes and review-depth choices. Report missing evidence
and preserve partial work; a saved document never establishes approval or execution.

Read `.codex/docs/release-and-operations.md`, `.codex/docs/execution-and-evidence.md`,
`.codex/docs/progression.md`, live `docs/technical-preferences.md`, and the selected release context.
Apply the shared candidate identity, evidence, verdict, write and external-action contracts.

## 1. Resolve the release task

Resolve version, outcome scope, candidate source, target platforms and actual distribution route from
the request and explicit records. `next` requires one agreed target; ambiguous/missing candidates need
clarification. Preparation-only requests stop with an accurate prepared/blocked outcome. Dates remain
unset unless selected. No branch or version change precedes resolution of its actual target and authority.

## 2. Prepare the candidate

Assign bounded responsibilities to qualified available people/agents under active delegation policy.
Useful roles are release-manager for candidate/version/change records; QA for evidence; DevOps for
build/delivery; applicable security/network/localization/performance specialists; community for drafts.
No fixed reporting chain or automatic spawning is required. Executor fallback preserves required
independent review. Each shared file or delivery action has one assigned writer/executor.

Use selected repository/versioning conventions and preserve dirty work. Branching/tagging applies only
to an actual Git route with authority for those operations. Generate selected builds, internal changelog
and `$release-checklist`/`$launch-checklist` reports. Request their explicit-only invocation when necessary;
never fabricate their verdicts. Callers that already explicitly authorize them need no repeat prompt.
Select applicable QA, human/independent review, performance, localization, security and platform evidence.
Telemetry is N/A with a documented no-telemetry scope; inaccessible selected telemetry is unassessed.

## 3. Go/no-go

Read back both persisted reports from exact returned/identified paths. Verify version, candidate,
platforms, scope and requirements baseline all match. Require RELEASE READY and LAUNCH READY plus
applicable final-acceptance evidence. CONCERNS, missing/malformed/stale reports, required unavailable
sign-off, failed checks or build changes mean NO-GO. Preserve the reason and partial work; resolve the
underlying evidence and reassess before delivery. A rationale cannot replace a required passing check.

## 4. Deliver the verified candidate

Identify exact artifact, Git operations if any, destinations and rollback route. Use existing explicit
authorization covering each action; clarify uncovered consequential operations before acting. Follow
the selected staging or direct/package route. Staging requires actual matching smoke evidence before
production; direct delivery uses its selected verification. Rebuilding/changing the candidate requires
affected checks again. Confirm delivered identity and installation/launch evidence required by the route.
Do not duplicate deployment tasks. On failure, stop dependent promotion/publication, preserve recovery
information and report actual partial state. Do not automatically reset branches or execute rollback.

## 5. Communicate and monitor

Prepare `$patch-notes` at the canonical single release path and applicable announcements/known issues.
Publish only with explicit messaging/publication authorization and verified facts; do not announce
success after failed delivery. Record actual post-release observations separately from planned monitoring,
with supplied duration, owners and metrics. Schedule nothing without scheduling authorization.
Use incident-response for actual incidents and supported retrospective scopes when applicable.

Return version/candidate, exact report paths, GO/NO-GO basis, actions actually performed, delivery status,
communication state, remaining monitoring and blocked dependencies. COMPLETE requires the requested
authorized delivery and applicable immediate verification to succeed; PREPARED identifies preparation-only
completion; BLOCKED identifies unmet required work. Keep production/stage.txt unchanged by this skill.
