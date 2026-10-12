"""Isolated executable fixtures for the read-only project-coherence observer.

Run with Python 3.9+. Optional --bash exercises the existing shell/runtime adapter.
--output saves concise actual results; all fixture projects stay in a temp directory.
"""
import argparse
import hashlib
import json
import os
import shutil
from pathlib import Path
import subprocess
import sys
import tempfile


STUDIO = Path(__file__).resolve().parents[2]
SCRIPT = STUDIO / ".codex/scripts/project_coherence.py"
SHELL = STUDIO / ".codex/scripts/project-coherence.sh"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bash")
    parser.add_argument("--output", default=str(STUDIO / 'CGS Skill Testing Framework/results/coherence.json'))
    args = parser.parse_args()
    results = []
    with tempfile.TemporaryDirectory(prefix="Lorsulia's coherence ") as temporary:
        root = Path(temporary) / "studio space"
        project = root / "games/Player's game"
        project.mkdir(parents=True)
        (root / "docs").mkdir()
        prefs = root / "docs/technical-preferences.md"

        def write(path, value):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(value, encoding="utf-8")

        def configure(engine="Godot", version="4.7.2", extra="", roots="games/Player's game"):
            write(prefs, f"- **Engine**: {engine}\n- **Engine Version**: {version}\n- **Project / Code Roots**: {roots}\n" + extra)

        def clear():
            # Only the known files created by this fixture are removed.
            for p in [project / "project.godot", project / "ProjectSettings/ProjectVersion.txt", project / "Game.uproject", project / "Other.uproject"]:
                if p.exists():
                    p.unlink()

        def run(name, expected=0, check=None, status=None, command=None, env=None):
            completed = subprocess.run(command or [sys.executable, str(SCRIPT), "--root", str(root), "--project", str(project)],
                                       cwd=project, text=True, encoding="utf-8", capture_output=True, env=env)
            data = json.loads(completed.stdout) if completed.stdout.strip().startswith("{") else {}
            matching = [f for f in data.get("findings", []) if f["check"] == check]
            passed = completed.returncode == expected and (check is None or len(matching) == 1 and matching[0]["status"] == status)
            results.append({"case": name, "passed": passed, "exit": completed.returncode,
                            "expected_exit": expected, "check": check, "expected_status": status,
                            "observed": matching, "errors": data.get("errors", []), "stderr": completed.stderr})
            return data

        configure(extra="- **Rendering**: Forward+\n- **Physics**: Jolt\n")
        write(project / "project.godot", 'config_version=5\n[rendering]\nrenderer/rendering_method="forward_plus"\n[physics]\n3d/physics_engine="Jolt Physics"\n')
        run("godot rendering match", check="rendering", status="MATCH")
        run("godot named 3d backend match", check="physics-3d", status="MATCH")
        run("godot exact version unassessed", check="project-version", status="NOT ASSESSED")
        configure(extra="- **Rendering**: Compatibility\n")
        run("godot rendering differs", check="rendering", status="DIFFERS")
        write(project / "project.godot", '[physics]\n3d/physics_engine="DEFAULT"\n')
        configure(extra="- **Physics**: Jolt\n")
        run("godot default is unknown", check="physics-3d", status="NOT ASSESSED")
        write(project / "project.godot", '[rendering]\nrenderer/rendering_method="unterminated\n')
        run("godot malformed supported scalar", expected=2, check="metadata-reader", status="NOT ASSESSED")
        write(project / "project.godot", '[rendering]\nrenderer/rendering_method="mobile"\nrenderer/rendering_method="mobile"\n')
        run("godot duplicate supported scalar", expected=2)

        clear()
        configure("Unity", "6000.6.4f1")
        write(project / "ProjectSettings/ProjectVersion.txt", "m_EditorVersion: 6000.6.4f1\nm_EditorVersionWithRevision: 6000.6.4f1 (abc)\n")
        run("unity exact metadata match", check="project-version", status="MATCH")
        configure("Unity", "6000.6.3f1")
        run("unity patch difference preserved", check="project-version", status="DIFFERS")
        configure("Unity", "Unity 6.6")
        run("unity marketing prose unassessed", check="project-version", status="NOT ASSESSED")
        configure("Unity", "6000.6")
        run("unity incomplete selected version unassessed", check="project-version", status="NOT ASSESSED")
        write(project / "ProjectSettings/ProjectVersion.txt", "m_EditorVersion: 6000.6.4f1\nm_EditorVersion: 6000.6.3f1\n")
        run("unity conflicting version declarations", expected=2)

        clear()
        configure("Unreal", "5.8")
        write(project / "Game.uproject", '{"EngineAssociation":"5.8"}')
        run("unreal association match", check="project-version", status="MATCH")
        configure("Unreal", "5.8.1")
        run("unreal association lacks patch precision", check="project-version", status="NOT ASSESSED")
        configure("Unreal", "5.7")
        run("unreal association differs", check="project-version", status="DIFFERS")
        write(project / "Game.uproject", '{"EngineAssociation":"{5FFE8984-EA6F-49EC-859E-6CB8C10FE54D}"}')
        run("unreal source build association", check="project-version", status="NOT ASSESSED")
        write(project / "Game.uproject", '{"EngineAssociation":""}')
        run("unreal empty association", check="project-version", status="NOT ASSESSED")
        write(project / "Game.uproject", '{"EngineAssociation":')
        run("unreal malformed json", expected=2)
        write(project / "Game.uproject", '{"EngineAssociation":"5.8","EngineAssociation":"5.7"}')
        run("unreal duplicate json key", expected=2)
        write(project / "Other.uproject", '{}')
        run("multiple unreal projects", check="engine", status="NOT ASSESSED")

        clear()
        configure()
        run("missing engine metadata", check="engine", status="NOT ASSESSED")
        write(project / "project.godot", "config_version=5\n")
        write(project / "Game.uproject", '{}')
        run("mixed metadata scopes", check="engine", status="NOT ASSESSED")
        clear()
        write(project / "Game.uproject", '{"EngineAssociation":"5.8"}')
        run("selected family mismatch", check="engine", status="DIFFERS")
        configure("[TO BE CONFIGURED]", "[TO BE CONFIGURED]")
        run("unselected engine remains unknown", check="engine", status="NOT ASSESSED")
        configure("Unreal", "5.8", roots="other")
        run("explicit root does not override selection", check="project-root", status="DIFFERS")
        configure("Unreal", "5.8", roots="game-a; game-b")
        run("multiple declared roots unassessed", check="project-root", status="NOT ASSESSED")
        configure("Unreal", "5.8", roots="the actual project")
        run("prose root remains unassessed", check="project-root", status="NOT ASSESSED")
        configure("Unreal", "5.8", roots="See games/Foo for project root")
        run("prose root with slash remains unassessed", check="project-root", status="NOT ASSESSED")
        configure("Unreal", "5.8", extra='- **Engine**: Godot\n')
        run("duplicate preferences", expected=2, check="preferences", status="NOT ASSESSED")
        configure("Unreal", "5.8", extra='```md\n- **Engine**: Godot\n```\n<!-- - **Engine**: Unity -->\n')
        run("fenced and comment examples ignored", check="engine", status="MATCH")
        configure("Unreal", "5.8", extra='```md\n- **Engine**: Godot\n')
        run("unclosed preference fence", expected=2, check="preferences", status="NOT ASSESSED")
        configure("Unreal", "5.8", extra='<!-- - **Engine**: Unity\n')
        run("unclosed preference comment", expected=2, check="preferences", status="NOT ASSESSED")
        configure("Unreal", "5.8", extra='-->\n')
        run("unmatched preference comment", expected=2, check="preferences", status="NOT ASSESSED")
        configure("Unreal", "5.8", extra='- **Test Roots and Commands**: $(touch injected); python -c "open(\'injected\',\'w\')"\n- **Installed Version Evidence**: claimed installed 5.8\n')
        before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob("*") if p.is_file()}
        run("command text data only", check="commands", status="NOT ASSESSED")
        after = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob("*") if p.is_file()}
        results.append({"case": "observer made no writes", "passed": before == after})
        run("installed claim remains unverified", check="installed-runtime", status="NOT ASSESSED")
        write(root / "docs/engine-reference/unreal/VERSION.md", "- Library version: **5.7**.\n")
        run("library difference is not automatic failure", check="library-compatibility", status="NOT ASSESSED")
        run("missing explicit project argument", expected=2, command=[sys.executable, str(SCRIPT), "--root", str(root)])
        run("missing root", expected=2, command=[sys.executable, str(SCRIPT), "--root", str(root / "absent"), "--project", "."])
        prefs.unlink()
        run("unavailable preferences", expected=2, check="preferences", status="NOT ASSESSED")
        configure("Unreal", "5.8")
        prefs.write_bytes(b"\xff\xfeinvalid utf8")
        run("unreadable text encoding", expected=2)
        configure("Unreal", "5.8")
        if args.bash:
            env = dict(os.environ, LORSULIA_HOOK_PYTHON=sys.executable, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1", MSYS_NO_PATHCONV="1", MSYS2_ARG_CONV_EXCL="*")
            run("bash nested nonGit spaces apostrophes", check="project-root", status="MATCH", command=[args.bash, str(SHELL), "--root", str(root), "--project", str(project)], env=env)
            run("bash missing path value", expected=2, command=[args.bash, str(SHELL), "--project"], env=env)
            env["LORSULIA_HOOK_PYTHON"] = str(root / "missing-python")
            env["PATH"] = str(Path(args.bash).parent.parent / "usr/bin")
            for relative in ['.codex/scripts/project-coherence.sh', '.codex/hooks/hook-lib.sh']:
                destination = root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(STUDIO / relative, destination)
            run("bash unavailable runtime", expected=2, command=[args.bash, str(root / '.codex/scripts/project-coherence.sh'), "--root", str(root), "--project", str(project)], env=env)

    report = {"classification": "executable isolated fixtures; no engine or native Codex integration", "cases": results,
              "passed": sum(r["passed"] for r in results), "total": len(results)}
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({"passed": report["passed"], "total": report["total"], "failures": [r for r in results if not r["passed"]]}, indent=2))
    return 0 if all(r["passed"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
