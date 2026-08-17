#!/usr/bin/env python3
"""Validate governance-executable glossary term YAML files.

Validation is intentionally layered:
1. JSON Schema enforces the public artifact contract.
2. Controlled vocabulary checks keep schema and vocabulary documentation aligned.
3. Repository-specific checks enforce filename, alias, source-file, and revocation semantics.
"""
from pathlib import Path
import json
import re
import sys
from urllib.parse import urlparse
import yaml

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - user-facing fallback path
    Draft202012Validator = None

ROOT = Path(__file__).resolve().parents[1]
TERMS_DIR = ROOT / "glossary" / "terms"
SCHEMA_PATH = ROOT / "schemas" / "governance-term.schema.json"
VOCAB_PATH = ROOT / "schemas" / "governance-vocabularies.yaml"

ALIAS_COLLISION_EXEMPTIONS = {"tta"}
EXTERNAL_XREF_NAMESPACES = {"keri1", "toip2"}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "term"


def normalize_term_ref(value: str) -> str:
    value = re.sub(r"\[\[(?:ref|xref):\s*", "", value, flags=re.IGNORECASE)
    value = value.replace("]]", "")
    value = value.strip().strip(".,;:")
    if "," in value:
        value = value.split(",", 1)[0].strip()
    return slugify(value)


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def enum_at(schema: dict, *path: str) -> set[str]:
    node = schema
    for part in path:
        node = node[part]
    if "enum" in node:
        return set(node["enum"])
    if "items" in node and "enum" in node["items"]:
        return set(node["items"]["enum"])
    return set()


def assert_vocab_schema_alignment(schema: dict, vocab: dict) -> list[str]:
    checks = {
        "governance_profile": ("properties", "governance_profile"),
        "authority_scope": ("properties", "governance", "properties", "authority_scope"),
        "delegation_mode": ("properties", "governance", "properties", "delegation_mode"),
        "lifecycle_states": ("properties", "governance", "properties", "lifecycle_states"),
        "execution_role": ("properties", "governance", "properties", "execution_role"),
        "control_plane_role": ("properties", "governance", "properties", "control_plane_role"),
        "enforcement_points": ("properties", "governance", "properties", "enforcement_points"),
        "assurance_level_hint": ("properties", "assurance", "properties", "assurance_level_hint"),
        "auditability": ("properties", "assurance", "properties", "auditability"),
        "evidence_artifacts": ("properties", "assurance", "properties", "evidence_artifacts"),
        "decision_points": ("properties", "control_plane", "properties", "decision_points"),
    }
    errors = []
    for key, schema_path in checks.items():
        vocab_values = set(vocab.get(key, []))
        schema_values = enum_at(schema, *schema_path)
        if vocab_values != schema_values:
            errors.append(
                f"schemas/governance-vocabularies.yaml::{key} does not match governance-term.schema.json enum"
            )
    # control_plane.evidence_produced should match evidence_artifacts too.
    if enum_at(schema, "properties", "control_plane", "properties", "evidence_produced") != set(vocab.get("evidence_artifacts", [])):
        errors.append("control_plane.evidence_produced enum does not match evidence_artifacts vocabulary")
    return errors


def basic_required_field_errors(data: dict) -> list[str]:
    required = ["schema_version", "concept_id", "designations", "term", "definition", "editorial", "provenance", "governance", "assurance", "control_plane"]
    errors = []
    for key in required:
        if key not in data:
            errors.append(f"<root>: missing required field {key}")
    return errors


