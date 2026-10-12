---
name: balance-check
description: "Analyzes game balance data files, formulas, and configuration to identify outliers, broken progressions, degenerate strategies, and economy imbalances. Use after modifying any balance-related data or design. Use when user says 'balance report', 'check game balance', 'run a balance check'."
---

Read `.codex/docs/resource-preparation.md` for resource locations, shared write,
review/evidence and recovery requirements. Its shared handoff rules apply here;
initial design can record future resource needs before type contracts exist.

## Invocation and execution

Invoke this workflow as `$balance-check`.

Use existing authorization for the bounded task. Describe the intended outputs and preserve unrelated work. Ask only about unresolved consequential choices or material scope expansion; do not repeat file- or section-level approval prompts.

Arguments: `[system-name|path-to-data-file]`. Treat bracketed values as optional unless the workflow says otherwise.

Use an available qualified `economy-designer` for an applicable economy or loot analysis when delegation is authorized. Combat, Progression,
and any other resolved system stay with the current reviewer unless their actual
data includes an economy/loot subdomain.


## Phase 1: Identify Balance Domain

Determine the balance domain from the first provided argument:

- **Combat** → weapon/ability DPS, time-to-kill, damage type interactions
- **Economy** → resource faucets/sinks, acquisition rates, item pricing
- **Progression** → XP/power curves, dead zones, power spikes
- **Loot** → rarity distribution, pity timers, inventory pressure
- **File path given** → accept exactly one existing project-local supported text
  data file, not a directory, generated/binary file, or external path; otherwise
  stop without a verdict
- **Other system name** → resolve it against `BREAKDOWN.md` and existing GDD
  names. If zero or multiple systems match, ask the user to select rather than
  guessing a domain.

If no argument, ask the user which system to check. Reject unknown flags and
ambiguous multi-target inputs.

---

## Phase 2: Read Data Files

Start from the resolved target GDD. Read only data files it explicitly references,
existing same-system data/balance files, and their direct declared dependencies.
Do not expand `relevant files` to unrelated domain data. List every selected file
and the reason it is in scope in Data Sources. Missing, empty, unreadable, or
malformed inputs remain explicit evidence gaps.

---

## Phase 3: Read Design Document

Read the resolved GDD to obtain formulas, variable definitions, units, intended
ranges, and tuning knobs. If any required baseline is absent, mark the affected
check `NOT EVALUATED` with the missing source; do not invent a generic threshold.
A run containing an unevaluated applicable check cannot receive BALANCED.

---

## Phase 4: Perform Analysis

Before each calculation, validate the input domain: denominators must be nonzero;
probabilities must be within range and use an explicitly stated normalization;
units and time bases must agree; values requiring nonnegative inputs must reject
negative values; cyclic formula dependencies must be reported; stochastic claims
must include a sufficient stated distribution/sample basis. For invalid inputs,
name the exact file/field, mark only that calculation `NOT EVALUATED`, and continue
independent checks.

Run only domain checks relevant to the documented mechanics. Calculated projections are not observed player behavior; qualitative pacing and strategy claims need actual human/play evidence when required:

**Combat balance:**
- Calculate DPS for all weapons/abilities at each power tier
- Check time-to-kill at each tier
- Identify any options that dominate all others (strictly better)
- Check if defensive options can create unkillable states
- Verify damage type/resistance interactions are balanced

**Economy balance:**
- Map all resource faucets and sinks with flow rates
- Project resource accumulation over time
- Check for infinite resource loops
- Compare selected resource sinks with their documented generation model
- Check if any items are never worth purchasing

**Progression balance:**
- Plot the XP curve and power curve
- Check for dead zones (no meaningful progression for too long)
- Check for power spikes (sudden jumps in capability)
- Verify content gates align with expected player power
- Check if skip/grind strategies break intended pacing

**Loot balance:**
- Calculate expected time to acquire each rarity tier
- Check pity timer math
- Verify no loot is strictly useless at any stage
- Check inventory pressure vs acquisition rate

---

## Phase 5: Output the Analysis

```
## Balance Check: [System Name]

### Data Sources Analyzed
- [List of files read]

### Verdict: [BALANCED / CONCERNS / OUT OF BALANCE]

- BALANCED: every applicable calculation is supported by a design baseline and no material deviation is found.
- CONCERNS: one or more non-blocking deviations or unevaluated items require review.
- OUT OF BALANCE: at least one critical deviation or degenerate strategy is supported by the cited formula and values.

### Findings
| Value | Formula or Source | Expected | Actual | Deviation | Severity |
|-------|-------------------|----------|--------|-----------|----------|

For `NOT EVALUATED`, put the missing/invalid baseline reason in Formula or Source
and do not fabricate Expected, Actual, or Deviation values.

### Degenerate Strategies Found
- [Strategy description and why it is problematic]

### Progression Analysis
[Graph description or table showing progression curve health]

### Recommendations
| Priority | Issue | Suggested Fix | Impact |
|----------|-------|--------------|--------|

### Values That Need Attention
[Specific values with suggested adjustments and rationale]
```

---

## Phase 6: Fix & Verify Cycle

If the original request already authorizes a bounded fix or report save, perform that work. Otherwise offer the applicable choices after presenting the report:
- Prompt: "Balance check complete. What would you like to do next?"
- Options:
  - `[A] Fix highest-priority issue now — walk me through it`
  - `[B] Save report to design/balance/balance-check-[system]-[date].md`
  - `[C] Stop here — I'll review the findings manually`

If [A]:
- Ask which issue to address first (refer to the Recommendations table by priority row)
- Show the current value, proposed value, exact target file, and the complete
  resulting edit for every affected data, formula, GDD, or ADR file. Use existing bounded authorization; clarify a consequential unresolved adjustment before changing it. If another file is
  discovered afterward, stop and present a revised complete changeset instead of
  editing outside the approved boundary.
- After authorization, apply only the previewed edits.
- After each fix, re-run the affected calculations and checks and inspect for regressions
- If the fix changes a tuning knob defined in a GDD or referenced by an ADR, remind the user:
  > "This value is defined in a design document. After the approved GDD edit has actually been written, identify affected FRAMEWORK/GDD/resource consumers; use installed `$propagate-design-change`. Do not propagate a proposed value that is not yet in the document."

If [B]:
- Write the report to `design/balance/balance-check-[system]-[date].md` (create the directory if needed). Use the current date for [date] in YYYY-MM-DD format.
- Confirm the file was written, then end with: "Re-run `$balance-check` after fixes to verify."

If [C]:
- Summarize open issues and end with: "Re-run `$balance-check` after fixes to verify."
