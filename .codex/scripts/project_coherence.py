"""Observe selected preferences against explicit project metadata; never execute it.

Adapted from Claude Code Game Studios' project-coherence.sh. See the accompanying
project-coherence documentation for the deliberately bounded metadata readers.
"""
import argparse
import json
import re
import sys
from pathlib import Path


class MetadataError(ValueError):
    pass


def text(path):
    return path.read_text(encoding="utf-8-sig")


def preferences(path):
    # Only current live bullet fields, outside comments and fenced examples.
    body = re.sub(r"<!--.*?-->", "", text(path), flags=re.S)
    if "<!--" in body or "-->" in body:
        raise MetadataError("unclosed or unmatched preference comment")
    fields, fence = {}, None
    for line in body.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        match = re.match(r"^\s*-\s+\*\*(.+?)\*\*:\s*(.*?)\s*$", line)
        if match:
            key, value = match.groups()
            if key in fields:
                raise MetadataError("duplicate preference field: " + key)
            fields[key] = value
    if fence is not None:
        raise MetadataError("unclosed preference example fence")
    return fields


def selected(value):
    value = (value or "").strip()
    if not value or value.startswith("[") or value.casefold() in {
        "unconfigured", "unknown", "not assessed", "not selected", "none configured"
    }:
        return None
    return value.strip("`")


def literal_path(value):
    value = selected(value)
    if not value or any(c in value for c in "\n;|<>[]"):
        return None
    quoted = value.startswith(('"', "'")) and value.endswith(value[0])
    if quoted:
        value = value[1:-1]
    if "$" in value or "`" in value or re.search(r"\s(?:and|or)\s", value):
        return None
    if not quoted and " " in value and "/" not in value and "\\" not in value:
        return None
    return Path(value.replace("\\", "/"))


def exact_version(value):
    value = selected(value)
    if value and re.fullmatch(r"\d+\.\d+(?:\.\d+)?(?:[abfp]\d+)?", value):
        return value
    return None


def godot_values(path):
    # Read relevant scalar assignments only. This is not a Godot Variant parser.
    watched = {"rendering/renderer/rendering_method", "physics/3d/physics_engine"}
    values, section = {}, ""
    for line in text(path).splitlines():
        line = line.strip()
        if not line or line.startswith(";"):
            continue
        if re.fullmatch(r"\[[^\]]+\]", line):
            section = line[1:-1]
            continue
        if "=" not in line:
            continue
        key, raw = line.split("=", 1)
        key = section + "/" + key.strip()
        if key not in watched:
            continue
        if key in values:
            raise MetadataError("duplicate Godot scalar: " + key)
        try:
            value = json.loads(raw.strip())
        except json.JSONDecodeError as exc:
            raise MetadataError("unsupported or malformed quoted Godot scalar: " + key) from exc
        if not isinstance(value, str):
            raise MetadataError("expected string Godot scalar: " + key)
        values[key] = value
    return values


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise MetadataError("duplicate JSON key: " + key)
        result[key] = value
    return result


