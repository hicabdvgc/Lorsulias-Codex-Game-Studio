---
name: security-audit
description: Assess the selected game security surface and evidence, with actionable
  findings and explicit unassessed coverage.
---

# Security Audit

Invoke as `$security-audit`. Arguments: `[full | network | save | input | quick]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Default to full over the actual available project scope; reject unknown modes. Read live roots,
selected online/offline/platform choices, data flows, accepted architecture, relevant obligations
and delivery checklist when supplied. No sources or unresolved roots prevent dependent scans.
Quick is a limited screen whose omissions remain explicit; it cannot establish a full audit.

Inspect applicable trust boundaries: save/serialization validation and tampering; authentication,
authority, replication and rate/resource limits for network features; malformed input/file paths;
secrets, logs and personal data; cheat threats where relevant; dependencies and supply chain.
Confirmed offline scope can make network checks N/A. Do not invent online requirements or
claim every game needs anti-cheat. Distinguish source inspection, reproducible evidence and
untested hypotheses. Redact discovered secrets and identify their locations without exposing values.
Use the security-engineer expertise within available tools and current delegation policy.

Classify findings CRITICAL/HIGH/MEDIUM/LOW with the actual threat, impact, preconditions, evidence,
remediation and verification needed. Keep accepted risks linked to explicit decisions; the auditor
cannot accept them. Report scope, dependency evidence, limitations and re-audit triggers. Default
output is conversational; an authorized save uses production/security/security-audit-[scope]-[date].md.
No automatic code changes, exploit deployment or credentials/configuration changes follow an audit.
Final acceptance uses the project's RELEASE_CHECKLIST obligations. Missing required coverage cannot
support a passing readiness claim; there is no imposed universal severity threshold or release phase.
