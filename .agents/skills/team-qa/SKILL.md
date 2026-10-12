---
name: team-qa
description: Coordinate actual QA execution and sign-off for the selected sprint or
  feature using criterion-level evidence.
---

# Team Qa

Invoke as `$team-qa`. Arguments: `[sprint | feature: system-name]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Resolve the selected sprint or named feature; without a selector use explicit current scope or ask.
Reject malformed feature arguments. Read actual membership and story status, applicable GDD/FRAMEWORK,
resource/tool contracts, QA plans, actual build/revision, selected test/launch commands and relevant
bugs. A missing root/build/plan input leaves dependent work unassessed. Do not infer the newest report
is relevant from its date alone.

Use QA strategy expertise to map all applicable criteria to feasible automation, inspection, engine,
manual and human evaluation. Assign available qualified executors under current delegation policy;
plan authorship does not require a fixed named role. Use `$qa-plan` for authorized missing/updated plans,
preserving scope identity. Required independent review persists when executors or depth change.

Check matching smoke evidence before dependent full QA execution. Run `$smoke-check` within the
request's scope if needed. FAIL or required UNKNOWN/NOT ASSESSED coverage blocks the affected handoff;
PASS WITH WARNINGS is acceptable only for nonrequired gaps under applicable policy. Preserve useful
planning and unrelated assessments while that handoff is blocked.

Execute actual test cases with configured tools and real inputs. Record build, steps/command, outcome,
limitations and actual reviewer for every method. Human experience, listening, accessibility and
intended-user tool evaluation require actual people. Report observed bugs through `$bug-report` when
authorized; absence of a person or engine cannot become a passing simulation.

Return coverage, actual pass/fail/unassessed cases, bugs and **APPROVED / APPROVED WITH CONDITIONS /
NOT APPROVED / NOT ASSESSED**. Conditions are advisory; required failures or missing evidence prevent
approval. A request for the QA cycle authorizes its bounded sign-off record at
production/qa/qa-[scope]-[session].md. Preserve prior sessions and inspect the saved output. No automatic
story closure, session-state creation or phase advance follows QA sign-off.
