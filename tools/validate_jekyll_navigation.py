#!/usr/bin/env python3
"""Detect duplicate publishable Jekyll navigation identities.

A navigation identity is the normalized combination of front-matter title and parent.
Files excluded by _config.yml are ignored. Generated term pages are intentionally
excluded because they are hidden from navigation by collection defaults.
"""
from collections import defaultdict
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8")) or {}
EXCLUDED = [str(item).rstrip("/") for item in CONFIG.get("exclude", [])]
SKIP_DIRS = {".git", "node_modules", "vendor", "_site", "_terms"}


def is_excluded(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return any(rel == item or rel.startswith(item + "/") for item in EXCLUDED)


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    _, raw, _ = text.split("---", 2)
    return yaml.safe_load(raw) or {}


def main() -> int:
    identities = defaultdict(list)
    for path in ROOT.rglob("*.md"):
        rel_parts = path.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in rel_parts) or is_excluded(path):
            continue
        data = front_matter(path)
        if not data or data.get("nav_exclude") is True:
            continue
        title = str(data.get("title", "")).strip()
        if not title:
            continue
        parent = str(data.get("parent", "")).strip()
        key = (title.casefold(), parent.casefold())
        identities[key].append(path.relative_to(ROOT).as_posix())

    duplicates = {key: paths for key, paths in identities.items() if len(paths) > 1}
    if duplicates:
        print("Duplicate Jekyll navigation identities found:")
        for (title, parent), paths in sorted(duplicates.items()):
            print(f'- title="{title}", parent="{parent or "<root>"}": {", ".join(paths)}')
        return 1

    print(f"Validated {len(identities)} unique Jekyll navigation identities")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
