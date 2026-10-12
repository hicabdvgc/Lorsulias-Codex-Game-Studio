---
name: regression-suite
description: Maintain or assess the mapping of critical paths and verified bug fixes
  to actual regression tests and protocols.
---

# Regression Suite

Invoke as `$regression-suite`. Arguments: `[update | audit | report]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Resolve the requested mode; use update when explicitly requested by context, otherwise clarify.
Load tests/regression-suite.md if present, actual configured test roots/commands, relevant GDD and
FRAMEWORK critical paths, resource/tool requirements and bug reports. Missing/unreadable scope is
an assessment gap. A legitimately empty inventory is distinguishable from failed discovery.

Map criterion/critical-path identities to real test assertions or manual protocols; verify the
reference rather than guessing coverage by filename. For Verified Fixed/Closed bugs, connect the
original reproduction to a relevant regression check where feasible; explain manual alternatives
and outstanding gaps. Do not silently use Open bugs as verified fixes. Detect renamed/missing tests,
orphan candidates, changed requirements and stale quarantine decisions. Preserve stable identities.

Report critical-path and bug coverage, drift, proposed tests/protocols and limitations. Use **COVERED / PARTIAL / MISSING / EXEMPT** per mapping; EXEMPT requires a justified inapplicable method and cannot waive a required manual/human check. Summarize **GAPS / CRITICAL GAPS / NOT ASSESSED** where warranted. Mapping
coverage does not prove execution. Report mode summarizes existing registrations and limitations;
audit compares them with current requirements; update performs that analysis and maintains the manifest.

In update mode, re-read and preserve the manifest's How to run, registered tests by system, known gaps
and quarantined tests, including concurrent/unrelated entries. Describe actual runner locations even
though the studio manifest remains under tests/. Audit/report are conversational by default; an
explicit report save is bounded. This skill inventories and plans: it does not run the suite, implement
missing tests, disable quarantined tests or change work status. Verify promised manifest saves.
