# Release and Operations Contracts

## Requirements and assessment

`production/releases/RELEASE_CHECKLIST.md` owns selected release requirements. Use the
release-checklist template to record version/scope, platforms and distribution route, requirement
identity and source, applicability, obligation strength, evaluation method, responsible evaluator,
and unresolved decisions. Preserve existing identities when wording changes. A requirements draft
is useful but cannot support final acceptance until its consequential decisions are settled.

`$release-checklist` authors scoped requirements and the internal assessment.
`$launch-checklist` evaluates applicable external/platform/distribution/operational requirements.
Both read the same requirements baseline; neither silently relaxes a requirement during assessment.
Explicitly authorized requirement changes retain rationale and invalidate affected old conclusions.

Internal reports use `production/releases/release-checklist-[date].md`; external reports use
`production/launch/launch-checklist-[date].md`. Each records version, candidate build/revision,
platforms, scope, requirements baseline (revision or identifiable snapshot), generated date,
item-level PASS / FAIL / NOT VERIFIED / justified N/A, evidence method/result/limitations and
actual evaluator, required independence/human evidence, and verdict with blocking/advisory findings.
Use an exact report returned by its writer or explicitly identified by the task. On date collision,
update only the same assessment when requested; resolve a separate explicit path for another candidate.
Reread before saving, preserve concurrent changes, and read back the promised output.

Known required failure or required unavailable evidence means RELEASE BLOCKED / LAUNCH BLOCKED.
With all required checks satisfied, unresolved advisory findings yield CONCERNS; otherwise use
RELEASE READY / LAUNCH READY. Preserve known failures alongside evidence gaps. Project-selected
bug dispositions apply; severity labels alone do not invent a new acceptance policy. An undecided
obligation is a blocking definition gap, not N/A. Report inapplicability with its project basis.

Final acceptance uses this canonical checklist and the actual candidate's applicable evidence.
`$team-release` requires both persisted READY reports for the exact candidate, scope/platforms and
requirements baseline, plus applicable final-acceptance evidence. CONCERNS, previews, stale reports,
unknown scope and missing evidence cannot enter GO. These authored reports are release deliverables;
they do not introduce review receipts or automatic review skipping. Assessment alone never deploys.

## Candidate to delivery

Resolve actual roots, launch/test/build commands and selected services from live technical preferences
and project evidence. A version label alone does not establish artifact identity; retain a build ID,
revision and artifact reference/checksum where available. Changed candidates need affected checks
reassessed. Verify the delivered artifact corresponds to the checked candidate.

Select applicable build, QA, human, independent, performance, security, localization, certification,
legal, store and operational checks from actual commitments. Unavailable required evidence blocks
the dependent step. No default telemetry, storefront, online service, CI, staging, warning budget,
soak duration or on-call period is imposed. Current platform obligations need official evidence;
restricted/unavailable documentation stays explicit and cannot support a pass.

Existing explicit task authorization carries through bounded work. Release preparation does not
itself authorize tags, pushes, deployments, external messages or publication. Resolve exact operations,
targets and candidate before those actions; do not repeat requests when authorization already covers
them. Use qualified available executors under current delegation policy. Preserve required review
independence regardless of role availability. Prepare communication drafts separately from publication.

For a selected staging route, obtain actual matching smoke results before production promotion.
For direct/package delivery, perform the selected route's actual verification without inventing a
staging environment. Preserve partial work and record failed handoffs. Rollback planning identifies
the selected recovery artifact/procedure and trigger; it does not claim recovery was executed.
Monitoring periods, owners and metrics come from supplied decisions. Future checks remain planned.
Do not schedule follow-ups or publish messages without corresponding authorization.

The declared workflow section stays one of conceptualization, development-schematics,
pre-implementation, implementation. Release adds no Live stage and does not bypass the slice,
milestone or final-acceptance requirements in progression.md.

## Change records and incident handoffs

`$changelog` requires Git and verifies the selected range. Its optional internal history save is
`docs/CHANGELOG.md`. `$patch-notes` may read a matching release changelog without Git and writes one
authoritative `production/releases/[version]/patch-notes.md`. Preserve old copies and explicit links;
new runs do not automatically mirror into docs/patch-notes/. Draft notes never establish shipment.
Retrospective context comes from `production/retrospectives/` and cannot prove release inclusion.

Use `.codex/docs/templates/incident-response.md` with the uniquely identified bug/hotfix record,
or `production/qa/hotfix-[date]-[short-name].md`. Preserve BUG identities and the bug header's
Open -> Verified Fixed -> Closed lifecycle; a fix implementation is not verification. Incident
observations, causal hypotheses, mitigation, deployed verification and follow-ups remain distinct.
Use supported sprint/milestone retrospective targets only when those scopes actually apply.
