#!/usr/bin/env python3
"""Explicit narrative rotation, adapted from the Claude helper; never a hook."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import tempfile

spec = importlib.util.spec_from_file_location('session_state', Path(__file__).with_name('session-state.py'))
state = importlib.util.module_from_spec(spec)
spec.loader.exec_module(state)


def rotate(root, dry_run=False):
    root = Path(root)
    source = root / 'production/session-state/active.md'
    try:
        original = source.read_bytes()
    except FileNotFoundError:
        return {'status': 'ABSENT', 'message': 'No state to rotate.'}
    # Validate precisely the bytes later archived/replaced, rather than another read.
    parsed = state.parse_state(original.decode('utf-8-sig'), source)
    if parsed['status'] != 'VALID':
        raise ValueError('Rotation refused: ' + '; '.join(parsed['limitations']))
    # Preserve the exact original prefix, including BOM and newline convention.
    marker = b'<!-- /CHECKPOINT -->'
    end = original.index(marker) + len(marker)
    narrative = original[end:]
    substantive = narrative.decode('utf-8-sig').strip()
    if not substantive or substantive == '## Notes' or re.fullmatch(r'## Notes\r?\n\r?\nNarrative archived: [^\r\n]+', substantive):
        return {'status': 'UNCHANGED', 'message': 'No unarchived narrative.'}
    digest = hashlib.sha256(narrative).hexdigest()
    archive = root / 'production/session-logs' / ('session-state-' + digest + '.md')
    if dry_run:
        return {'status': 'DRY RUN', 'archive': str(archive), 'narrative_bytes': len(narrative)}
    lock = source.with_name('.session-state-rotation.lock')
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise ValueError('Rotation lock exists; inspect active operation/stale lock before retrying.')
    os.close(descriptor)
    temporary = None
    archived = False
    try:
        if source.read_bytes() != original:
            raise ValueError('State changed before rotation; source preserved.')
        with tempfile.NamedTemporaryFile(dir=source.parent, prefix='.rotation-', delete=False) as f:
            temporary = Path(f.name)
            f.write(original[:end] + ('\n\n## Notes\n\nNarrative archived: ' + archive.relative_to(root).as_posix() + '\n').encode())
            f.flush()
            os.fsync(f.fileno())
        archive.parent.mkdir(parents=True, exist_ok=True)
        try:
            with archive.open('xb') as f:
                f.write(narrative)
                f.flush()
                os.fsync(f.fileno())
        except FileExistsError:
            if archive.read_bytes() != narrative:
                raise ValueError('Archive collision/content mismatch; source preserved.')
        if archive.read_bytes() != narrative:
            raise OSError('Archive verification failed; source preserved.')
        archived = True
        if source.read_bytes() != original:
            raise ValueError('State changed during rotation; source preserved, archive saved at ' + str(archive))
        os.replace(temporary, source)
        temporary = None
        return {'status': 'ROTATED', 'archive': str(archive), 'source': str(source)}
    except (OSError, ValueError) as exc:
        raise ValueError(str(exc) + ('; verified archive retained at ' + str(archive) if archived else '; inspect archive for a partial save: ' + str(archive))) from exc
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        lock.unlink(missing_ok=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        print(json.dumps(rotate(args.root.resolve(), args.dry_run)))
    except (OSError, ValueError) as exc:
        print(json.dumps({'status': 'ERROR', 'message': str(exc)}))
        raise SystemExit(1)
