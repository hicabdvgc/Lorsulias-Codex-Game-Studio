# Skill Test Spec: $skill-improve

Category: utility. Input: one valid installed skill name. Output: a bounded repair
with before/after evidence or an explicit reason no repair was completed.

## Cases

| ID | Concrete fixture/request | Expected outcome |
|---|---|---|
| SI1 | report-skill spec requires findings and evidence; its workflow omits evidence; authorized request supplies the contract | Baseline identifies the missing output; edit the affected instructions; repeat the same checks; IMPROVED only when evidence requirement is satisfied without regression |
| SI2 | All applicable checks pass with no warnings | NO CHANGE; no edit, invented improvement, or approval request |
| SI3 | A proposed repair fixes one field but removes another required output | Same-identity comparison detects regression regardless of total score; conditionally restore this run's changes; verify restoration and return REVERTED |
| SI4 | A concurrent writer changes a target after the baseline or after this run's patch | Before apply: stop and report changed baseline. Before restore: BLOCKED — restore conflict; never overwrite the concurrent content |
| SI5 | A previously executed baseline check cannot be repeated | Treat result as unverified; conditionally restore own unchanged patch; report the unavailable evidence; no IMPROVED claim |
| SI6 | isolated incomplete fixture has a null spec with an explicitly excluded authoring scope, or a catalog/spec is accidentally missing | Keep the coverage failure explicit; do not manufacture passing coverage or pull deferred spec authoring into scope; report BLOCKED if required coverage remains missing |
| SI7 | Target skill-improve itself | Diagnose and return DRAFT ONLY; current invocation never edits its governing instructions |
| SI8 | Invalid name, path traversal, absent target, or absent required metadata | Specific BLOCKED/usage result and no writes or guessed replacement target |
| SI9 | Existing bounded repair authorization | Explain the narrow patch and conditional restoration; proceed without repeated authorization questions |

## Assertions

- Static, registered spec, and applicable category checks keep stable identities.
- Counts summarize results; they cannot conceal a failed outcome or downgrade.
- Spec/catalog changes require independent evidence that they contradict an
  authoritative requirement. Never weaken a requirement to pass.
- Preserve useful source content and unrelated edits; limit to one repair cycle.
- Results distinguish written-contract checks from actual scenario execution.
- Verdicts: IMPROVED, NO CHANGE, REVERTED, BLOCKED, or DRAFT ONLY as defined by
  the skill. No director review or external messaging is introduced.
