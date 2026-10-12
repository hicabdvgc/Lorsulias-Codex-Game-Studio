---
name: tech-debt
description: "Track, categorize, and prioritize technical debt across the codebase. Scans for debt indicators, maintains a debt register, and recommends repayment scheduling."
---
Read `.codex/docs/work-preparation.md` for status authority, criterion-level evidence, applicable governance, authorization, concurrent writes and recovery.


## Invocation and execution

Invoke this workflow as `$tech-debt`.

Existing authorization carries through add, prioritize and explicitly requested saves. Scan and report are conversational by default. Clarify missing consequential decisions before dependent writes.

Arguments: `[scan|add|prioritize|report]`. Treat bracketed values as optional unless the workflow says otherwise.


## Phase 1: Parse Subcommand

Determine the mode from the argument:

- `scan` — Scan the codebase for tech debt indicators
- `add` — Add a new tech debt entry manually
- `prioritize` — Re-prioritize the existing debt register
- `report` — Generate a summary report of current debt status

If no subcommand is provided, output usage and stop. Verdict: **FAIL** — missing required subcommand.

If the argument is not exactly one of `scan`, `add`, `prioritize`, or `report`,
output the same usage and stop with **FAIL**. Do not treat unknown or extra
arguments as scan/report. All four modes use only `docs/tech-debt-register.md`.
If it is absent, scan/add may propose creating that existing register format in
their changeset; prioritize/report stop with a clear missing-register error and
do not output COMPLETE.

---

## Phase 2A: Scan Mode

Search only project-owned source, configuration, and test files. Exclude vendored
dependencies, generated files, build/cache/output directories, and this workflow's
own documentation. Search for debt indicators:

- `TODO` comments (count and categorize)
- `FIXME` comments (candidates that may be bugs rather than accepted debt)
- `HACK` comments (workarounds that need proper solutions)
- `@deprecated` markers
- Duplicated code blocks (similar patterns in multiple files)
- Complexity or coupling with demonstrated maintenance impact (candidate only)

Length, duplication, and marker matches are discovery signals, not automatic debt.
Before registration, state the concrete impact. Any candidate enters the register only
when supplied decisions establish consciously deferred/accepted work and explain WHY;
otherwise leave it as an unregistered bug/candidate.

Categorize each finding:

- **Architecture Debt**: Wrong abstractions, missing patterns, coupling issues
- **Code Quality Debt**: Duplication, complexity, naming, missing types
- **Test Debt**: Missing tests, flaky tests, untested edge cases
- **Documentation Debt**: Missing docs, outdated docs, undocumented APIs
- **Dependency Debt**: Outdated packages, deprecated APIs, version conflicts
- **Performance Debt**: Known slow paths, unoptimized queries, memory issues

Present the findings to the user.

Before appending, compare every candidate with `docs/tech-debt-register.md` by affected Files plus Description and, for code markers, the recorded marker location. If the same debt is already registered, report `already registered` in the session and do not append another TD row. If the original marker text or location changed, report that its state cannot be confirmed; do not infer resolution or create a replacement row automatically.

For a scan-only request, report candidates and existing matches without writing.
For an authorized save, register only supported accepted debt, preserve existing
rows and verify the saved output. Unsettled candidates remain in the report.
Verdict: **COMPLETE** for the requested scan/save; **PARTIAL** if scope is unassessed.
Resolve scan roots through `.codex/docs/code-root-resolution.md`; missing roots
cannot be treated as a clean scan.

---

## Phase 2B: Add Mode

Use supplied description, affected files, impact and WHY the work is consciously
deferred. Ask only for missing information needed to register it. Retain the
Architecture, Code Quality, Test, Documentation, Dependency and Performance Debt
categories. Normalize supported Impact to Low, Med, High or Critical. Effort uses
the project's S/M/L/XL scale when defined; otherwise record Unknown and do not
invent day ranges. Record WHY in Description or associated notes.

Derive the next unused ID from the current register, use the current date, set the
existing Sprint column to Backlog unless the user provides an existing sprint, and
calculate Priority by the Phase 2C Impact/Effort/ID rule. Present the complete new
entry to the user. Immediately before append, re-read the table; if the candidate
ID is now occupied, select the next unused ID rather than overwriting a row.

Re-read the register before the authorized edit; preserve concurrent additions, stable IDs, unknown columns and unrelated prose. Verify the saved changes.

Within the add request’s authorization, append the deduplicated entry. Verdict: **COMPLETE** — entry added to register.

If registration lacks a supplied deferral decision, report the missing decision and retain the candidate without registration.

---

## Phase 2C: Prioritize Mode

Read the debt register at `docs/tech-debt-register.md`.

Use only the fields already present in the register. Sort deterministically by Impact (`Critical` > `High` > `Med` > `Low`), then by lower Effort (`S` < `M` < `L` < `XL`), then by ID ascending. Explain this ranking policy. Keep Unknown or incomparable effort/impact explicitly unranked until resolved. Update the existing Priority cells to reflect that ordering; do not invent frequency values, numeric mappings, or new fields.

Re-sort only the existing table rows by this rule and recommend which items to include in the next sprint. Preserve every non-table paragraph, heading, comment, unknown column, and hand-written note except the existing header statistics that this mode explicitly updates.

Present the re-prioritized register to the user.

Re-read the register before the authorized edit; preserve concurrent additions, stable IDs, unknown columns and unrelated prose. Verify the saved changes.

Within the prioritize request’s authorization, write the scoped update. Verdict: **COMPLETE** — register re-prioritized and saved.

Unranked rows remain visible with their missing assessment; prioritization does not register new candidates or assign story readiness.

---

## Phase 2D: Report Mode

Read the debt register. Generate only statistics directly supported by its current columns:

- Total items by category
- Effort distribution (counts of S/M/L/XL)
- Impact distribution
- Count assigned to Backlog versus an explicitly named sprint
- Age hints only where Added/Sprint values are directly comparable

The register has no resolution status or prior-report baseline. Do not claim items-resolved counts or a growing/stable/shrinking trend. If age cannot be established from existing values, state `age unknown` rather than guessing.

Output the report conversationally by default. An explicit bounded report save
does not authorize register changes. Verdict: **COMPLETE** — debt report generated.

---

## Phase 3: Next Steps

- Run `$sprint-plan` to schedule high-priority debt items into the next sprint.
- Comparable saved observations may support a later trend analysis.

### Debt Register Format

```markdown
## Technical Debt Register
Last updated: [Date]
Total items: [N] | Effort distribution: S [N] / M [N] / L [N] / XL [N]

| ID | Category | Description | Files | Effort | Impact | Priority | Added | Sprint |
|----|----------|-------------|-------|--------|--------|----------|-------|--------|
| TD-001 | [Cat] | [Description] | [files] | [S/M/L/XL] | [Low/Med/High/Critical] | [Rank / Unranked] | [Date] | [Sprint to fix or "Backlog"] |
```

### Rules
- Tech debt is not inherently bad — it is a tool. The register tracks conscious decisions.
- Every debt entry must explain WHY it was accepted (deadline, prototype, missing info)
- Only rows with an existing, directly comparable sprint number can receive an "older than 3 sprints" hint. For date-only/Backlog/ambiguous values, report `age unknown` rather than guessing.
