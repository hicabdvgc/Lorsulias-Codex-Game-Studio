"""Bounded regression fixtures for exact Git context and rotation snapshot validation."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

sys.dont_write_bytecode = True
STUDIO = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=str(STUDIO / 'CGS Skill Testing Framework/results/regressions.json'))
    args = parser.parse_args()
    rows = []

    def record(name, passed, actual):
        rows.append({"case": name, "passed": bool(passed), "actual": actual})

    with tempfile.TemporaryDirectory(prefix="Lorsulia's runtime regression ") as tmp:
        root = Path(tmp)
        env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0")
        overrides = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR", "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES")
        for key in overrides:
            env.pop(key, None)
        subprocess.run(["git", "init", str(root)], env=env, check=True, capture_output=True)
        (root / "res_lib").mkdir()
        (root / "res_lib/a.json").write_text("{invalid", encoding="utf-8")
        alt = dict(env, GIT_INDEX_FILE=str(root / "alternate-index"))
        subprocess.run(["git", "-C", str(root), "add", "res_lib/a.json"], env=alt, check=True, capture_output=True)

        def observe(environment, command="git commit -m example", mode="commit"):
            event = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "cwd": str(root), "tool_input": {"command": command}}
            proc = subprocess.run([sys.executable, str(STUDIO / ".codex/hooks/git-command-check.py"), mode, str(root)],
                                  input=json.dumps(event), env=environment, text=True, encoding="utf-8", capture_output=True)
            return proc.returncode, proc.stdout + proc.stderr

        code, output = observe(alt)
        record("alternate staged index cannot receive cleaned-context pass", code == 1 and "NOT ASSESSED" in output and "GIT_INDEX_FILE" in output and "Staged observation" not in output, output)
        for key in overrides:
            code, output = observe(dict(env, **{key: str(root / "other")}))
            record("explicit unavailable context for " + key, code == 1 and "NOT ASSESSED" in output and key in output, output)
        code, output = observe(dict(env, GIT_INDEX_FILE=""))
        record("empty override remains explicit", code == 1 and "NOT ASSESSED" in output, output)
        code, output = observe(alt, "git push --force", "push")
        record("existing force prohibition survives unavailable context", code == 2 and "BLOCKED" in output, output)
        code, output = observe(alt, "printf irrelevant")
        record("irrelevant command stays irrelevant", code == 0 and not output, output)
        subprocess.run(["git", "-C", str(root), "add", "res_lib/a.json"], env=env, check=True, capture_output=True)
        code, output = observe(env)
        record("ordinary staged JSON enforcement retained", code == 2 and "staged JSON is invalid" in output, output)

        spec = importlib.util.spec_from_file_location("rotation_regression", STUDIO / ".codex/scripts/rotate_session_state.py")
        rotation = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rotation)
        source = root / "production/session-state/active.md"
        source.parent.mkdir(parents=True)
        original = b"<!-- STATUS -->\r\nTask: fixture\r\n<!-- /STATUS -->\r\n<!-- CHECKPOINT -->\r\nPending verification\r\n<!-- /CHECKPOINT -->\r\n## Notes\r\nPreserve this narrative.\r\n"

        def write_original():
            source.write_bytes(original)

        write_original()
        record("read_state retains shared parser behavior", rotation.state.read_state(root) == rotation.state.parse_state(original.decode(), source), rotation.state.read_state(root))
        # Old implementation used a separate read_state call. This tripwire proves
        # rotation now validates its exact byte snapshot through parse_state.
        with patch.object(rotation.state, "read_state", side_effect=AssertionError("separate read is forbidden")):
            result = rotation.rotate(root, dry_run=True)
        record("rotation dry run parses its own snapshot", result["status"] == "DRY RUN" and source.read_bytes() == original, result)
        malformed = original.replace(b"Task: fixture", b"Task: fixture\n<!-- STATUS -->")
        source.write_bytes(malformed)
        try:
            rotation.rotate(root)
            message = "unexpected rotation"
        except ValueError as exc:
            message = str(exc)
        record("malformed original cannot be rotated", "Rotation refused" in message and source.read_bytes() == malformed, message)

        write_original()
        parse = rotation.state.parse_state

        def edit_after_parse(snapshot, path):
            parsed = parse(snapshot, path)
            source.write_bytes(malformed)
            return parsed

        with patch.object(rotation.state, "parse_state", side_effect=edit_after_parse):
            try:
                rotation.rotate(root)
                message = "unexpected rotation"
            except ValueError as exc:
                message = str(exc)
        record("intervening edit after parse stops rotation", "State changed before rotation" in message and source.read_bytes() == malformed, message)

        write_original()
        result = rotation.rotate(root)
        prefix_end = original.index(b"<!-- /CHECKPOINT -->") + len(b"<!-- /CHECKPOINT -->")
        archive = Path(result["archive"])
        record("rotation preserves exact checkpoint prefix and narrative", result["status"] == "ROTATED" and source.read_bytes().startswith(original[:prefix_end]) and archive.read_bytes() == original[prefix_end:], result["status"])
        repeat = rotation.rotate(root)
        record("repeat rotation has no duplicate archive", repeat["status"] == "UNCHANGED", repeat)

        write_original()
        real_read = Path.read_bytes

        def edit_on_archive_read(path):
            value = real_read(path)
            if path.parent.name == "session-logs":
                source.write_bytes(malformed)
            return value

        with patch.object(Path, "read_bytes", edit_on_archive_read):
            try:
                rotation.rotate(root)
                message = "unexpected rotation"
            except ValueError as exc:
                message = str(exc)
        record("final reread preserves concurrent change and completed archive", "State changed during rotation" in message and source.read_bytes() == malformed and archive.read_bytes() == original[prefix_end:], message)

    report = {"classification": "executable disposable Git and continuity fixtures; native dispatch unassessed", "cases": rows,
              "passed": sum(r["passed"] for r in rows), "total": len(rows)}
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": report["passed"], "total": report["total"], "failures": [r for r in rows if not r["passed"]]}, indent=2))
    return 0 if all(r["passed"] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
