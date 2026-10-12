# Skill Test Spec: $skill-test

Category: utility. Inputs: static [name|all], spec [name], category [name|all], audit.
Every mode returns conversation results and makes no file/catalog changes.

## Cases

| ID | Concrete fixture/request | Expected outcome |
|---|---|---|
| ST1 | static report-skill; valid identity/UI metadata, explicit read-only scope, required report fields and available references | Seven package checks assessed; supported optional metadata accepted; COMPLIANT when all pass; no writes |
| ST2 | Same package, UI prompt invokes /wrong-name and required description is absent | Exact identity/UI findings with evidence; NON-COMPLIANT; no invented spec or repair |
| ST3 | spec report-skill; registered spec requires a findings table but written skill omits findings | Compare all assertions, flag the missing outcome; NON-COMPLIANT; state written-contract comparison, without claiming fixture execution |
| ST4 | spec fixture-skill in an isolated fixture whose catalog spec is null | Explicit missing-coverage failure; NON-COMPLIANT; no guessed path or fabricated evaluation |
| ST5 | category report-skill with a missing/empty category authority | NON-COMPLIANT authority finding; no invented rubric; other targets continue in all mode |
| ST6 | audit the current installed studio | Discover actual skill/persona identities and match registered specs; assess current coverage without assuming missing utilities; no stale upstream counts. A complete, valid fixture can be COMPLIANT; required missing coverage in a deliberately incomplete fixture is NON-COMPLIANT |
| ST7 | An actual file is inaccessible, while another inspected file has a known defect | Preserve the known failure plus NOT ASSESSED check; overall NON-COMPLIANT; never hide failure behind uncertainty |
| ST8 | static ../outside or invalid/missing mode | Usage/invalid-target explanation, no traversal and no writes |
| ST9 | audit fixture has equal counts but duplicate identities and an orphan spec | Report identity defects despite matching totals; NON-COMPLIANT |

## Shared assertions

- Discover actual implementation/spec sets; use catalog paths for registered specs.
- Every applicable check has evidence and a result. Explain inapplicability.
- Missing optional quick validator is INFO; project checks continue.
- COMPLIANT needs all applicable checks passed; WARNINGS reflects partial/advisory
  issues; required unavailable evidence yields NOT ASSESSED unless a known failure
  already establishes NON-COMPLIANT.
- Review results stay in conversation. last_* fields remain unchanged.
- Do not require heading counts, fabricate a passing behavior run, or treat
  pending coverage as passed.

These are scenario specifications. Actual execution evidence must be recorded
separately by an authorized evaluator; the spec itself certifies no execution.
