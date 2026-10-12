---
name: story-readiness
description: "Review whether a story has usable pickup inputs and feasible completion evidence without changing work status."
---

# Story Readiness

Read `.codex/docs/work-preparation.md` for governing inputs, status authority,
criterion-level evidence, review, authorization and recovery rules. Apply them to
the selected scope. Read the package CONTRACT.md when present for its handoff.

## Invocation and resolution
`$story-readiness [story-file-path | all | sprint] [--review full|lean|solo]`.
Validate argument shape and project-contained files. No argument asks for scope.
For an authoring handoff before save, accept the complete supplied story draft
with its planned project-local path and assess that exact candidate. A missing
file without a complete supplied draft remains unavailable. Resolve review depth
from an explicit valid flag; otherwise use focused (lean) review.
All discovers story-*.md under actual epic directories, excluding EPIC/index files.
Sprint resolves an explicit active sprint reference and its plan; YAML membership
must identify the same sprint and agree with plan references. Do not choose by mtime.
Retain every missing referenced story in scope. Empty/unreadable scope is NOT ASSESSED.

Read the full story and relevant source requirements, FRAMEWORK, resource/tool
contracts, applicable accepted decisions/CONTROL and saved TR entries. Resolve
dependency paths first, otherwise exact epic-qualified identity. A missing,
ambiguous, cyclic, self or incomplete prerequisite dependency blocks pickup.

## Checklist
- Intended result and scope are clear; acceptance covers actual behavior without
  requiring a fixed count or heading layout. Linked design rules can supply detail.
- Each outcome has a feasible method: setup, action, observation and decision basis.
  Human assessment is allowed in every type. A bare evidence path cannot turn
  "feels good" into a usable protocol. Future results are completion obligations.
- Required inputs are available and usable against the applicable type contract.
  Files to Create are outputs and need not exist. Missing prerequisites cannot be
  satisfied by fabricated placeholders. Declared resource mappings determine scope.
- Applicable governing ADRs exist and are Accepted; a real list has one primary.
  A reasoned N/A is accepted when genuinely inapplicable, regardless of Type.
- Claimed TR IDs resolve to active saved records; missing required traceability is
  a gap. Nontechnical requirements can cite their source with justified N/A.
- Applicable CONTROL revision is a positive integer and rules are current. A
  mismatch requires assessing affected rules; do not just update a number.
- FRAMEWORK additions/modifications and affected producer/consumer responsibilities
  are specified at the needed scope. Required tools have usable prerequisites.
- Dependencies needed before pickup are complete. Scheduling a predecessor earlier
  does not satisfy it. Claims of completion do not replace required artifact evidence.
- Missing decisions are interpreted in context. An example question mark or quoted
  TODO is not automatically unresolved work. Known consequential open choices block
  dependent work. Unknown estimates can remain a planning gap when pickup is clear.
- Required independent review and feasible human evaluation plans are retained.
  Actual completion evidence need not pre-exist the work that will obtain it.

## Review and verdict
Apply QL-STORY-READY with the same full candidate and input revision. Use available
qualified expertise under the active delegation policy, identify self-review and
keep required independence intact across full/lean/solo. Recheck affected decisions
when their source changes during review; cached stale content is not authoritative.

Return a verdict for each story:
- READY: every applicable pickup condition and required review is satisfied.
- NEEDS WORK: assessable story with remediable direction/evaluation gaps.
- BLOCKED: a concrete dependency, governing decision or consequential choice prevents pickup.
- NOT ASSESSED: unavailable scope/input/reviewer prevents the needed assessment.
Report known blockers even when other checks are unassessed. Never turn incomplete
coverage into an all-ready aggregate. Identify candidate, actual reviewer/method,
source revisions, passing conditions, gaps, exact blockers and corrective producer.

## Read-only handoff
Do not edit stories, statuses, YAML, design or registries. Return conversational
findings; explicitly authorized report saves are bounded and confer no approval.
For sprint scope, flag required planned work that is not READY. Other candidate
stories may be listed as unassessed alternatives, never implicitly Ready.
Next-story pickup needs its own current assessment. Use installed `$dev-story` for authorized implementation.
This assessment does not establish the vertical-slice hard gate.
