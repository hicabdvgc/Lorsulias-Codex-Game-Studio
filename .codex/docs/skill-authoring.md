# Skill and Gate Authoring

Adapted from Claude Code Game Studios' skill-authoring guidance for the installed
Codex capabilities. Apply when writing skills, persona instructions, or checks.

1. Define the intended outcome, actual inputs, output form, and affected handoff.
   Separate prerequisites from outputs the task creates. Avoid universal policies
   inferred from an example, role title, or optional source configuration.
2. A gating result needs an explicit NOT ASSESSED (or equivalent) outcome for
   unavailable evidence. State the reason and affected check. Preserve known
   failures when other checks cannot run. A required unassessed check cannot pass.
3. Explain skipped/inapplicable work in the result. Absence of evidence or an
   unset configuration key must not silently choose a passing branch. Identify
   the producer of every field a decision depends on.
4. Source external technical claims when relevant. A reference gap stays visible
   in both the findings and the verdict. Never invent APIs or execution evidence.
5. Discover the actual coverage set when it is well-defined. When scope is selected
   manually, name it and the reason; do not represent it as exhaustive coverage.
6. Test meaningful outcomes and handoffs with representative inputs. Observe a
   failing example where a guard matters, using isolated fixtures. Do not damage
   working project files to manufacture a test. Record execution and walkthroughs separately.

Keep actionable instructions and supported Codex metadata. Preserve useful source
behavior; remove rules unrelated to the actual outcome. Follow bounded task
authorization and [review boundaries](review-workflow.md). Use the
[contract template](templates/SKILL-CONTRACT-TEMPLATE.md) only when a concrete
handoff needs an explicit contract. [Recovery](error-recovery-protocol.md) applies
to incomplete work; these documents do not supply an automated test runner.
