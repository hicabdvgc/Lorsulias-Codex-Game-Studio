"""Shared paths for isolated helper fixtures; never writes to studio inputs."""
from pathlib import Path
import ast, hashlib, json, os, re, shutil, subprocess, sys, tomllib
import yaml

T = Path(__file__).resolve().parents[3]
WORK = Path(os.environ['STUDIO_VERIFICATION_WORK']).resolve()
BASH = os.environ['STUDIO_TEST_BASH']
WORK.mkdir(parents=True, exist_ok=True)

def read(relative):
    return (T / relative).read_text(encoding='utf-8-sig')

def python_without_packages():
    """Provide a real Python without PyYAML, regardless of the caller's environment."""
    root = WORK / 'python-without-packages'
    executable = root / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
    if not executable.exists():
        subprocess.run([sys.executable, '-m', 'venv', '--without-pip', str(root)], check=True, timeout=60)
    return str(executable)
