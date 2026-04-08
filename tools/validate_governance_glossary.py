#!/usr/bin/env python3
"""Lightweight validator for governance-executable glossary term YAML files."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TERMS_DIR = ROOT / "glossary" / "terms"
REQUIRED_TOP = ["term:", "definition:", "governance:", "assurance:", "control_plane:"]

def validate_file(path: Path):
    text = path.read_text(encoding="utf-8")
    missing = [item for item in REQUIRED_TOP if item not in text]
    if missing:
        raise ValueError(f"{path.name}: missing required sections: {', '.join(missing)}")

files = sorted(TERMS_DIR.glob("*.yaml"))
if not files:
    raise SystemExit("No governance glossary YAML files found")

errors = []
for f in files:
    try:
        validate_file(f)
    except Exception as exc:
        errors.append(str(exc))

if errors:
    print("Validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print(f"Validated {len(files)} governance term files")
