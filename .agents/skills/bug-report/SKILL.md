---
name: bug-report
description: Record reproducible game defects and verify or close identified bugs
  using actual evidence and stable IDs.
---

# Bug Report

Invoke as `$bug-report`. Arguments: `[description] | analyze [project-path] | verify [BUG-NNNN] | close [BUG-NNNN]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


## Report and analyze

Parse one mode and resolve its actual scope; missing IDs/paths or ambiguous matches require resolution.
Description mode records summary, observed versus expected behavior, reproduction steps/frequency,
revision/build, platform, inputs, evidence, suspected system and related work. Missing reproduction
facts stay explicit. Analyze mode inspects the resolved project and reports candidate defects; static
suspicions are not observed runtime failures. Do not invent test sessions, logs or causes.

Use severity S1-Critical / S2-Major / S3-Minor / S4-Trivial and priority P1-Immediate /
P2-Next Sprint / P3-Backlog / P4-Wishlist, keeping impact separate from proposed urgency.
These compatibility labels do not impose a sprint schedule or authorization to interrupt work.
Read production/qa/bugs/ and supported existing consolidated records for duplicates. Before saving,
re-read the identity set, select the next unused BUG-NNNN and preserve concurrent additions. Use
production/qa/bugs/BUG-NNNN-[slug].md with one authoritative header Status: Open. Existing matching
bugs receive bounded updates instead of new identities. Record hypotheses explicitly.

## Verify and close

For verify, read the exact bug and reproduce its original steps on the identified fixed revision
using an appropriate automated, engine, manual or human method. Inspect expected behavior and affected
regressions. Record actual command/protocol, result, build and evaluator. Success changes Open to
Verified Fixed; failure keeps/returns it Open with observed failure. Unavailable verification records
the limitation and preserves status. Never invent a QA tester or infer success from a fix commit.

For close, require Verified Fixed and applicable verification still covering the delivery. Carry
existing closure authorization. Update the actual header from Verified Fixed to Closed and maintain
one closure record; do not search for an Open-only replacement. Repeated closure remains idempotent.
A newly observed regression needs explicit reopening or a linked report, preserving historical evidence.

Read back requested saves. Report actual classification/status and next activity. A report does not
fix code, accept a risk, alter story progress or launch a release. `$hotfix` is installed;
use its bounded implementation/release-evidence route when emergency work is requested.
