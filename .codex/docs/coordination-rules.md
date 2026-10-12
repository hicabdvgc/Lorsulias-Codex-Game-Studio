# Coordination Rules

1. Assign work by relevant capability and availability. Mandatory tier traversal
   is removed. Keep the requested task, inputs, output form/path, and write boundary explicit.
2. Respect user decisions and existing task authorization. Ask about unresolved
   material choices; do not repeat answered questions or per-file approval requests.
3. Sequence dependent work after its required inputs. Independent work may proceed
   while another activity is blocked. Creating an artifact does not require that
   output to exist before the task starts.
4. Use delegation only when supported and authorized by the active environment.
   For concurrent writers, assign non-overlapping ownership in the shared checkout.
   Supply the context the recipient needs; do not assume a particular inheritance model.
5. Collect required results before the dependent handoff. Verify promised files and
   report unresolved work using [error recovery](error-recovery-protocol.md).
6. Surface cross-domain conflicts with their evidence and consequences. Seek the
   relevant available expertise and user decision; do not invent absent director approvals.
7. The task owner traces affected consumers when an interface changes. Producer
   coordination is optional. Update the authorized affected artifacts and disclose
   unresolved consumers. Consult the catalogs and handover for installed components and explicitly excluded machinery.
8. Preserve required independent review and human testing when changing executors.
   Review outcomes follow [review-workflow.md](review-workflow.md).

Git worktree integration is installed; follow [worktree workflow](worktree-workflow.md) and verify the exact combined revision. A separate chat or
worktree must not be assumed to exist or contacted without authorization.

Resource handoffs follow [resource preparation](resource-preparation.md); tool work follows [tool development](tool-development.md). Assign actual executors and preserve required human evaluation when a later specialist is unavailable.

Work preparation uses [work-preparation.md](work-preparation.md). Assign QA strategy and tool development to available qualified executors; qa-lead and tools-programmer are installed personas. Story status changes belong to their authorized authoring/execution task. Reviewers and read-only observers do not synchronize progress.


For release/incident/communication handoffs use [.codex/docs/release-and-operations.md](release-and-operations.md). Release evidence is candidate-specific; deployment and publication use existing explicit authorization. Continuity uses bounded checkpoints and actual lifecycle observations.
