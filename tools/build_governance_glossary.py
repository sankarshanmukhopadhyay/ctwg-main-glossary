#!/usr/bin/env python3
"""Build the governance-executable glossary bundle from spec/terms-definitions markdown."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
TERMS_DIR = ROOT / "spec" / "terms-definitions"
OUT = ROOT / "generated" / "json" / "governance-executable-glossary.catalog.json"

def clean_inline(text: str) -> str:
    text = re.sub(r"\[\[ref: ([^\]]+)\]\]", lambda m: m.group(1), text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", text)
    return text.strip()

items = []
for path in sorted(TERMS_DIR.glob("*.md")):
    raw = path.read_text(encoding="utf-8")
    head = next((ln for ln in raw.splitlines() if ln.startswith("[[def:")), "")
    m = re.match(r"\[\[def: ([^\]]+)\]\]", head)
    if not m:
        continue
    term = m.group(1).split(",")[0].strip()
    items.append({"term": term, "definition_source": str(path.relative_to(ROOT)).replace("\\", "/"), "preview": clean_inline(raw[:280])})

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({"terms": items}, indent=2), encoding="utf-8")
print(f"Wrote {len(items)} catalog entries to {OUT}")