def inspect(root, project):
    findings, errors = [], []
    prefs_path = root / "docs/technical-preferences.md"

    def add(check, status, reason, evidence, **values):
        findings.append(dict(check=check, status=status, reason=reason,
                             evidence=[str(p) for p in evidence], **values))

    def unavailable(check, reason, evidence=(), **values):
        add(check, "NOT ASSESSED", reason, evidence, **values)

    def compare(check, wanted, actual, evidence, caveat=""):
        if wanted is None or actual is None:
            unavailable(check, "A selected value or supported explicit metadata value is unavailable. " + caveat,
                        evidence, selected=wanted, observed=actual)
        else:
            add(check, "MATCH" if wanted == actual else "DIFFERS",
                "Compared explicit declarations. " + caveat, evidence, selected=wanted, observed=actual)

    try:
        prefs = preferences(prefs_path)
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append(str(exc))
        unavailable("preferences", "Cannot read unambiguous live preference fields.", [prefs_path])
        return findings, errors
    declared = literal_path(prefs.get("Project / Code Roots"))
    raw_root = selected(prefs.get("Project / Code Roots")) or ""
    quoted_root = raw_root.startswith(('"', "'")) and raw_root.endswith(raw_root[0])
    if declared is not None and " " in str(declared) and not quoted_root and not (root / declared).is_dir():
        # A prose sentence containing a slash is not sufficient literal-path evidence.
        # Existing unquoted paths with spaces remain usable; quoted paths are explicit.
        declared = None
    if declared is None:
        unavailable("project-root", "Root is unset or uses prose/multiple-root notation; explicit --project only scopes this observation.", [prefs_path], observed=str(project))
    else:
        declared = (root / declared).resolve()
        compare("project-root", str(declared), str(project), [prefs_path])
    engine = selected(prefs.get("Engine"))
    engine = engine.casefold() if engine else None
    markers = {"godot": project / "project.godot", "unity": project / "ProjectSettings/ProjectVersion.txt"}
    try:
        unreal_files = sorted(p for p in project.iterdir() if p.suffix.casefold() == ".uproject")
        families = [name for name, path in markers.items() if path.is_file()]
        if unreal_files:
            families.append("unreal")
    except OSError as exc:
        errors.append(str(exc))
        unavailable("project-discovery", "Cannot enumerate the explicit project root.", [project])
        return findings, errors
    if engine not in {"godot", "unity", "unreal"}:
        unavailable("engine", "Select one supported engine name in live preferences; discovered markers do not select it.", [prefs_path, project], selected=engine, observed=families)
    elif len(families) != 1 or (engine == "unreal" and len(unreal_files) != 1):
        unavailable("engine", "No unique project metadata scope; missing or competing engine markers require resolution.", [project], selected=engine, observed=families)
    elif families[0] != engine:
        add("engine", "DIFFERS", "Selected engine differs from the sole observed metadata family.", [prefs_path, project], selected=engine, observed=families[0])
    else:
        add("engine", "MATCH", "Selected family has one project metadata scope; this does not establish a usable runtime.", [prefs_path, project], selected=engine, observed=engine)
        try:
            if engine == "godot":
                path = markers[engine]
                values = godot_values(path)
                unavailable("project-version", "config_version and feature tags do not establish the exact selected or installed engine version.", [path], selected=selected(prefs.get("Engine Version")))
                wanted = selected(prefs.get("Rendering"))
                aliases = {"forward+": "forward_plus", "forward plus": "forward_plus", "forward_plus": "forward_plus", "mobile": "mobile", "compatibility": "gl_compatibility", "gl compatibility": "gl_compatibility", "gl_compatibility": "gl_compatibility"}
                wanted = aliases.get(wanted.casefold()) if wanted else None
                compare("rendering", wanted, values.get("rendering/renderer/rendering_method"), [prefs_path, path], "Base configuration only; platform overrides, runtime changes and fallback remain unassessed.")
                physics = selected(prefs.get("Physics"))
                # Only named, unambiguous 3D backend choices are comparable.
                physics_aliases = {"jolt": "Jolt Physics", "jolt physics": "Jolt Physics", "godotphysics3d": "GodotPhysics3D"}
                wanted = physics_aliases.get(physics.casefold()) if physics else None
                observed = values.get("physics/3d/physics_engine")
                if observed == "DEFAULT":
                    observed = None
                compare("physics-3d", wanted, observed, [prefs_path, path], "Only a named Jolt or GodotPhysics3D choice is comparable. This checks the declared 3D backend, with no inference about 2D use, node types or defaults.")
            elif engine == "unity":
                path = markers[engine]
                matches = re.findall(r"^m_EditorVersion:\s*(.*?)\s*$", text(path), re.M)
                if len(matches) != 1 or exact_version(matches[0]) is None:
                    raise MetadataError("ProjectVersion.txt requires one supported m_EditorVersion value")
                wanted = exact_version(prefs.get("Engine Version"))
                if not wanted or not re.fullmatch(r"\d+\.\d+\.\d+[abfp]\d+", wanted):
                    wanted = None
                compare("project-version", wanted, matches[0], [prefs_path, path], "Only a full selected editor version is comparable. Recorded editor version is not proof of an installed or executed editor.")
            else:
                path = unreal_files[0]
                data = json.loads(text(path), object_pairs_hook=unique_object)
                if not isinstance(data, dict) or not isinstance(data.get("EngineAssociation", ""), str):
                    raise MetadataError(".uproject must be an object with a string EngineAssociation")
                version = exact_version(data.get("EngineAssociation"))
                wanted = exact_version(prefs.get("Engine Version"))
                if version and wanted and len(version.split(".")) != len(wanted.split(".")):
                    unavailable("project-version", "EngineAssociation and selected version have different precision; association cannot establish an exact patch match.", [prefs_path, path], selected=wanted, observed=version)
                else:
                    compare("project-version", wanted, version, [prefs_path, path], "Empty or opaque source-build associations do not establish a version; installation is unassessed.")
            if engine != "godot":
                add("godot-scalars", "NOT APPLICABLE", "Godot scalar readers do not apply to this selected family.", [project])
                unavailable("rendering-and-physics", "Unity/Unreal rendering and physics settings require project-specific inspection; no generic reader is installed.", [project])
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(str(exc))
            unavailable("metadata-reader", "Could not read supported project metadata: " + str(exc), [project])
    # These are provenance disclosures, never a probe or a compatibility verdict.
    library = root / "docs/engine-reference" / (engine if engine in {"godot", "unity", "unreal"} else "unconfigured") / "VERSION.md"
    library_value = None
    if engine in {"godot", "unity", "unreal"} and library.exists():
        try:
            rows = re.findall(r"^- Library version:\s*(.*?)\s*$", text(library), re.M)
            library_value = rows[0] if len(rows) == 1 else None
        except (OSError, UnicodeError) as exc:
            errors.append(str(exc))
    unavailable("library-compatibility", "Library coverage is separate from project selection; a version difference requires a scoped compatibility assessment.", [library], library=library_value, selected=selected(prefs.get("Engine Version")))
    unavailable("installed-runtime", "Recorded evidence is reproduced as data; no binary was located or executed and linked evidence was not evaluated.", [prefs_path], recorded=selected(prefs.get("Installed Version Evidence")))
    unavailable("commands", "Command declarations are data. No runner, shell syntax, export preset, test or build was executed or validated.", [prefs_path], declared=selected(prefs.get("Test Roots and Commands")))
    return findings, errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[2]), help="Studio root; relative paths use current directory")
    parser.add_argument("--project", required=True, help="Actual project root; relative paths use studio root")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    project = (root / args.project).resolve()
    if not root.is_dir() or not project.is_dir():
        print(json.dumps({"findings": [], "errors": ["Studio and explicit project roots must be existing directories."]}))
        return 2
    findings, errors = inspect(root, project)
    print(json.dumps({"studio_root": str(root), "project_root": str(project),
                      "scope": "read-only declared metadata; no readiness or runtime verdict",
                      "findings": findings, "errors": errors}, ensure_ascii=True, indent=2))
    return 2 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
