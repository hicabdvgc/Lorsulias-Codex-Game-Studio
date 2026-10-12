# Economy Model: [System Name]

Complete the sections relevant to this design; identify omitted topics and their
reason when the reader would otherwise expect them. Examples are illustrative.
Use developer CONCEPT, applicable GDD/FRAMEWORK decisions and `docs/ACCESSIBILITY.md`.
Read live `docs/technical-preferences.md` for selected technical choices. Link resource
requirements to RES_TYPE/TYPE_TEMP when defined; record unresolved needs in early
design. This design document does not substitute for a resource schema or delivered
resource. Save and accept within actual task authorization and required evidence.

*Created: [Date]*
*Owner: [assigned responsibility]*
*Status: [Draft / Balanced / Live — record supporting analysis and runtime evidence separately]*

---

## Overview

[What resources, currencies, and exchange systems does this economy cover?
What player behaviors does it incentivize?]

---

## Currencies

| Currency | Type | Earn Rate | Sink Rate | Cap | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| [Selected resource/currency] | [Role] | [Amount/unit time] | [Amount/unit time] | [Selected cap/none] | [Use] |

### Currency Rules
- [Rule 1 — e.g., "Soft currency has no cap but inflation is controlled via sinks"]
- [Rule 2 — e.g., "Premium currency cannot be converted back to real money"]
- [Rule 3]

---

## Sources (Faucets)

| Source | Currency | Amount | Frequency | Conditions |
| ---- | ---- | ---- | ---- | ---- |
| [Source] | [Resource] | [Amount/unit] | [Frequency] | [Conditions] |

---

## Sinks (Drains)

| Sink | Currency | Cost | Frequency | Purpose |
| ---- | ---- | ---- | ---- | ---- |
| [Sink] | [Resource] | [Cost/unit] | [Frequency] | [Purpose] |

---

## Balance Targets

| Metric | Target | Rationale |
| ---- | ---- | ---- |
| [Metric] | [Selected target, unit and domain] | [Design rationale/evidence] |

---

## Progression Curves

### Level XP Requirements
| Level | XP Required | Cumulative XP | Estimated Time |
| ---- | ---- | ---- | ---- |
| 1→2 | [100] | [100] | [10 min] |
| 5→6 | [500] | [1,500] | [2 hrs] |
| 10→11 | [1,500] | [7,500] | [8 hrs] |
| 20→21 | [5,000] | [50,000] | [40 hrs] |

*Formula*: `XP(n) = [formula, e.g., 100 * n^1.5]`

### Item Price Scaling
*Formula*: `Price(tier) = [formula, e.g., base_price * 2^(tier-1)]`

---

## Loot Tables

### [Drop Source Name]
| Item | Rarity | Drop Rate | Pity Timer | Notes |
| ---- | ---- | ---- | ---- | ---- |
| [Common item] | Common | [60%] | [N/A] | [Always useful, never feels bad] |
| [Uncommon item] | Uncommon | [25%] | [N/A] | [Noticeable upgrade] |
| [Rare item] | Rare | [12%] | [10 drops] | [Exciting, build-defining] |
| [Legendary item] | Legendary | [3%] | [30 drops] | [Game-changing, celebration moment] |

### Pity System
[If the selected design includes a pity system, define its distribution and reset behavior.]

---

## Economy Health Metrics

| Metric | Healthy Range | Warning Threshold | Action if Breached |
| ---- | ---- | ---- | ---- |
| [Metric] | [Selected range] | [Selected threshold] | [Investigation/action] |

---

## Ethical Guardrails

- [No pay-to-win: premium currency cannot buy gameplay power advantages]
- [Pity timers on all random drops: guaranteed outcome within X attempts]
- [Transparent drop rates displayed to players]
- [Spending limits for minor accounts]
- [No artificial scarcity pressure (FOMO timers) on essential items]

---

## Simulation Results

[Include results from economy simulations if available: player wealth
distribution over time, sink effectiveness, inflation rate, etc.]

---

## Dependencies

- Depends on: [combat balance, quest design, crafting system]
- Affects: [difficulty curve, player retention, monetization]
- Integration responsibilities: [available qualified executors and dependent decisions; live-ops/analytics roles are installed; evidence and actual tool access are still required]
