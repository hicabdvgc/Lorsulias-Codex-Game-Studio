# Test Evidence: [Story Title]

> **Story**: `[path to story file]`
> **Story Type**: [Logic | Integration | Visual/Feel | UI | Config/Data]
> **Date**: [date]
> **Tester**: [who performed the test]
> **Build / Commit**: [version or git hash]

---

## What Was Tested

[One paragraph describing the feature or behaviour that was validated. Include
the acceptance criteria numbers from the story that this evidence covers.]

**Acceptance criteria covered**: [AC-1, AC-2, AC-3]

---

## Acceptance Criteria Results

| # | Criterion (from story) | Result | Notes |
|---|----------------------|--------|-------|
| AC-1 | [exact criterion text] | PASS / FAIL / NOT ASSESSED / N/A (reason) | [any observations] |
| AC-2 | [exact criterion text] | PASS / FAIL / NOT ASSESSED / N/A (reason) | |
| AC-3 | [exact criterion text] | PASS / FAIL / NOT ASSESSED / N/A (reason) | |

---

## Supporting Evidence — Logs, Files, Screenshots or Video

List evidence actually obtained below, including commands/methods, exit status, inputs and limitations. Planned checks remain pending. Manual attachments may use this document’s directory
or `production/qa/evidence/[story-slug]/`. Link automated reports from the selected
runner’s actual output location; do not relocate them by assumption.

| # | Filename | What It Shows | Acceptance Criterion |
|---|----------|--------------|----------------------|
| 1 | `[filename.png]` | [brief description of what is visible] | AC-1 |
| 2 | `[filename.png]` | | AC-2 |

*If video: note the timestamp and what it demonstrates.*

---

## Test Conditions

- **Input / resource / tool / game state at start**: [actual reproducible setup]
- **Platform / hardware**: [e.g., "Windows 11, GTX 1080, 1080p"]
- **Relevant measurements and selected targets**: [actual values with units, or N/A]
- **Method / command and working directory**: [actual steps, arguments and observed result]
- **Limitations / missing checks**: [unavailable runner, independent reviewer or human evaluation]

---

## Observations

[Anything noteworthy that didn't cause a FAIL but should be recorded. Examples:
minor visual jitter, frame dip under load, behaviour that technically passes
but felt slightly off. These become candidates for polish work.]

- [Observation 1]
- [Observation 2]

If nothing notable: *No significant observations.*

---

## Review and Sign-Off

Record the actual reviewers and required responsibilities for these criteria.
Identify self-review. Missing required independent review or human evidence remains
unassessed; changing executor or review depth cannot waive it. Evidence does not
automatically change story status or authorize milestone progression.

| Required check / responsibility | Actual reviewer and method | Date / revision | Result / missing evidence |
|---|---|---|---|
| [applicable check] | [actual person/agent; independent or self-review] | [identity] | [result] |

Template: `.codex/docs/templates/test-evidence.md`.
Location: `production/qa/evidence/[story-slug]-evidence.md` (disambiguate by epic when needed).
Use for code, content, resource, tool and integration evidence of any story type.
