---
name: perf-profile
description: Analyze supplied performance measurements or prepare a scoped capture
  plan, separating measured bottlenecks from inspection candidates.
---

# Perf Profile

Invoke as `$perf-profile`. Arguments: `[system-name | full | path/to/existing-profiler-data]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


A data path must identify an existing profiler/benchmark file. Without an argument use an explicitly
identified current capture, otherwise ask for scope and provide a capture checklist. Read selected
platform/hardware/build, engine/package version, relevant system and configured budgets. Unknown
budgets remain unknown; do not supply a default frame/memory target or choose an engine.

Inspect supported capture contents and identify CPU/GPU/frame-time, allocation/memory, loading,
I/O or network contributors where measured. Explain units, collection interval, workload, build
settings and sampling limitations. An unreadable or unsupported export yields unassessed metrics,
not invented timing. Source inspection may suggest candidate hot paths but cannot rank measured cost.

Compare prior evidence only for comparable hardware, workload, revision and capture conditions.
Record differences that invalidate a numerical delta. Prioritize optimizations by observed cost,
likely benefit, correctness risk and supplied effort estimates. Avoid promises of quantified gains
or fixed quick-win durations without evidence. Use performance-analyst and selected engine expertise
when applicable and authorized. Verify version-sensitive profiling instructions through official docs.

Return budgets versus measurements, measured hotspots, hypotheses, proposed actions and verification
needed. If no data exists, return a concrete capture protocol with no quantitative verdict. A fix
requires the existing request to cover it; after an authorized fix rerun comparable measurements and
relevant correctness checks. Saving a report is optional and bounded to the requested output.
