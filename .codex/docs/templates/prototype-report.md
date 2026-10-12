# Concept Prototype Report: [Concept Name]

> **Date**: [YYYY-MM-DD]
> **Prototype Path**: [HTML / Engine / Paper]
> **Concept File**: design/gdd/CONCEPT.md (if exists)

---

## Hypothesis

[The falsifiable hypothesis this prototype set out to test:
"If the player [does X], they will feel [Y] — evidenced by [measurable signal Z]."]

---

## Riskiest Assumption Tested

[What was identified as the biggest risk in the concept, and whether it proved out.]

---

## Approach

[What was built, how long it took, what shortcuts were taken deliberately.]

**Experiment kind:** [Concept experiment / Technical spike]
**Path chosen:** [HTML / Engine / Paper]
**Duration/checkpoint selected:** [actual constraint or undecided]
**Reason for path:** [Why this path was appropriate for this hypothesis]

**Shortcuts taken (intentional):**
- [e.g., hardcoded values, placeholder art, no menus, etc.]

---

## Result

[What actually happened — specific observations, not opinions. Quote playtesters
directly where possible.]

---

## Metrics

| Metric | Value |
|--------|-------|
| Path used | [HTML / Engine / Paper] |
| Iterations to playable | [N — Engine path only; N/A otherwise] |
| Prototype duration | [e.g., 4 hours] |
| Playtesters | [N internal / N external] |
| Feel assessment | [Specific — "response felt sluggish at 200ms" not "felt bad"] |
| Hypothesis verdict | [CONFIRMED / PARTIALLY CONFIRMED / REFUTED / NOT ASSESSED] |

---

## Recommendation: [PROCEED / PIVOT / KILL / NOT ASSESSED]

[One paragraph explaining the recommendation with evidence from the result above.]

---

## If Proceeding

[What the prototype revealed that should directly inform GDD writing:]

- **Core tuning values discovered:** [e.g., "jump height of 3.5 units felt best"]
- **Assumptions confirmed:** [What the concept doc assumed that proved true]
- **Assumptions disproved:** [What the concept doc assumed that proved wrong]
- **Emergent mechanics:** [Behaviors that appeared during testing worth formalizing]

> Note: If HTML path was used and feel is uncertain, consider an engine prototype
> targeting feel specifically before committing to GDDs.

**Next steps:** Record the lesson for the relevant design/framework activity.
The developer incorporates chosen concept changes manually. An experiment does
not replace the vertical-slice hard gate or require advancing the workflow.

---

## If Pivoting

[What alternative direction the results suggest — what felt almost right and what
to adjust. Be specific about what to change, not just that something needs changing.]

**Pivot direction:** [What to try differently]
**What to keep:** [What worked and should be preserved]
**Next step:** `$prototype [revised-concept]`

---

## If Killing

[Why this concept does not work — what specific signal led to this verdict.
This report is the deliverable; no further action needed on this concept.]

**Next step:** `$brainstorm [new-direction]`

---

## Lessons Learned

- **What assumptions were broken by actually building this?**
  [...]

- **What surprised us that didn't show up in the brainstorm?**
  [...]

- **What would we test differently next time?**
  [...]

---

> *Prototype code location: `prototypes/[concept-name]-concept/`*
> *Retention decision: [retain / revise / archive / remove / undecided], with reasons.*
> *Reuse requires checking the applicable production contracts and actual evidence.*

## Evidence Boundaries

[Separate executed checks, human session observations, and simulated paper
walkthroughs. Missing human evidence leaves feel conclusions NOT ASSESSED.]
