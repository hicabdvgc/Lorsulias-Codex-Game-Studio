# Skill Quality Rubric

Evaluate each applicable metric against the requested outcome. For category mode,
the evidence is the written instructions; actual scenario execution is a separate
evidence type. Report PASS, WARN (partial), FAIL (contradiction/known omission),
NOT ASSESSED (unavailable evidence), or NOT APPLICABLE with a scope reason.
Known failures take precedence, then required unassessed checks, then warnings.
Do not grade heading counts, agent counts, fixed cadence, or unspecified formats.

## Skill Categories

### `gate`

| Metric | Required outcome |
|---|---|
| G1 | Derives applicable criteria from the workflow and selected decision. |
| G2 | Required checks survive changes of executor or optional review intensity. |
| G3 | Verdicts distinguish failure, unavailable evidence, and passing results. |
| G4 | Progression depends on outcome evidence, including the slice hard gate and required human tests. |
| G5 | Status writes require authorization and the relevant completion evidence. |

### `authoring`

| Metric | Required outcome |
|---|---|
| A1 | Uses the applicable existing template or agreed output contract. |
| A2 | Uses settled decisions and asks about material unknowns. |
| A3 | Preserves unrelated content when revising an existing artifact. |
| A4 | Supplies the actual information needed by its consumer at this stage. |
| A5 | Saves authorized partial work clearly when incremental authoring is useful. |

### `review`

| Metric | Required outcome |
|---|---|
| R1 | States supported target and relevant review scope. |
| R2 | Findings identify observable evidence and reviewed revision. |
| R3 | Verdict distinguishes blocking issues, concerns, and unavailable evidence. |
| R4 | Incomplete required coverage cannot pass. |
| R5 | Returns corrective actions without silently rewriting or approving the target. |

### `readiness`

| Metric | Required outcome |
|---|---|
| RD1 | Evaluates genuine prerequisites and the specified result. |
| RD2 | Separates future outputs from required pickup inputs. |
| RD3 | Defines a feasible completion evaluation, including human judgment when relevant. |
| RD4 | Reports specific missing decisions/evidence. |
| RD5 | Hands off a supported status with its reasons. |

### `pipeline`

| Metric | Required outcome |
|---|---|
| P1 | Produces the agreed output format for the next consumer. |
| P2 | Orders work by actual dependencies. |
| P3 | Honors bounded authorization and preserves unrelated content. |
| P4 | Preserves applicable review and evidence obligations. |
| P5 | Uses current governing inputs and checks promised results. |

### `analysis`

| Metric | Required outcome |
|---|---|
| AN1 | Inspects evidence without changing source facts during analysis. |
| AN2 | Presents traceable findings in a form useful for the requested decision. |
| AN3 | Saves results only within an authorized writing task. |
| AN4 | Separates supported conclusions from missing evidence and proposals. |

### `team`

| Metric | Required outcome |
|---|---|
| T1 | Assigns explicit responsibilities and output boundaries to available executors. |
| T2 | Sequences dependencies and permits parallel work only when independent and authorized. |
| T3 | Surfaces failed/missing required results. |
| T4 | Verifies required handoffs before consuming them. |
| T5 | Requests genuinely missing inputs without fabricating them. |

### `sprint`

| Metric | Required outcome |
|---|---|
| SP1 | Uses the actual requested planning period, milestone, or release evidence. |
| SP2 | Avoids imposed sprint duration, capacity, or optional reviewer requirements. |
| SP3 | Produces actionable plans/reports in their agreed form. |
| SP4 | Keeps recommendations distinct from authorized persisted changes. |

### `utility`

| Metric | Required outcome |
|---|---|
| U1 | Accepts the documented inputs and produces its stated useful outcome/format. |
| U2 | Handles missing evidence and inappropriate inputs explicitly. |
| U3 | Preserves read/write scope and current authorization. |
| U4 | References available capabilities and reports pending dependencies honestly. |

## Agent Categories

Category labels preserve source catalog organization; they impose no hierarchy.

### `director`

| Metric | Required outcome |
|---|---|
| D1 | Uses the selected gate vocabulary, including unavailable evidence. |
| D2 | Stays within its assigned domain and decision authority. |
| D3 | Surfaces tradeoffs to the actual decision owner. |
| D4 | Inherits active runtime settings and uses supplied evidence. |

### `lead`

| Metric | Required outcome |
|---|---|
| L1 | Returns the requested domain assessment/output. |
| L2 | Preserves scope and routes unresolved cross-domain decisions appropriately. |
| L3 | Inherits runtime capabilities without assuming tool grants. |

### `specialist`

| Metric | Required outcome |
|---|---|
| S1 | Produces the assigned domain result. |
| S2 | Preserves cross-domain decisions and dependencies. |
| S3 | Identifies needed expertise or evidence when unavailable. |

### `engine`

| Metric | Required outcome |
|---|---|
| E1 | Uses verified selected-version API evidence. |
| E2 | Applies relevant engine/language knowledge to the actual task. |
| E3 | Reports unsupported claims and preserves interface requirements. |

### `qa`

| Metric | Required outcome |
|---|---|
| Q1 | Produces the requested test findings, cases, or evidence. |
| Q2 | Distinguishes planned checks from actual observations. |
| Q3 | Evaluates the specified outcome without adding product features. |

### `operations`

| Metric | Required outcome |
|---|---|
| O1 | Describes the actual operational responsibilities and outputs. |
| O2 | Works within assigned boundaries with available expertise. |
| O3 | Claims only capabilities and evidence actually available. |
