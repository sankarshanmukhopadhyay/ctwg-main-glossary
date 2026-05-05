#!/usr/bin/env python3
"""Generate Jekyll markdown pages from governance-executable glossary YAML artifacts."""
from pathlib import Path
import json
import re
from collections import defaultdict
import yaml

ROOT = Path(__file__).resolve().parents[1]
TERMS_DIR = ROOT / "glossary" / "terms"
OUT_COLLECTION = ROOT / "_terms"
TERMS_INDEX = ROOT / "terms-index.md"
LETTER_DIR = ROOT / "terms"
GOVERNANCE_DIR = ROOT / "governance"
GENERATED_MD = ROOT / "generated" / "markdown"
GENERATED_JSON = ROOT / "generated" / "json"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "term"


def clean_text(text):
    if text is None:
        return ""
    return str(text).strip()


def format_list(items):
    items = [clean_text(i) for i in (items or []) if clean_text(i)]
    if not items:
        return "Not specified"
    return "\n".join(f"- {i}" for i in items)


def term_page(data):
    title = clean_text(data.get("term", "Untitled Term"))
    aliases = data.get("aliases") or []
    definition = clean_text(data.get("definition"))
    notes = data.get("notes") or []
    see_also = data.get("see_also") or []
    gov = data.get("governance") or {}
    assurance = data.get("assurance") or {}
    control = data.get("control_plane") or {}
    crosswalk = data.get("crosswalk") or {}
    supporting = data.get("supporting_definitions") or []
    mental_models = data.get("mental_models") or []

    aliases_md = ", ".join(aliases) if aliases else "None"
    crosswalk_lines = []
    for key, vals in crosswalk.items():
        if vals:
            crosswalk_lines.append(f"- **{key.upper()}**: {', '.join(vals)}")
    crosswalk_md = "\n".join(crosswalk_lines) if crosswalk_lines else "Not specified"

    safe_title = title.replace('"', "'")

    return f"""---
title: \"{safe_title}\"
---

> Generated file. Update `glossary/terms/{slugify(title)}.yaml` and regenerate artifacts instead of editing this page directly.

# {title}

## Definition
{definition or 'Definition not yet provided.'}

## Aliases
{aliases_md}

## Governance Profile
- **Authority scope**: {', '.join(gov.get('authority_scope', [])) or 'Not specified'}
- **Delegation mode**: {clean_text(gov.get('delegation_mode')) or 'Not specified'}
- **Revocation supported**: {gov.get('revocation_supported', 'Not specified')}
- **Lifecycle states**: {', '.join(gov.get('lifecycle_states', [])) or 'Not specified'}
- **Execution role**: {clean_text(gov.get('execution_role')) or 'Not specified'}
- **Control-plane role**: {clean_text(gov.get('control_plane_role')) or 'Not specified'}

## Enforcement Points
{format_list(gov.get('enforcement_points'))}

## Assurance
**Evidence artifacts**
{format_list(assurance.get('evidence_artifacts'))}

- **Assurance level hint**: {clean_text(assurance.get('assurance_level_hint')) or 'Not specified'}
- **Auditability**: {clean_text(assurance.get('auditability')) or 'Not specified'}

## Control Plane
**Decision points**
{format_list(control.get('decision_points'))}

- **Accountable entity**: {clean_text(control.get('accountable_entity')) or 'Not specified'}

**Evidence produced**
{format_list(control.get('evidence_produced'))}

## Notes
{format_list(notes)}

## Supporting Definitions
{format_list(supporting)}

## Mental Models
{format_list(mental_models)}

## See Also
{format_list(see_also)}

## Crosswalk References
{crosswalk_md}
"""


