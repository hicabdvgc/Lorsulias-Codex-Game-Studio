"""Read-only checks of supported pending Git commands; command text is never executed."""
from pathlib import Path
import json
import os
import re
import shlex
import subprocess
import sys


def context(message):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                     "additionalContext": message}}, ensure_ascii=True))


def git(cwd, *args):
    env = os.environ.copy()
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0", GIT_NO_REPLACE_OBJECTS="1")
    result = subprocess.run(["git", "--no-optional-locks", "-c", "core.fsmonitor=false",
                             "-C", str(cwd), *args], capture_output=True, env=env, timeout=15)
    if result.returncode:
        raise ValueError(result.stderr.decode("utf-8", "replace").strip() or "Git inspection failed")
    return result.stdout


def inspect(mode, studio, event):
    if not isinstance(event, dict):
        raise ValueError("hook input must be a JSON object")
    if event.get("hook_event_name") not in (None, "PreToolUse") or event.get("tool_name") != "Bash":
        return
    payload = event.get("tool_input")
    command = payload.get("command") if isinstance(payload, dict) else None
    if not isinstance(command, str):
        raise ValueError("Bash tool_input.command must be text")
    # Preserve quoted Windows backslashes. This parser accepts a single literal Git
    # invocation; shell programs, expansion and chained commands stay unassessed.
    lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|<>()")
    lexer.whitespace_split = True
    lexer.commenters = ""
    lexer.escape = ""
    try:
        tokens = list(lexer)
    except ValueError as exc:
        raise ValueError("command cannot be parsed: " + str(exc)) from exc
    if not tokens:
        return
    looks_relevant = bool(re.search(r"\bgit(?:\.exe)?\b.*\b" + mode + r"\b", command, re.S))
    if tokens[0].lower() not in ("git", "git.exe"):
        if looks_relevant:
            context("NOT ASSESSED: embedded/chained Git command; use a single literal Git invocation for this observer.")
        return
    if any(t and all(c in ";&|<>()" for c in t) for t in tokens) or any(x in command for x in ("$", "`", "\n", "\r")):
        if looks_relevant:
            context("NOT ASSESSED: shell expansion or compound command; command text was not executed.")
        return
    raw_cwd = event.get("cwd")
    if not isinstance(raw_cwd, str) or not raw_cwd:
        raise ValueError("event cwd is required to resolve actual Git context")
    cwd = Path(raw_cwd).resolve()
    index = 1
    while index < len(tokens) and tokens[index] == "-C":
        if index + 1 >= len(tokens):
            raise ValueError("missing git -C directory")
        value = Path(tokens[index + 1])
        cwd = (cwd / value).resolve()
        index += 2
    if index >= len(tokens) or tokens[index] != mode:
        if looks_relevant:
            context("NOT ASSESSED: unsupported Git global options; no repository inspection performed.")
        return
    args = tokens[index + 1:]
    if mode == "push" and any(a in ("-f", "--force", "--force-with-lease") or a.startswith("--force-with-lease=") for a in args):
        print("BLOCKED: force-push variants are disabled by the existing project command policy.", file=sys.stderr)
        raise SystemExit(2)
    overrides = [key for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR",
                                "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES")
                 if key in os.environ]
    if overrides:
        raise ValueError("inherited Git context overrides require explicit assessment: " +
                         ", ".join(overrides) + "; no repository inspection performed")
    root = Path(git(cwd, "rev-parse", "--show-toplevel").decode("utf-8").strip()).resolve()
    if mode == "push":
        # No test runner, network access, branch-protection API or remote mutation.
        context("Push observation: literal arguments " + json.dumps(args) + ". Tests/build checks were NOT RUN. "
                "Check the intended remote/ref and actual project obligations; no protected branch names are assumed.")
        return
    # -a/-i/-o/pathspec commits can replace the index after this hook, so its
    # snapshot would not describe the commit. Other uncommon forms stay explicit.
    i = 0
    while i < len(args):
        arg = args[i]
        if arg in ("-m", "--message", "-F", "--file"):
            if i + 1 >= len(args):
                raise ValueError("missing commit message/file argument")
            i += 2
            continue
        if arg in ("--amend", "--no-edit", "--signoff", "-s", "--allow-empty") or arg.startswith(("--message=", "--file=", "-m")):
            i += 1
            continue
        context("NOT ASSESSED: commit option/pathspec may change staged scope or is unsupported: " + arg)
        return
    names = git(cwd, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z").split(b"\0")
    notes = []
    checked = 0
    for raw in filter(None, names):
        name = raw.decode("utf-8")
        path = (root / name).resolve()
        resource = any(path.is_relative_to((studio / p).resolve()) for p in ("res_lib", "assets/data"))
        design = path.is_relative_to((studio / "design/gdd").resolve()) and path.suffix.lower() == ".md"
        gameplay = path.is_relative_to((studio / "src/gameplay").resolve())
        if not ((resource and path.suffix.lower() == ".json") or design or gameplay):
            continue
        blob = git(cwd, "show", ":" + name)
        if resource and path.suffix.lower() == ".json":
            try:
                json.loads(blob, parse_constant=lambda value: (_ for _ in ()).throw(ValueError("non-JSON constant " + value)))
            except (ValueError, UnicodeError) as exc:
                print("BLOCKED: staged JSON is invalid: " + name + ": " + str(exc), file=sys.stderr)
                raise SystemExit(2)
            checked += 1
        if design:
            headings = re.findall(r"^#{1,6}\s+(.+)$", blob.decode("utf-8"), re.M)
            notes.append(name + ": staged headings observed: " + json.dumps(headings) + "; no completeness verdict.")
        if gameplay and re.search(rb"(damage|health|speed|rate|chance|cost|duration)\s*[:=]\s*[0-9]+", blob):
            notes.append(name + ": numeric gameplay-value candidate; inspect applicable resource/CONTROL rules, not a proven violation.")
    context(f"Staged observation: {checked} resource JSON file(s) parsed. " + " ".join(notes) +
            " Only res_lib/ and assets/data/ JSON syntax is enforced; other schemas, imports, tests and project rules require explicit review.")


if __name__ == "__main__":
    try:
        if sys.version_info < (3, 9):
            raise ValueError("Python 3.9 or newer is required")
        if len(sys.argv) != 3 or sys.argv[1] not in ("commit", "push"):
            raise ValueError("usage: git-command-check.py commit|push STUDIO_ROOT")
        inspect(sys.argv[1], Path(sys.argv[2]).resolve(), json.load(sys.stdin))
    except (ValueError, OSError, UnicodeError, subprocess.TimeoutExpired) as exc:
        context("NOT ASSESSED: " + str(exc))
        raise SystemExit(1)
