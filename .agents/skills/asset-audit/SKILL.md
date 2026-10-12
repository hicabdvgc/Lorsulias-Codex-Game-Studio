---
name: asset-audit
description: "Audits game assets for compliance with naming conventions, file size budgets, format standards, and pipeline requirements. Identifies orphaned assets, missing references, and standard violations."
---

Read `.codex/docs/resource-preparation.md` for resource locations, shared write,
review/evidence and recovery requirements. Its shared handoff rules apply here;
initial design can record future resource needs before type contracts exist.

## Invocation and execution

Invoke this workflow as `$asset-audit`.

Arguments: `[all|art|audio|vfx|shaders|data]`. Empty input defaults to `all`.
Normalize the category to lowercase. On any other value, stop before scanning
and list the accepted values.


## Phase 1: Read Standards

Read the applicable RES_TYPE/TYPE_TEMP, asset specification, visual/audio direction,
live technical preferences and scoped AGENTS.md instructions. Identify each rule's
source and obligation. Resolve conflicting contract requirements rather than
silently selecting a winner. Unselected naming, format or budget rules remain
NOT CHECKED; examples never become defaults.

## Phase 2: Select Actual Resource Scope

Resolve categories through RES_TYPE and the declared resource inventory, source and
import mappings. Include prepared resources in `res_lib/` and declared engine copies
when relevant; do not infer categories solely from folder names. For `all`, list
all declared types and locations and identify unmapped material. For a category,
select its mapped types. If contracts are absent, a supplied inventory can support
bounded existence/syntax observations; report which intended checks cannot run.

Do not create missing directories. Distinguish absent paths, unreadable paths,
unsupported formats and an empty scope. Record sources separately from prepared
outputs to avoid treating intentionally loose material as failed production assets.

## Phase 3: Run Compliance Checks

For every applicable check, record one of `PASS`, `FAIL`, or `NOT CHECKED` plus
the evidence used. If a binary property cannot be read, a file cannot be parsed,
or a referenced schema does not exist, record `NOT CHECKED` and the reason; never
infer that the asset passed.

Check selected naming, file-size/dimension/duration budgets and formats only against
explicit applicable requirements. Check structured syntax with an available parser;
schema compliance requires the actual schema and a suitable method. Media property
and engine-import checks require readable evidence and applicable tools. A manual
inspection can be evidence if its method and limitations are recorded.

**Unresolved-reference candidates:** Search existing source code, scenes,
prefabs/resources, data files, manifests, and asset specs for each asset's project
path, engine URI, and stable resource identifier. If no direct reference is found,
report `NO REFERENCE FOUND`; do not call the asset deletable because dynamic or
editor-bound references may not be searchable.

**Missing assets:** Extract references from the same repositories and normalize
engine URIs, project-relative paths, separators, and case rules to a project path
before testing existence. Ignore known imported/derived paths. Put references
that cannot be resolved in `NOT CHECKED` rather than reporting them as missing;
never report one normalized path as both missing and unreferenced.

---

## Phase 4: Output Audit Report

```markdown
# Asset Audit Report -- [Category] -- [Date]

## Summary
- **Total assets scanned**: [N]
- **Naming violations**: [N]
- **Size violations**: [N]
- **Format violations**: [N]
- **Assets with no reference found**: [N]
- **Missing assets**: [N]

## Check Evidence
| File | Check | Expected | Actual | Result |
|------|-------|----------|--------|--------|

## Naming Violations
| File | Expected Pattern | Issue |
|------|-----------------|-------|

## Size Violations
| File | Budget | Actual | Overage |
|------|--------|--------|---------|

## Format Violations
| File | Expected Format | Actual Format |
|------|----------------|---------------|

## Assets With No Reference Found
| File | Evidence Searched | Result | Recommendation |
|------|-------------------|--------|----------------|

## Missing Assets (normalized reference points to absent file)
| Reference Location | Expected Path | Normalization Evidence | Result |
|-------------------|---------------|------------------------|--------|

## Unverified References
| Reference Location | Original Reference | Reason |
|-------------------|--------------------|--------|

## Recommendations
[Prioritized list of fixes]

## Verdict: [COMPLIANT / WARNINGS / NON-COMPLIANT]
```

`COMPLIANT` is allowed only when every applicable check was actually performed
and passed. Any `NOT CHECKED`, empty scan, unsupported file, or recoverable scan
error forces at least `WARNINGS`; a failed blocking format or normalized missing
reference produces `NON-COMPLIANT`. These three verdicts are the only overall
health classification; do not emit a second CLEAN/MINOR/NEEDS enum.

Return the report in conversation. Save only when explicitly requested, to the user-selected bounded report path; otherwise remain read-only.

---

## Phase 5: Next Steps

- Fix naming violations using the patterns defined in AGENTS.md.
- Identify unused candidates for a separate authorized retention decision; this audit deletes nothing.
- Run `$content-audit` to cross-check asset counts against GDD-specified requirements.