def write_indexes(term_refs):
    grouped = defaultdict(list)
    for title, url in term_refs:
        letter = title[0].upper() if title and title[0].isalnum() else '#'
        grouped[letter].append((title, url))
    for letter in grouped:
        grouped[letter].sort(key=lambda x: x[0].lower())

    letters = sorted(grouped.keys(), key=lambda x: ('{' if x == '#' else x))
    lines = [
        '---',
        'title: "Glossary Terms"',
        'nav_order: 2',
        'has_children: false',
        '---',
        '',
        '# Glossary Terms',
        '',
        f'This index is generated from `{TERMS_DIR.relative_to(ROOT)}/` and currently includes **{len(term_refs)}** terms.',
        '',
        '## Browse by letter',
        ''
    ]
    for letter in letters:
        target = "{{ '/terms/num/' | relative_url }}" if letter == '#' else f"{{{{ '/terms/{letter.lower()}/' | relative_url }}}}"
        lines.append(f'- [{letter}]({target})')
    lines.append('')
    for letter in letters:
        lines.append(f'## {letter}')
        lines.append('')
        for title, url in grouped[letter][:25]:
            lines.append(f'- [{title}]({url})')
        if len(grouped[letter]) > 25:
            target = "{{ '/terms/num/' | relative_url }}" if letter == '#' else f"{{{{ '/terms/{letter.lower()}/' | relative_url }}}}"
            lines.append(f'- [View all {len(grouped[letter])} terms for {letter}]({target})')
        lines.append('')
    TERMS_INDEX.write_text("\n".join(lines), encoding='utf-8')

    LETTER_DIR.mkdir(exist_ok=True)
    for letter in letters:
        subdir = LETTER_DIR / ('num' if letter == '#' else letter.lower())
        subdir.mkdir(parents=True, exist_ok=True)
        page = [
            '---',
            f'title: "Terms: {letter}"',
            'parent: "Glossary Terms"',
            'nav_exclude: true',
            '---',
            '',
            f'# Terms: {letter}',
            ''
        ]
        for title, url in grouped[letter]:
            page.append(f'- [{title}]({url})')
        page.append('')
        (subdir / 'index.md').write_text("\n".join(page), encoding='utf-8')


def write_generated_inventory_page():
    inventory_path = GENERATED_JSON / 'governance-inventory.json'
    if not inventory_path.exists():
        return
    inventory = json.loads(inventory_path.read_text(encoding='utf-8'))
    page = [
        '---',
        'title: "Generated Inventories"',
        'parent: Governance Documentation',
        'nav_order: 20',
        '---',
        '',
        '# Generated Inventories',
        '',
        'This page summarizes the generated governance inventory built from the structured term layer.',
        '',
        f"- Total terms: **{inventory.get('term_count', 0)}**",
        f"- Authority-bearing terms: **{len(inventory.get('authority_terms', []))}**",
        f"- Delegation-sensitive terms: **{len(inventory.get('delegation_terms', []))}**",
        f"- Revocation-sensitive terms: **{len(inventory.get('revocation_terms', []))}**",
        f"- Lifecycle-sensitive terms: **{len(inventory.get('lifecycle_terms', []))}**",
        f"- Evidence-producing terms: **{len(inventory.get('evidence_terms', []))}**",
        f"- Control-plane terms: **{len(inventory.get('control_plane_terms', []))}**",
        '',
        '## Top authority scopes',
        ''
    ]
    for scope, count in list(inventory.get('authority_scope_counts', {}).items())[:20]:
        page.append(f'- `{scope}`: {count}')
    page.extend(['', '## Assurance level hints', ''])
    for hint, count in inventory.get('assurance_level_hints', {}).items():
        page.append(f'- `{hint}`: {count}')
    page.extend([
        '',
        '## Artifact references',
        '',
        '- `generated/json/governance-inventory.json`',
        '- `generated/markdown/governance-inventory.md`',
        '- `generated/json/governance-quality-report.json`',
        '- `generated/markdown/governance-quality-report.md`',
        '- `generated/json/artifact-manifest.json`',
        '- `generated/markdown/artifact-manifest.md`',
        '- `glossary/overlays/governance/inventory.json`',
        ''
    ])
    (GOVERNANCE_DIR / 'generated-inventories.md').write_text("\n".join(page), encoding='utf-8')


def main():
    OUT_COLLECTION.mkdir(exist_ok=True)
    term_refs = []
    for path in sorted(TERMS_DIR.glob('*.yaml')):
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
        title = clean_text(data.get('term'))
        if not title:
            continue
        slug = slugify(path.stem)
        out = OUT_COLLECTION / f'{slug}.md'
        out.write_text(term_page(data), encoding='utf-8')
        term_refs.append((title, f"{{{{ '/terms/{slug}/' | relative_url }}}}"))

    write_indexes(term_refs)
    write_generated_inventory_page()

    summary = {
        'term_count': len(term_refs),
        'collection_dir': str(OUT_COLLECTION.relative_to(ROOT)),
        'index_page': str(TERMS_INDEX.relative_to(ROOT)),
        'generated_inventory_page': str((GOVERNANCE_DIR / 'generated-inventories.md').relative_to(ROOT)),
        'generated_quality_report_page': str((GOVERNANCE_DIR / 'quality-report.md').relative_to(ROOT)),
    }
    GENERATED_JSON.mkdir(parents=True, exist_ok=True)
    (GENERATED_JSON / 'jekyll-site-build-summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(f'Generated {len(term_refs)} Jekyll term pages')


if __name__ == '__main__':
    main()
