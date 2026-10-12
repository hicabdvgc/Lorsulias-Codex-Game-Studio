---
name: content-audit
description: "Compare declared content requirements with resource inventory and report missing, invalid or unverified content."
---

Read `.codex/docs/resource-preparation.md` for resource locations, shared write,
review/evidence and recovery requirements. Its shared handoff rules apply here;
initial design can record future resource needs before type contracts exist.

## Invocation and execution

Invoke this workflow as `$content-audit`.

Use existing authorization for the bounded task. Describe the intended outputs and preserve unrelated work. Ask only about unresolved consequential choices or material scope expansion; do not repeat file- or section-level approval prompts.

Arguments: `[system-name | --summary | (no arg = full audit)]`. Treat bracketed values as optional unless the workflow says otherwise.

Use available qualified `producer` expertise when useful and delegation is authorized. Otherwise perform the applicable responsibilities in the current agent, preserving required independence and human evidence.


When this skill is invoked:

Parse the argument:
- No argument → full audit across all systems
- `[system-name]` → audit that single system only
- `--summary` → summary table only, no file write

For a system argument, resolve the name through `BREAKDOWN.md` and the
mapped GDD path. Exactly one match is required. Missing or ambiguous matches
stop with the candidate list and no report write.

If `producer` is available, it may return an analysis draft only and must not
write files. If it is unavailable, continue in the current agent. If delegation
fails after scanning, produce a partial report from the collected evidence and
name the missing analysis; never fabricate the omitted results.

---

## Phase 1 — Context Gathering

1. **Read `design/gdd/BREAKDOWN.md`** for the full list of systems, their
   identities, dependencies, and explicitly selected milestone scope. Also read existing explicit asset-format
   requirements from the in-scope GDDs and `docs/technical-preferences.md`
   so implementation format can be compared without inventing a new standard.

2. **L0 pre-scan**: Search all GDD files for `## Summary`/`## Overview`
   and common content-count phrases only to prioritize reading order. A missed
   keyword never excludes a GDD and never proves that it has no auditable
   content.

3. **Read every in-scope GDD** (or the single system GDD if a system name was
   given). At minimum read Summary/Overview, Detailed Rules, Visual and Audio
   requirements, and every section containing an explicit list. If those
   sections cannot be located reliably, read the full document.

4. **For each GDD, extract explicit content counts or lists.** Look for patterns
   like:
   - "N enemies" / "enemy types:" / list of named enemies
   - "N levels" / "N areas" / "N maps" / "N stages"
   - "N items" / "N weapons" / "N equipment pieces"
   - "N abilities" / "N skills" / "N spells"
   - "N dialogue scenes" / "N conversations" / "N cutscenes"
   - "N quests" / "N missions" / "N objectives"
   - Any explicit enumerated list (bullet list of named content pieces)

4. **Build a content inventory table** from the extracted data:

   | System | Content Type | Specified Count/List | Source GDD |
   |--------|-------------|---------------------|------------|

   Note: If a GDD describes content qualitatively but gives no count, record
   "Unspecified" and describe which coverage conclusion lacks a declared baseline. A generative design may instead define qualitative acceptance criteria.

---

## Phase 2 — Implementation Scan

For each content type found in Phase 1, scan the relevant directories and match
implementation identity. When the GDD names content, match each name against
stable existing file/data references and report the missing names; equal raw
file counts do not prove completion. Treat same-named scene, data, and art files
as one content item. Use approximate file counts only when the GDD gives a total
without names, and label that row `Approximate`.

Resolve content through the declared inventory, RES_TYPE/TYPE_TEMP and source-to-library
and engine-import mappings. Inspect actual files in `res_lib/` and the selected
project roots; a directory convention is not proof of an item's type or identity.
Exclude examples, tests and derived duplicates using their documented purpose.
Separate existence, format/reference validation, engine integration and observed
usability. Runtime checks apply only when requested scope includes integration and
a relevant build exists. Mark unreadable or unsupported evidence NOT ASSESSED.

## Phase 3 — Gap Report

Produce the gap table:

```
| System | Content Type | Specified | Found | Gap | Status | Notes |
|--------|-------------|-----------|-------|-----|--------|-------|
```

For each identity that exists in the wrong explicit format, keep it in Found but
add `FORMAT ISSUE` to Notes with expected and actual formats. Format issues are
completeness gaps for the final verdict, distinct from missing names.