def main() -> int:
    files = sorted(TERMS_DIR.glob("*.yaml"))
    if not files:
        print("No governance glossary YAML files found", file=sys.stderr)
        return 1

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    vocab = load_yaml(VOCAB_PATH) or {}
    validator = Draft202012Validator(schema) if Draft202012Validator else None

    errors = assert_vocab_schema_alignment(schema, vocab)
    if validator is None:
        print("Warning: jsonschema is not installed; running repository integrity checks with basic required-field validation.")
    term_names: dict[str, str] = {}
    alias_map: dict[str, str] = {}
    slug_map: dict[str, str] = {}
    concept_ids: dict[str, str] = {}
    source_objects = 0

    for f in files:
        try:
            data = load_yaml(f)
            if not isinstance(data, dict):
                raise ValueError("term file does not parse to an object")

            if validator:
                schema_errors = sorted(validator.iter_errors(data), key=lambda err: list(err.path))
                if schema_errors:
                    formatted = []
                    for err in schema_errors[:8]:
                        location = ".".join(str(p) for p in err.path) or "<root>"
                        formatted.append(f"{location}: {err.message}")
                    if len(schema_errors) > 8:
                        formatted.append(f"... and {len(schema_errors) - 8} more schema errors")
                    raise ValueError("schema validation failed: " + "; ".join(formatted))
            else:
                required_errors = basic_required_field_errors(data)
                if required_errors:
                    raise ValueError("basic validation failed: " + "; ".join(required_errors))

            term = str(data.get("term", "")).strip()
            if term != term.lower():
                raise ValueError("term must use repository-standard lowercase display casing")
            expected_slug = slugify(f.stem)
            computed_slug = slugify(term)
            if expected_slug != computed_slug:
                raise ValueError(f'filename slug mismatch: file implies "{expected_slug}" but term implies "{computed_slug}"')

            concept_id = str(data.get("concept_id", "")).strip()
            expected_concept_id = f"urn:tig:concept:{expected_slug}"
            if concept_id != expected_concept_id:
                raise ValueError(f'concept_id must be "{expected_concept_id}"')
            if concept_id in concept_ids:
                raise ValueError(f'duplicate concept_id also used by {concept_ids[concept_id]}')
            concept_ids[concept_id] = f.name

            designations = data.get("designations") or []
            preferred_en = [
                d for d in designations
                if isinstance(d, dict) and d.get("status") == "preferred" and d.get("language") == "en"
            ]
            if len(preferred_en) != 1 or preferred_en[0].get("label") != term:
                raise ValueError("designations must contain exactly one English preferred label equal to term")

            term_key = term.casefold()
            if term_key in term_names:
                raise ValueError(f"duplicate term name also found in {term_names[term_key]}")
            term_names[term_key] = f.name

            if computed_slug in slug_map:
                raise ValueError(f"duplicate generated slug also found in {slug_map[computed_slug]}")
            slug_map[computed_slug] = f.name

            source_file = data.get("source_file")
            if source_file and not (ROOT / source_file).exists():
                raise ValueError(f"source_file does not exist: {source_file}")

            aliases = data.get("aliases") or []
            if not isinstance(aliases, list):
                raise ValueError("aliases must be a list when present")
            for alias in aliases:
                alias_text = str(alias).strip()
                if not alias_text:
                    raise ValueError("aliases may not contain empty values")
                alias_key = alias_text.casefold()
                existing = alias_map.get(alias_key)
                current = term
                existing_slug = slugify(existing) if existing else ""
                current_slug = slugify(current)
                normalized_aliases = {alias_key}
                if alias_key.endswith("s"):
                    normalized_aliases.add(alias_key[:-1])
                collision_is_expected = bool(normalized_aliases & {existing_slug, current_slug})
                if existing and existing != current and alias_key not in ALIAS_COLLISION_EXEMPTIONS and not collision_is_expected:
                    raise ValueError(f'alias collision: "{alias_text}" already mapped to "{existing}"')
                alias_map[alias_key] = current

            sources = data.get("sources") or []
            if not isinstance(sources, list):
                raise ValueError("sources must be a list when present")
            for source in sources:
                if isinstance(source, dict):
                    source_objects += 1
                    title = str(source.get("title", "")).strip()
                    url = str(source.get("url", "")).strip()
                    if not title or not url:
                        raise ValueError("structured source entries require title and url")
                    parsed = urlparse(url)
                    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                        raise ValueError(f"structured source URL is not absolute HTTP(S): {url}")
                elif not isinstance(source, str):
                    raise ValueError("source entries must be strings or structured citation objects")

            gov = data.get("governance") or {}
            lifecycle_states = [str(s).strip() for s in gov.get("lifecycle_states", [])]
            if gov.get("revocation_supported") and "revoked" not in lifecycle_states:
                raise ValueError('revocation_supported is true but lifecycle_states does not include "revoked"')

            assurance = data.get("assurance") or {}
            control = data.get("control_plane") or {}
            evidence_artifacts = set(assurance.get("evidence_artifacts") or [])
            evidence_produced = set(control.get("evidence_produced") or [])
            if evidence_artifacts and evidence_produced and not evidence_artifacts.intersection(evidence_produced):
                raise ValueError("assurance.evidence_artifacts and control_plane.evidence_produced should share at least one evidence type")

        except Exception as exc:
            errors.append(f"{f.name}: {exc}")

    known_slugs = set(slug_map)
    known_alias_slugs = {slugify(alias): slugify(term) for alias, term in alias_map.items()}
    for f in files:
        data = load_yaml(f) or {}
        term = str(data.get("term", "")).strip()
        see_also = data.get("see_also") or []
        if not isinstance(see_also, list):
            errors.append(f"{f.name}: see_also must be a list when present")
            continue
        for item in see_also:
            ref_slug = normalize_term_ref(str(item))
            if ref_slug and ref_slug not in known_slugs and ref_slug not in known_alias_slugs:
                errors.append(f'{f.name}: see_also reference "{item}" does not resolve to a known term or alias')

        text_fields = [
            str(data.get("definition") or ""),
            *[str(item) for item in data.get("notes") or []],
            *[str(item) for item in data.get("supporting_definitions") or []],
            *[str(item) for item in data.get("mental_models") or []],
        ]
        for text in text_fields:
            if text.count("[[") != text.count("]]"):
                errors.append(f"{f.name}: malformed internal reference marker has unmatched brackets")
            for match in re.finditer(r"\[\[(ref|xref):\s*([^\]]+)\]\]", text, flags=re.IGNORECASE):
                kind, target = match.groups()
                parts = [part.strip() for part in target.split(",") if part.strip()]
                if not parts:
                    errors.append(f"{f.name}: empty {kind} reference marker")
                    continue
                if kind.lower() == "xref" and parts[0].casefold() in EXTERNAL_XREF_NAMESPACES:
                    continue
                candidate = parts[-1] if kind.lower() == "xref" and len(parts) > 1 else parts[0]
                ref_slug = slugify(candidate)
                if ref_slug and ref_slug not in known_slugs and ref_slug not in known_alias_slugs:
                    errors.append(f'{f.name}: {kind} reference "{target}" does not resolve to a known term or alias')

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Validated {len(files)} governance term files")
    print(f"Checked {len(alias_map)} aliases for collisions")
    print(f"Checked {source_objects} structured source citations")
    print("Schema and controlled vocabularies are aligned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
