"""Observe declared paths in Lorsulia's catalog. Never infer workflow completion."""
from pathlib import Path
import argparse
import json
import sys


def run():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--phase")
    args = parser.parse_args()
    try:
        import yaml
    except ImportError:
        raise ValueError("PyYAML unavailable in selected Python; supply an available runtime with PyYAML. No installation performed.")
    class UniqueLoader(yaml.SafeLoader):
        pass
    def mapping(loader, node):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node)
            if not isinstance(key, str) or key in result:
                raise ValueError("catalog mapping keys must be unique strings")
            result[key] = loader.construct_object(value_node)
        return result
    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    root = args.root.resolve()
    try:
        catalog = yaml.load((root / ".codex/docs/workflow-catalog.yaml").read_text(encoding="utf-8-sig"), Loader=UniqueLoader)
    except yaml.YAMLError as exc:
        raise ValueError("malformed catalog: " + str(exc)) from exc
    phases = catalog.get("phases") if isinstance(catalog, dict) else None
    if not isinstance(phases, dict) or not phases:
        raise ValueError("catalog requires a nonempty phases mapping")
    if args.phase and args.phase not in phases:
        raise ValueError("unknown phase: " + args.phase)
    rows, ids = [], set()
    for phase, data in phases.items():
        if args.phase and phase != args.phase:
            continue
        steps = data.get("steps") if isinstance(data, dict) else None
        if not isinstance(steps, list) or not steps:
            raise ValueError("phase requires a nonempty steps list: " + phase)
        for step in steps:
            if not isinstance(step, dict) or not isinstance(step.get("id"), str) or not step["id"] or step["id"] in ids:
                raise ValueError("steps require unique nonempty string identities")
            ids.add(step["id"])
            row = {"phase": phase, "id": step["id"], "outcome": step.get("completion"), "status": "NO_CHECK"}
            if "artifact" in step:
                artifact = step["artifact"]
                value = artifact.get("path") if isinstance(artifact, dict) else None
                if not isinstance(value, str) or not value.strip():
                    raise ValueError("artifact.path must be a nonempty literal path: " + step["id"])
                relative = Path(value.replace("\\", "/"))
                path = (root / relative).resolve()
                if relative.is_absolute() or not path.is_relative_to(root) or any(c in value for c in "*?["):
                    raise ValueError("artifact.path must be a literal path within the studio: " + value)
                row.update(path=value, maturity=artifact.get("maturity"))
                try:
                    if not path.exists():
                        row["status"] = "ABSENT"
                    elif path.is_file():
                        row["status"] = "PRESENT" if path.read_bytes().strip() else "EMPTY"
                    elif path.is_dir():
                        row["status"] = "PRESENT" if next(path.iterdir(), None) else "EMPTY"
                    else:
                        row["status"] = "UNREADABLE"
                except OSError as exc:
                    row.update(status="UNREADABLE", error=str(exc))
            rows.append(row)
    counts = {status: sum(r["status"] == status for r in rows) for status in ("PRESENT", "ABSENT", "EMPTY", "UNREADABLE", "NO_CHECK")}
    print(json.dumps({"root": str(root), "steps_observed": len(rows), "counts": counts, "observations": rows,
                      "limitation": "Declared-path discovery only; no maturity, manual outcome or gate conclusion."}, ensure_ascii=True))
    return 2 if counts["UNREADABLE"] else 1 if counts["ABSENT"] or counts["EMPTY"] else 0


if __name__ == "__main__":
    try:
        if sys.version_info < (3, 9):
            raise ValueError("Python 3.9 or newer is required")
        raise SystemExit(run())
    except (ValueError, OSError, UnicodeError) as exc:
        print(json.dumps({"status": "NOT ASSESSED", "error": str(exc)}))
        raise SystemExit(2)