**Status categories:**
- `COMPLETE`: every declared identity/criterion is evidenced for the selected audit scope.
- `IN PROGRESS`: some specified content is present but required work remains.
- `EARLY`: use only if the project defines this stage; explain its criterion.
- `NOT STARTED`: a complete reliable inventory establishes no specified content exists.
- `UNSPECIFIED`: no usable requirement baseline; exclude from numeric totals.
- `NOT ASSESSED`: inventory, format or other required evidence cannot be inspected.

A count may describe existence coverage even when integration/usability is unassessed;
label the coverage dimension. Approximate counts cannot establish COMPLETE.
Priority follows explicit project obligations and demonstrated dependencies, without
inventing MVP tags or percentage-based schedules.

**Summary line:**
- Exclude UNSPECIFIED rows from numeric sums.
- Total content items specified (sum of numeric Specified values)
- Total content items found (cap each row's contribution at its Specified value;
  report excess identities separately in Notes)
- Each numeric Gap is `max(0, Specified - Found)`.
- If total Specified is zero, output `Overall gap: not computable — no numeric
  specifications`; never divide by zero. Otherwise compute
  `sum(row gaps) / total Specified * 100`.

---

## Phase 4 — Output

### Full audit and single-system modes

Present the gap table and summary. When the task already authorizes a saved report,
write `docs/content-audit-[date].md` without another approval prompt and verify it.
Otherwise keep the result conversational and offer the optional save. Re-read an
existing report and preserve unrelated scope; resolve a conflicting assessment
before overwriting. Use this report structure:

```markdown
# Content Audit — [Date]

## Summary
- **Total specified**: [N] content items across [M] systems
- **Total found**: [N]
- **Gap**: [N] items ([X%] not found in the declared inventory)
- **Scope**: [Full audit | System: name]

> Evidence scope: [identity matching / approximate count / supplied criteria].
> Integration and usability: [executed evidence or NOT ASSESSED].

## Gap Table

| System | Content Type | Specified | Found | Gap | Status |
|--------|-------------|-----------|-------|-----|--------|

## HIGH PRIORITY Gaps

[List systems flagged HIGH PRIORITY with rationale]

## Per-System Breakdown

### [System Name]
- **GDD**: `design/gdd/[file].md`
- **Content types audited**: [list]
- **Notes**: [any caveats about scan accuracy for this system]

## Recommendation

Focus implementation effort on:
1. [Highest-gap HIGH PRIORITY system]
2. [Second system]
3. [Third system]

## Unspecified Content Counts

The following GDDs describe content without giving explicit counts. These rows
remain auditable as qualitative design gaps but receive no numeric status.
Consider adding counts to improve auditability:
[List of GDDs and content types with "Unspecified"]
```

After writing the report, ask:

> "Would you like to create backlog stories for any of the content gaps?"

If yes: for each system the user selects, suggest a story title and point them
to `$create-stories [epic-slug]` or `$quick-design` depending on the size of the gap.

### --summary mode

Print the Gap Table and Summary directly to conversation. Do not write a file.
End with: "You can choose to save the full report to
`docs/content-audit-[date].md`."

---

## Phase 5 — Next Steps

After the audit, recommend the highest-value follow-up actions:

- If a content area is `UNSPECIFIED` → run `$design-system [name]` to define a
  count/list.
- If a numeric row is `NOT STARTED` and its specification already exists → point
  to the existing stories/planning path; do not ask design-system to add a count
  that is already present.
- Planning support (`$create-stories`, `$sprint-plan`) is installed; hand off scoped resource-preparation outcomes without turning created outputs into prerequisites or priority into readiness.
- If backlog stories are needed → "Run `$create-stories [epic-slug]` for each HIGH PRIORITY gap."
- If `--summary` was used → "Choose whether to save the full report to
  `docs/content-audit-[date].md`."

**Verdict (exactly one):**
- **MISSING CRITICAL CONTENT** — a missing/format-invalid item is explicitly
  critical in the GDD or blocks an MVP/Vertical Slice path.
- **GAPS FOUND** — any non-critical missing name, numeric gap, format issue, or
  UNSPECIFIED design gap exists.
- **COMPLETE** — every auditable named/numeric item is present in the required
  format for the selected audit scope and no required UNSPECIFIED/NOT ASSESSED item remains.
- **NOT ASSESSED** — required evidence is unavailable and no demonstrated content gap establishes either gap verdict. Preserve known failures even with partial coverage.
