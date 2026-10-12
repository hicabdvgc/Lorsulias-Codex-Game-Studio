# Agent Test Spec: systems-designer

## Agent Summary

The role supplies mathematical rules, economies, progression and subsystem interactions. It inherits the runtime and returns rules/formulas, worked cases and interaction tables where useful, plus unresolved tuning or product choices. A conflict over complexity needs an explicit product decision, not a mandatory hierarchy traversal.

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

### Case 6: Formula regression

Evaluate damage = base_attack * (1 + strength_modifier * 0.1) - defense * 0.5
for base_attack 10..100, strength_modifier 0..20, defense 0..50. Its minimum is
-15 and maximum is 300. The source specification incorrectly expected an always
positive result. Expect NEEDS REVISION if nonnegative damage is required, with a
clamping or rule choice presented to the developer. Balance/fun remains unproven.

## Representative fixture

Review damage = attack*(1+strength*0.1)-defense*0.5, attack10..100/strength0..20/defense0..50; nonnegative required.

Inspect whether the response reaches the supported domain conclusion and makes
the missing-evidence or responsibility boundary explicit. See the general cases
above for authorization and review-continuity checks.
