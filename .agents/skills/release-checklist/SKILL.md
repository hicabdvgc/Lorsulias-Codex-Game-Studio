---
name: release-checklist
description: Generate an internal release readiness checklist from release-scope stories,
  open bugs, QA evidence, build evidence, and changelog status.
---

# Internal Release Requirements and Readiness

Invoke `$release-checklist [release or milestone identifier]`. Preserve explicit invocation policy.

Read root instructions and the shared contracts linked below. Carry existing bounded task authorization
through saves; clarify consequential unresolved choices. Reread shared files before writes, preserve
concurrent changes and stable identities, and read back promised outputs. Required independent review
and actual human evidence survive executor changes and review-depth choices. Report missing evidence
and preserve partial work; a saved document never establishes approval or execution.

Read `.codex/docs/release-and-operations.md`, `.codex/docs/execution-and-evidence.md`,
`.codex/docs/progression.md`, live `docs/technical-preferences.md`, and the selected release context.
Apply the shared candidate identity, evidence, verdict, write and external-action contracts.

## Resolve requirements and candidate

Use an explicit target or one validated active reference. Ambiguity needs selection; never choose the
latest file. Resolve version, candidate identity, platforms and included work. Distinguish a request
to draft/update requirements from assessment against settled requirements. Read the selected milestone,
scope decisions, designs/FRAMEWORK, accessibility, resource/tool obligations and applicable platform facts.

Use `.codex/docs/templates/release-checklist-template.md` to author/update
production/releases/RELEASE_CHECKLIST.md within the request. Preserve agreed requirements and their
strength. Unknown choices stay Draft. Do not invent release commitments to fill a template. If the task
is assessment-only, report missing definitions and do not write them without authoring authorization.

## Assess internal readiness

Read authoritative release-scope stories and actual criterion evidence; Complete labels alone do not
prove current candidate coverage. Read relevant bug records, QA/sign-off, matching smoke/regression,
build/install results and the version changelog. Resolve actual roots/runners. CI is conditional.
Capture scope, candidate/revision, inputs, method, result, limitation and actual evaluator. A planned
check or evidence path is NOT VERIFIED. TODO/FIXME markers are candidates, not severity classifications.
External certification, distribution and launch operations are handed to `$launch-checklist`.

Use internal item PASS/FAIL/NOT VERIFIED/justified N/A. Required failure or unavailable evidence yields
RELEASE BLOCKED. With required items passed, unresolved advisory items yield CONCERNS; otherwise
RELEASE READY. Unknown requirement applicability blocks definition/readiness. Compare only an explicitly
identified comparable previous report; otherwise label first baseline. Preserve known failures and gaps.

## Output and save

Show release identity/baseline, story/bug disposition, item evidence, changelog state, comparable deltas,
required/advisory findings and canonical verdict. Save the requested assessment at
production/releases/release-checklist-[date].md using the shared collision/write rules. Explicit
read-only review remains conversational. Return the exact saved path and verdict; failed saves do not
satisfy team-release. Requirements and report writes are separate outcomes; preserve either successful
write if the other fails. Final acceptance and deployment remain separate decisions.
