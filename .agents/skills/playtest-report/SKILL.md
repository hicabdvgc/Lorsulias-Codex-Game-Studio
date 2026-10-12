---
name: playtest-report
description: Prepare or analyze actual playtest records, separating human observations,
  interpretations and milestone learning.
---

# Playtest Report

Invoke as `$playtest-report`. Arguments: `[new | analyze path-to-notes] [--review full|lean|solo]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Resolve new versus analyze; without enough context ask. Analyze needs readable notes and the relevant
session/build. Read the stated learning question, relevant CONCEPT/GDD/FRAMEWORK or milestone goals,
selected platform/input/accessibility and prior findings only where relevant. Do not manufacture a
hypothesis, participant or measured metric from generic design expectations.

New creates a clearly **NOT RUN** record: session/build/platform/input, actual participants to fill,
question and protocol, first impressions, flow, working/pain/confusion/delight observations, relevant
feature feedback, encountered bugs, supplied quantitative measures and open questions. No fixed
first-five-minute window, priority count or default positive assessment applies.

Analyze organizes actual notes into observations with provenance, interpretations, supported
findings, conflicting reports and unanswered questions. Preserve human wording and uncertainty.
Connect findings to slice experience/usability, framework operations or the selected MVP/Alpha/Beta/
Gold learning goals. Proposed design actions are separate from accepted decisions. Route observed
bugs through `$bug-report`, scoped changes through FRAMEWORK/`$propagate-design-change`, and unresolved
experience decisions to the developer. Developer authorship of CONCEPT remains intact.

Apply relevant CD-PLAYTEST review guidance when an analyzed result requires it; blank records
cannot supply that review. Required independent or human evidence persists across review-depth choices.
Save new records under production/playtests/playtest-[session-or-scope]-[date].md. Preserve existing
explicit report references and previous sessions, resolve collisions before overwriting, and inspect
the saved record. Report what was observed, what was inferred and what remains untested. No stage,
story or milestone status changes follow saving a report.
