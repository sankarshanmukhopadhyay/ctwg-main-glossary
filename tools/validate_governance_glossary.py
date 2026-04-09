#!/usr/bin/env python3
"""Validate governance-executable glossary term YAML files."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
TERMS_DIR = ROOT / 'glossary' / 'terms'
REQUIRED = ['term', 'definition', 'governance', 'assurance', 'control_plane']
GOV_REQUIRED = ['authority_scope', 'delegation_mode', 'revocation_supported', 'lifecycle_states', 'execution_role']
ASSURANCE_REQUIRED = ['evidence_artifacts', 'assurance_level_hint', 'auditability']
CONTROL_REQUIRED = ['decision_points', 'accountable_entity', 'evidence_produced']
VALID_DELEGATION = {
    'none', 'direct', 'indirect', 'direct_or_constrained', 'constrained', 'transitive', 'delegable'
}
VALID_EXECUTION_ROLE = {
    'design', 'design_time', 'runtime', 'governance_time', 'assurance_time', 'hybrid', 'mixed', 'reference'
}
VALID_AUDITABILITY = {'low', 'medium', 'moderate', 'high', 'basic'}
ALIAS_COLLISION_EXEMPTIONS = {
    'tta',
}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r'[^a-z0-9]+', '-', value)
    return value.strip('-') or 'term'


files = sorted(TERMS_DIR.glob('*.yaml'))
if not files:
    raise SystemExit('No governance glossary YAML files found')

errors = []
term_names = {}
alias_map = {}
slug_map = {}

for f in files:
    try:
        data = yaml.safe_load(f.read_text(encoding='utf-8'))
        if not isinstance(data, dict):
            raise ValueError('term file does not parse to an object')

        missing = [k for k in REQUIRED if k not in data]
        if missing:
            raise ValueError(f'missing required keys: {", ".join(missing)}')

        term = str(data.get('term', '')).strip()
        if not term:
            raise ValueError('term must be a non-empty string')

        definition = str(data.get('definition', '')).strip()
        if not definition:
            raise ValueError('definition must be a non-empty string')

        expected_slug = slugify(f.stem)
        computed_slug = slugify(term)
        if expected_slug != computed_slug:
            raise ValueError(f'filename slug mismatch: file implies "{expected_slug}" but term implies "{computed_slug}"')

        term_key = term.casefold()
        if term_key in term_names:
            raise ValueError(f'duplicate term name also found in {term_names[term_key]}')
        term_names[term_key] = f.name

        if computed_slug in slug_map:
            raise ValueError(f'duplicate generated slug also found in {slug_map[computed_slug]}')
        slug_map[computed_slug] = f.name

        gov = data.get('governance') or {}
        if not isinstance(gov, dict):
            raise ValueError('governance must be an object')
        gov_missing = [k for k in GOV_REQUIRED if k not in gov]
        if gov_missing:
            raise ValueError(f'missing governance keys: {", ".join(gov_missing)}')

        authority_scope = gov.get('authority_scope')
        if not isinstance(authority_scope, list) or not authority_scope or not all(str(i).strip() for i in authority_scope):
            raise ValueError('governance.authority_scope must be a non-empty list of strings')

        lifecycle_states = gov.get('lifecycle_states')
        if not isinstance(lifecycle_states, list) or not lifecycle_states or not all(str(i).strip() for i in lifecycle_states):
            raise ValueError('governance.lifecycle_states must be a non-empty list of strings')

        delegation_mode = str(gov.get('delegation_mode', '')).strip()
        if not delegation_mode:
            raise ValueError('governance.delegation_mode must be a non-empty string')
        if delegation_mode not in VALID_DELEGATION:
            raise ValueError(f'governance.delegation_mode must be one of: {", ".join(sorted(VALID_DELEGATION))}')

        revocation_supported = gov.get('revocation_supported')
        if not isinstance(revocation_supported, bool):
            raise ValueError('governance.revocation_supported must be boolean')

        execution_role = str(gov.get('execution_role', '')).strip()
        if execution_role not in VALID_EXECUTION_ROLE:
            raise ValueError(f'governance.execution_role must be one of: {", ".join(sorted(VALID_EXECUTION_ROLE))}')

        assurance = data.get('assurance') or {}
        if not isinstance(assurance, dict):
            raise ValueError('assurance must be an object')
        assurance_missing = [k for k in ASSURANCE_REQUIRED if k not in assurance]
        if assurance_missing:
            raise ValueError(f'missing assurance keys: {", ".join(assurance_missing)}')

        evidence_artifacts = assurance.get('evidence_artifacts')
        if not isinstance(evidence_artifacts, list):
            raise ValueError('assurance.evidence_artifacts must be a list')

        auditability = str(assurance.get('auditability', '')).strip()
        if auditability not in VALID_AUDITABILITY:
            raise ValueError(f'assurance.auditability must be one of: {", ".join(sorted(VALID_AUDITABILITY))}')

        control = data.get('control_plane') or {}
        if not isinstance(control, dict):
            raise ValueError('control_plane must be an object')
        control_missing = [k for k in CONTROL_REQUIRED if k not in control]
        if control_missing:
            raise ValueError(f'missing control_plane keys: {", ".join(control_missing)}')

        decision_points = control.get('decision_points')
        if not isinstance(decision_points, list):
            raise ValueError('control_plane.decision_points must be a list')

        accountable_entity = str(control.get('accountable_entity', '')).strip()
        if not accountable_entity:
            raise ValueError('control_plane.accountable_entity must be a non-empty string')

        evidence_produced = control.get('evidence_produced')
        if not isinstance(evidence_produced, list):
            raise ValueError('control_plane.evidence_produced must be a list')

        source_file = data.get('source_file')
        if source_file:
            if not (ROOT / source_file).exists():
                raise ValueError(f'source_file does not exist: {source_file}')

        aliases = data.get('aliases') or []
        if not isinstance(aliases, list):
            raise ValueError('aliases must be a list when present')
        for alias in aliases:
            alias_text = str(alias).strip()
            if not alias_text:
                raise ValueError('aliases may not contain empty values')
            alias_key = alias_text.casefold()
            existing = alias_map.get(alias_key)
            current = term
            existing_slug = slugify(existing) if existing else ''
            current_slug = slugify(current)
            normalized_aliases = {alias_key}
            if alias_key.endswith('s'):
                normalized_aliases.add(alias_key[:-1])
            collision_is_expected = bool(normalized_aliases & {existing_slug, current_slug})
            if existing and existing != current and alias_key not in ALIAS_COLLISION_EXEMPTIONS and not collision_is_expected:
                raise ValueError(f'alias collision: "{alias_text}" already mapped to "{existing}"')
            alias_map[alias_key] = current

        if revocation_supported and 'revoked' not in [str(s).strip() for s in lifecycle_states]:
            raise ValueError('revocation_supported is true but lifecycle_states does not include "revoked"')

    except Exception as exc:
        errors.append(f'{f.name}: {exc}')

if errors:
    print('Validation failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)

print(f'Validated {len(files)} governance term files')
print(f'Checked {len(alias_map)} aliases for collisions')
