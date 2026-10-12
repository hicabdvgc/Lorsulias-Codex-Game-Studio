---
name: consistency-check
description: "Compare shared facts across scoped GDDs and available entity records; distinguish contradictions, stale registries and missing coverage. Supports full, evidence-based incremental and identity-specific checks."
---

Read `.codex/docs/resource-preparation.md` for resource locations, shared write,
review/evidence and recovery requirements. Its shared handoff rules apply here;
initial design can record future resource needs before type contracts exist.

## Invocation and execution

Invoke this workflow as `$consistency-check`.

Use existing authorization for the bounded task. Describe the intended outputs and preserve unrelated work. Ask only about unresolved consequential choices or material scope expansion; do not repeat file- or section-level approval prompts.

Arguments: `[full | since-last-review | entity:<name> | item:<name>]`. Treat bracketed values as optional unless the workflow says otherwise.


# Consistency Check

Compare current owning and consuming documents, using `design/registry/entities.yaml`
when available to locate shared identities. Start with targeted searches and read
enough context to compare semantics, units and authority. Document comparisons
remain possible without a registry; identity-specific checks need resolvable entries.
Missing coverage, stale records and conflicting current facts are separate findings.

**When to run:**
- After writing each new GDD (before moving to the next system)
- Before `$review-all-gdds` (so that skill starts with a clean baseline)
- Before `$create-architecture` (inconsistencies poison downstream ADRs)
- On demand: `$consistency-check entity:[name]` to check one entity specifically

**Output:** Read-only conflict report. An optional saved copy uses
`design/consistency-report-[date].md` and is written when the task explicitly authorizes that bounded save. Existing save authorization carries through.

---

## Phase 1: Parse Arguments and Load Registry

**Modes:**
- No argument / `full` — compare scoped GDDs and available registered entries
- `since-last-review` — compare changed scope using an identifiable baseline and reliable change evidence, otherwise fall back to full
- `entity:<name>` — check one specific entity across all GDDs
- `item:<name>` — check one specific item across all GDDs

Validate exactly one mode or selector before loading the registry. `entity:` and
`item:` require a non-empty name and cannot be combined with another mode.
Resolve selector names under the project's existing case rules; empty,
malformed, unknown, or ambiguous selectors stop with candidate evidence and no
verdict.

**Load the registry:**

```
Read `design/registry/entities.yaml` in full.
```

If the file does not exist or has no entries, report that registry comparisons
are unavailable, initialize the four lookup tables as empty, and continue with
the cross-GDD formula, ownership, and dependency checks in Phase 3. Registry
absence is not a reason to skip GDD consistency analysis.

Build four lookup tables from the registry:
- **entity_map**: `{ name → { source, attributes, referenced_by } }`
- **item_map**: `{ name → { source, selected attributes, ... } }`
- **formula_map**: `{ name → { source, variables, output_range } }`
- **constant_map**: `{ name → { source, value, unit } }`

Parse YAML strictly. Duplicate keys, malformed records, or non-mapping entries
are reported with their location and stop registry-backed comparison; never
silently discard an entry or build partial lookup tables. A selector that needs
an invalid registry stops without a verdict. A full scan may continue its
cross-GDD checks only while clearly marking registry comparison unavailable.

Count total registered entries. Report:
```
Registry loaded: [N] entities, [N] items, [N] formulas, [N] constants
Scope: [full | since-last-review | entity:name | item:name]
```

---

## Phase 2: Locate In-Scope GDDs

