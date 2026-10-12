# Staged Design Observation

For an ordinary supported git commit, validate-commit.sh observes headings in staged design/gdd Markdown blobs. It uses the Git index, including renamed paths, and ignores deleted files. Headings do not prove applicable content, maturity or independent review. Use design-review/review-all-gdds with the actual intended scope for that assessment.

These are Codex PreToolUse handlers matching Bash, not Git-installed hooks. Input is one JSON object
with tool_name Bash, tool_input.command text and cwd. The shared Bash helper selects working Python;
git-command-check.py inspects supported literal `git [-C directory ...] commit|push` forms without
executing the supplied command. Commit messages/file flags and ordinary index commits are supported;
-a/-i/-o, pathspec or unknown flags, chained commands, expansions and wrappers remain explicitly unassessed.
Paths with spaces/apostrophes use the established Windows launcher and structured subprocess argv.
Git is required for repository inspection. Missing/malformed inputs, runtime or Git errors produce
NOT ASSESSED (exit 1); an observed invalid staged JSON or supported forbidden force push exits 2.
Irrelevant events return 0 with no output. Observations use PreToolUse additionalContext JSON.
This bounded parser is not a complete command-policy enforcement boundary. Existing command safety
remains registered independently. No test suite, Git merge hook or SessionStart handler is installed here.

Interface verified against [official Codex hooks](https://learn.chatgpt.com/docs/hooks) on 2026-10-08.
Direct script execution and native client dispatch must be reported separately.
