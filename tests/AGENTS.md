# Test directory guidance

Read root instructions and `.codex/docs/work-preparation.md`. This skeleton is a
guidance location; it does not choose a game test root or runner. Resolve actual
project/module/package roots through `docs/technical-preferences.md` and
`.codex/docs/code-root-resolution.md` before dependent writes.

Use the selected language and runner conventions, real production interfaces and
existing patterns. Verify engine APIs against the installed version. Test meaningful
outcomes and relevant regressions, including resource relationships, tool workflows
and FRAMEWORK integration. Avoid tests that merely reproduce implementation or
fixed coverage quotas. Isolate fixtures and restore changed state; document genuine
external dependencies and nondeterminism rather than disguising them as unit tests.

Map every applicable criterion to feasible methods. Automation, inspection, manual,
engine and human evaluation can complement one another. Existing test files and
planned protocols are not execution evidence. Record actual revision, inputs,
commands/methods, results, limitations and reviewers. Required independent review
and human evaluation remain pending until performed. Manual records belong under
`production/qa/evidence/`; automated outputs use the selected runner's locations.
Do not change story status or declare game validity from infrastructure scaffolding.
