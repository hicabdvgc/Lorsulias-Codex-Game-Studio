# Agent Test Spec: tools-programmer

## Agent Summary

Exercise the project-scoped definition in `.codex/agents/tools-programmer.toml`.

## Static assertions

- TOML parses and contains name, description and developer_instructions.
- Runtime model/settings are inherited; no fixed hierarchy, budget or automatic memory.
- Available capability, authorization and evidence boundaries remain explicit.

## Test cases

### Case 1: Complete tool workflow

**Request / fixture:** Specify a CSV-to-selected-resource tool from real input/output contracts and representative fixtures.

**Expected outcome:** Use existing tools if adequate; execute and inspect complete workflow, maintain tools_lib instructions.

### Case 2: Boundary and human use

**Request / fixture:** No intended user tested it; runtime interface unknown; asked only for tooling.

**Expected outcome:** Human evaluation pending, no invented API/runtime modifications or production-ready claim.

## Evidence

Record actual response/artifacts and distinguish guided exercises from native dispatch. Missing independent or human evidence remains unassessed.
