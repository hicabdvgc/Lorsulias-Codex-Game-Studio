# Staged Resource and Code Observation

validate-commit.sh blocks invalid staged JSON under this studio's res_lib/ and assets/data/. It observes candidate numeric gameplay values in staged src/gameplay content, requiring explicit review against applicable contracts. It does not enforce a universal TODO owner format, source layout, schema or test coverage policy.

These are Codex PreToolUse handlers matching Bash, not Git-installed hooks. Input is one JSON object
with tool_name Bash, tool_input.command text and cwd. The shared Bash helper selects working Python;
git-command-check.py inspects supported literal `git [-C directory ...] commit|push` forms without
executing the supplied command. Commit messages/file flags and ordinary index commits are supported;
-a/-i/-o, pathspec or unknown flags, chained commands, expansions and wrappers remain explicitly unassessed.
Paths with spaces/apostrophes use the established Windows launcher and structured subprocess argv.
Inherited Git directory, worktree, index or object-store overrides leave the context NOT ASSESSED;
the observer does not strip them and report checks against a different repository or index.
Git is required for repository inspection. Missing/malformed inputs, runtime or Git errors produce
NOT ASSESSED (exit 1); an observed invalid staged JSON or supported forbidden force push exits 2.
Irrelevant events return 0 with no output. Observations use PreToolUse additionalContext JSON.
This bounded parser is not a complete command-policy enforcement boundary. Existing command safety
remains registered independently. No test suite, Git merge hook or SessionStart handler is installed here.

Interface verified against [official Codex hooks](https://learn.chatgpt.com/docs/hooks) on 2026-10-08.
Direct script execution and native client dispatch must be reported separately.
