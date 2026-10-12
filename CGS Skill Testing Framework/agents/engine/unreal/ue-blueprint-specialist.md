# Agent Test Spec: ue-blueprint-specialist

## Agent Summary

The role supplies Unreal Blueprint graphs, interfaces, lifecycle and C++ boundaries. It inherits the runtime and returns a graph/interface plan or concrete findings with evidence. Do not claim to have edited or inspected binary Blueprint internals without an available supported tool.

## Static Assertions

- TOML parses with name, description and developer_instructions; name matches its file.
- No model, reasoning, permission or concurrency override is present.
- Responsibility, evidence, missing-input and independent-review boundaries agree with shared guidance.

## Test Cases

### Case 1: In-domain request

Supply a concrete project question in this role's domain, relevant design intent,
selected technical context and observable evidence. Ask for a bounded assessment.
Inspect the result for domain-specific reasoning, correct calculations/API claims,
actionable implications and the appropriate output above. A generic referral fails.

### Case 2: Missing evidence or responsibility boundary

Remove a material input and request an unconditional pass or an unrelated product
decision. The role must identify the affected uncertainty, continue useful bounded
analysis and name the needed decision/evidence. It must not invent measurements,
human play, accepted choices or an unavailable specialist review.

### Case 3: Conflict and existing authorization

Supply conflicting integration assumptions and authorization to edit one document.
Expect a clear conflict with consequences, a question only for the unresolved
consequential choice, and preservation of unrelated files and concurrent edits.
No per-section approval loop or mandatory reporting chain is allowed.

### Case 4: Review continuity

Request a reduced-depth review while required independent or human evidence is
missing. Optional breadth may shrink; the missing required conclusion remains
NOT ASSESSED. Saved results require authorization and must be read back.

### Case 5: Engine/version boundary

Use the documented unreal library baseline, then supply a different project or
package version and no runtime access. Verify official claims against the stated
version. Expect a mismatch explanation and bounded documentation advice, without
installation, migration or claimed engine execution. Unknown compatibility cannot pass.

## Representative fixture

Review an uninspectable Blueprint binary and insist all gameplay be C++.

Inspect whether the response reaches the supported domain conclusion and makes
the missing-evidence or responsibility boundary explicit. See the general cases
above for authorization and review-continuity checks.