```
Search for files matching `design/gdd/*.md`.
```

Exclude: `CONCEPT.md`, `BREAKDOWN.md`, `game-pillars.md`, prior review reports and other catalog/context documents — these are
not system GDDs.

For `since-last-review` mode:
Use an explicitly identified reviewed snapshot/commit or supplied before/after artifacts.
A saved report can identify that snapshot; its date or first save commit alone does
not prove what was reviewed. Include directly affected systems and dependencies. Include
both committed changes after that anchor and current working-tree modifications.
Supplied before/after snapshots can establish the baseline and changed scope without
Git. If neither those snapshots nor usable Git evidence identifies the reviewed
baseline and changes, explain the limitation and fall back to `full`. Never infer
a review baseline from filesystem dates or return an incremental PASS from an unanchored scan.

If no in-scope system GDD exists, stop with a clear error. Do not produce a
verdict and do not write a report.

Report the in-scope GDD list before scanning.

---

## Phase 3: Search-First Conflict Scan

For every in-scope GDD, first read its Summary or Overview, Dependencies,
Formulas, and the sections that declare entity/system ownership. This baseline
scan is mandatory even when the registry is empty and must check all four
existing consistency classes: registry values (when available), formulas,
ownership, and dependency targets. Search-first remains an optimization for
locating registered names; it must not exclude unregistered formulas, competing
owners, or missing explicit dependencies.

For each registered entry, search every in-scope GDD for the literal escaped
entry name. On a hit, read the complete containing Markdown section so that
table headers, units, formulas, and values remain together; three context lines
are not sufficient evidence. Expand beyond these sections only when a possible
conflict needs investigation.

Treat registry names as escaped literal text, never as regular expressions.
Require token/Markdown boundaries under the project's existing case rules.
Substring-only hits and names that cannot be located uniquely are
**UNVERIFIABLE**, not comparable values.

### 3a: Entity Scan

For each entity in entity_map:

```
Search files matching `design/gdd/*.md` for the literal bounded
`[entity_name]`, then read the complete containing Markdown section.
```

For each GDD hit, extract the values mentioned near the entity name:
- any numeric attributes (counts, costs, durations, ranges, rates)
- any categorical attributes (types, tiers, categories)
- any derived values (totals, outputs, results)
- any other attributes registered in entity_map

Compare extracted values against the registry entry.

**Conflict detection:**
- Registry says `[entity_name].[attribute] = [value_A]`. GDD says `[entity_name] has [value_B]`. → **CONFLICT**
- Registry says `[item_name].[attribute] = [value_A]`. GDD says `[item_name] is [value_B]`. → **CONFLICT**
- GDD mentions `[entity_name]` but doesn't specify the attribute. → **NOTE** (no conflict, just unverifiable)

### 3b: Item Scan

For each item in item_map, search all GDDs for the item name. Extract:
- The attributes actually declared for that item, their units, reference identity and scope

Compare against registry entry values.

### 3c: Formula Scan

For each formula in formula_map, search all GDDs for the formula name. Extract:
- variable names mentioned near the formula
- output range or cap values mentioned

Compare against registry entry:
- Different variable names → compare definitions and units; a renamed equivalent variable is not itself a conflict
- Output range stated differently → **CONFLICT**

### 3d: Constant Scan

For each constant in constant_map, search all GDDs for the constant name. Extract:
- Any numeric value mentioned near the constant name

Compare against registry value:
- Different number → **CONFLICT**

### 3e: Dependency Scan

Read every in-scope `Dependencies` section. Resolve each explicit target via
`BREAKDOWN.md`, or through a unique GDD filename/title when the index is
unavailable. A target with no corresponding GDD is a **Dependency Gap** finding
that names the source GDD and missing target with MEDIUM severity. Ambiguous
targets are UNVERIFIABLE and list all candidates; never guess.

---

## Phase 4: Deep Investigation (Conflicts Only)

For each conflict found in Phase 3, do a targeted full-section read of the
conflicting GDD to get precise context:

```
Read the complete conflicting section in `design/gdd/[conflicting_gdd].md`.
```
(Or search with wider context if the file is large)

Confirm the conflict with full context. Determine:
1. Compare the registry `source:` GDD's current text, the registry value, and
   relevant Git changes. `source:` is ownership evidence, not unconditional
   proof that its current value is correct.
2. When source text and registry disagree, show both with available history. If
   evidence cannot establish intent, report the conflict and ask the user to
   decide; never choose a winner automatically.
3. **Is this a genuine design change?** If the conflict represents an intentional
   design decision, the resolution is: update the source GDD, update the registry,
   then fix all other GDDs.

For each conflict, classify:
- **🔴 CONFLICT** — same named entity/item/formula/constant with different values
  in different GDDs. Must resolve before architecture begins.
- **⚠️ STALE REGISTRY** — source GDD value changed but registry not updated.
  Registry needs updating; other GDDs may be correct already.
- **ℹ️ UNVERIFIABLE** — entity mentioned but no comparable attribute stated.
  Not a conflict; just noting the reference.

---

## Phase 5: Output Report

```
## Consistency Check Report
Date: [date]
Registry entries checked: [N entities, N items, N formulas, N constants]
GDDs scanned: [N] ([list names])

---

### Conflicts Found (must resolve before architecture)

🔴 [Entity/Item/Formula/Constant Name]
   Registry (source: [gdd]): [attribute] = [value]
   Conflict in [other_gdd].md: [attribute] = [different_value]
   → Resolution needed: [which doc to change and to what]

---

### Stale Registry Entries (registry behind the GDD)

⚠️ [Entry Name]
   Registry says: [value] (written [date])
   Source GDD now says: [new value]
   → Update registry entry to match source GDD, then check referenced_by docs.

---

### Unverifiable References (no conflict, informational)

ℹ️ [gdd].md mentions [entity_name] but states no comparable attributes.
   No conflict detected. No action required.

---

### Dependency Gaps

| Source GDD | Missing Target | Severity | Evidence |
|------------|----------------|----------|----------|
| [gdd] | [system] | MEDIUM | [Dependencies entry] |

### Clean Entries (no issues found)

✅ [N] registry entries verified across all GDDs with no conflicts.

---

Verdict: CONSISTENT | CONFLICTS FOUND | DEPENDENCY GAP | NOT ASSESSED
```

**Verdict (exactly one):**
- **CONFLICTS FOUND** — value, formula, or ownership conflict exists. This takes
  precedence when conflicts and dependency gaps coexist.
- **DEPENDENCY GAP** — no conflict exists, but an explicit dependency target has
  no corresponding GDD.
- **CONSISTENT** — registry values (when available), formulas, ownership, and
  dependencies were all checked with no issue. Required UNVERIFIABLE evidence
  prevents CONSISTENT.
- **NOT ASSESSED** — no demonstrated conflict/dependency gap takes precedence, but required evidence is unavailable. Identify missing registry coverage separately from document contradictions.

---

## Phase 6: Suggested Corrections and Optional Report

Remain read-only. List each proposed GDD or registry correction, its evidence,
and the exact existing field or section that would need a later edit. Do not
update the registry, create a failure log, or write session state.

When the task authorizes a saved report, write `design/consistency-report-[date].md`
within that scope and verify the saved content. Re-read an existing report and preserve
unrelated assessments; resolve a path collision before overwriting a different scope.
Otherwise return the report conversationally and offer a save. Do not cite an unwritten
path as an artifact.

## Phase 7: Closing

Do not append to `production/session-state/active.md` and do not claim a report
file exists unless Phase 6 saved it successfully.

Close with the result and relevant next activity. Existing authorization for a
report save carries through; further design or registry edits need their own task scope.

---

## Recovery / Reference

- **If CONSISTENT**: Run `$review-all-gdds` for holistic design-theory review, or
  `$create-architecture` when full BREAKDOWN, system designs, full FRAMEWORK and applicable technical choices support architecture.
- **If DEPENDENCY GAP**: Run `$design-system [missing-system]`, then re-run.
- **If CONFLICTS FOUND**: Fix the flagged GDDs, then re-run
  `$consistency-check` to confirm resolution.
- **If STALE REGISTRY**: Use the report's proposed correction in a separate
  explicitly authorized edit, then re-run to verify.
- Run `$consistency-check` after writing each new GDD to catch issues early,
  not at architecture time.
