#!/usr/bin/env python3
"""Validate Trust Infrastructure Glossary vocabulary profiles."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
TERMS_DIR = ROOT / "glossary" / "terms"
PROFILES_DIR = ROOT / "profiles"

def main() -> int:
    known = {}
    for path in sorted(TERMS_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        cid = data.get("concept_id")
        if cid:
            known[cid] = path.name

    errors = []
    profile_ids = set()
    for path in sorted(PROFILES_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for field in ["profile_id", "title", "version", "minimum_tig_version", "purpose", "concepts"]:
            if field not in data:
                errors.append(f"{path.name}: missing {field}")
        pid = data.get("profile_id")
        if pid in profile_ids:
            errors.append(f"{path.name}: duplicate profile_id {pid}")
        profile_ids.add(pid)
        concepts = data.get("concepts") or []
        if len(concepts) != len(set(concepts)):
            errors.append(f"{path.name}: duplicate concept references")
        for cid in concepts:
            if cid not in known:
                errors.append(f"{path.name}: unknown concept_id {cid}")

    if errors:
        print("Profile validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Validated {len(list(PROFILES_DIR.glob('*.yaml')))} vocabulary profiles against {len(known)} concepts")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
