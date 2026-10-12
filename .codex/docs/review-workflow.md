# Review Workflow

Identify the artifact/activity, relevant requirements, available evidence, and
input revision before reviewing. Use the relevant prompts in
[director-gates.md](director-gates.md); their role prefixes identify expertise,
not a mandatory studio hierarchy.

The current task/procedure states the review scope and whether independence is
required. Use a qualified available person/agent. Identify self-review explicitly;
if independence is required and unavailable, report NOT ASSESSED for that check.
Human play and usability observations must come from actual sessions.

Early design feedback uses available concept, breakdown, and preliminary framework
inputs. Later integration review uses the completed framework and resource contracts.
Do not require future output artifacts to review the work that creates them.

Report the reviewed scope/revision, actual reviewer, findings with evidence,
unassessed or inapplicable checks, verdict, and corrective action. A known failure
remains visible even if another check could not run. Missing required evidence
prevents a passing conclusion for the affected decision. A documented optional
check may be inapplicable without blocking independent work.

Return results in conversation by default, without editing the reviewed artifact,
writing review receipts, or changing status. A task authorized to save results
must identify the destination and writer; never assume conversation-only results
will be available to a later file reader. Receipt hashes and automatic review skipping
are not part of this review procedure. Incremental scope uses an identified reviewed
baseline and reliable change evidence, including supplied before/after snapshots
without Git. When those inputs are unavailable, use the skill's full-review fallback.
After relevant inputs change, recheck affected conclusions against the changed inputs.

Review-mode settings cannot waive workflow requirements. The vertical-slice hard
gate requires actual play, integration, and framework-operation evidence before
production. MVP/Alpha/Beta/Gold and release checks use project-defined criteria.

Readiness reviews assess genuine prerequisites and feasible criterion-level methods. They never modify story Status. Sprint YAML derives status from stories; a summary or priority is not review evidence. Final milestone definitions follow the vertical-slice hard gate. See [work-preparation.md](work-preparation.md) for drafts, status and evidence interfaces.
