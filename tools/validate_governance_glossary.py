#!/usr/bin/env python3
"""Validate governance-executable glossary term YAML files."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
TERMS_DIR = ROOT / 'glossary' / 'terms'
REQUIRED = ['term', 'definition', 'governance', 'assurance', 'control_plane']
GOV_REQUIRED = ['authority_scope', 'delegation_mode', 'revocation_supported', 'lifecycle_states', 'execution_role']

files = sorted(TERMS_DIR.glob('*.yaml'))
if not files:
    raise SystemExit('No governance glossary YAML files found')

errors = []
for f in files:
    try:
        data = yaml.safe_load(f.read_text(encoding='utf-8'))
        if not isinstance(data, dict):
            raise ValueError('term file does not parse to an object')
        missing = [k for k in REQUIRED if k not in data]
        if missing:
            raise ValueError(f'missing required keys: {", ".join(missing)}')
        gov = data.get('governance') or {}
        gov_missing = [k for k in GOV_REQUIRED if k not in gov]
        if gov_missing:
            raise ValueError(f'missing governance keys: {", ".join(gov_missing)}')
    except Exception as exc:
        errors.append(f'{f.name}: {exc}')

if errors:
    print('Validation failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)

print(f'Validated {len(files)} governance term files')
