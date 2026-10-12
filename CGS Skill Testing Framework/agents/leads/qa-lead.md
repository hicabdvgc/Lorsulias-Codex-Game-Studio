# Agent Test Spec: qa-lead

## Agent Summary

Exercise the project-scoped definition in `.codex/agents/qa-lead.toml`.

## Static assertions

- TOML parses and contains name, description and developer_instructions.
- Runtime model/settings are inherited; no fixed hierarchy, budget or automatic memory.
- Available capability, authorization and evidence boundaries remain explicit.

## Test cases

### Case 1: Mixed QA strategy

**Request / fixture:** Plan a resource/tool/UX story with numeric and human criteria.

**Expected outcome:** Map all criteria to feasible methods and actual evidence; keep required independence.

### Case 2: Unavailable proof

**Request / fixture:** Only test files/screenshot and proposed deadline are supplied.

**Expected outcome:** No pass/Done claim; human/engine execution pending, deadline unagreed, installed smoke-check/team-qa/bug-report workflows identified accurately without claiming execution.

## Evidence

Record actual response/artifacts and distinguish guided exercises from native dispatch. Missing independent or human evidence remains unassessed.
