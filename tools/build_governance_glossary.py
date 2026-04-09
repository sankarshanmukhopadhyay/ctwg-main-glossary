#!/usr/bin/env python3
"""Build machine-readable and markdown bundles from governance-executable glossary YAML artifacts."""
from pathlib import Path
from collections import Counter, defaultdict
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
TERMS_DIR = ROOT / "glossary" / "terms"
JSON_OUT = ROOT / "generated" / "json"
MD_OUT = ROOT / "generated" / "markdown"
OVERLAY_GOV = ROOT / "glossary" / "overlays" / "governance"


SUBSTANTIVE_AUTHORITY_SCOPES = {
    'access_decisioning',
    'assurance_and_audit',
    'credential_issuance',
    'delegation_and_scope',
    'governance_recognition',
    'policy_definition',
    'registry_management',
    'verification_and_reliance',
}
SUBSTANTIVE_DECISION_POINTS = {
    'access_decision',
    'delegation_grant',
    'issuance_decision',
    'policy_approval',
    'registration_decision',
    'reliance_decision',
    'revocation_decision',
}



def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "term"


def load_terms():
    terms = []
    for path in sorted(TERMS_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if data:
            data["slug"] = slugify(path.stem)
            terms.append(data)
    return terms


def build_jsonld(terms):
    graph = []
    for term in terms:
        graph.append({
            "@type": "DefinedTerm",
            "@id": f"urn:toip:glossary:{term['slug']}",
            "name": term.get("term"),
            "description": term.get("definition"),
            "inDefinedTermSet": "ToIP Main Glossary",
            "identifier": term.get("term"),
            "subjectOf": {
                "governance": term.get("governance", {}),
                "assurance": term.get("assurance", {}),
                "control_plane": term.get("control_plane", {}),
                "crosswalk": term.get("crosswalk", {})
            }
        })
    return {
        "@context": "https://schema.org",
        "@type": "DefinedTermSet",
        "name": "ToIP Main Glossary",
        "@graph": graph
    }


def build_markdown(terms):
    lines = ["# Governance-Executable Glossary", "", f"Total terms: **{len(terms)}**", ""]
    for term in terms:
        lines.append(f"## {term.get('term', 'Untitled Term')}")
        lines.append("")
        lines.append(term.get("definition", ""))
        lines.append("")
        gov = term.get("governance", {})
        assurance = term.get("assurance", {})
        control = term.get("control_plane", {})
        lines.append(f"- Slug: `{term.get('slug')}`")
        lines.append(f"- Governance profile: {term.get('governance_profile') or 'Not specified'}")
        lines.append(f"- Authority scope: {', '.join(gov.get('authority_scope', [])) or 'Not specified'}")
        lines.append(f"- Delegation mode: {gov.get('delegation_mode', 'Not specified')}")
        lines.append(f"- Revocation supported: {gov.get('revocation_supported', 'Not specified')}")
        lines.append(f"- Lifecycle states: {', '.join(gov.get('lifecycle_states', [])) or 'Not specified'}")
        lines.append(f"- Assurance level hint: {assurance.get('assurance_level_hint', 'Not specified')}")
        lines.append(f"- Accountable entity: {control.get('accountable_entity', 'Not specified')}")
        lines.append("")
    return "\n".join(lines)


def classify_terms(terms):
    inventory = {
        "term_count": len(terms),
        "authority_terms": [],
        "delegation_terms": [],
        "revocation_terms": [],
        "lifecycle_terms": [],
        "evidence_terms": [],
        "control_plane_terms": [],
        "governance_profiles": defaultdict(list),
        "assurance_level_hints": Counter(),
        "authority_scope_counts": Counter(),
        "evidence_artifact_counts": Counter(),
        "decision_point_counts": Counter(),
    }

    for term in terms:
        slug = term["slug"]
        name = term.get("term")
        gov = term.get("governance", {})
        assurance = term.get("assurance", {})
        control = term.get("control_plane", {})
        profile = term.get("governance_profile") or "unclassified"
        lifecycle_states = [str(s).strip() for s in (gov.get("lifecycle_states") or []) if str(s).strip()]
        evidence_artifacts = [str(s).strip() for s in (assurance.get("evidence_artifacts") or []) if str(s).strip()]
        control_evidence = [str(s).strip() for s in (control.get("evidence_produced") or []) if str(s).strip()]
        authority_scope = [str(s).strip() for s in (gov.get("authority_scope") or []) if str(s).strip()]
        decision_points = [str(s).strip() for s in (control.get("decision_points") or []) if str(s).strip()]

        record = {"term": name, "slug": slug}
        inventory["governance_profiles"][profile].append(record)
        inventory["assurance_level_hints"][assurance.get("assurance_level_hint") or "unspecified"] += 1
        inventory["authority_scope_counts"].update(authority_scope)
        inventory["evidence_artifact_counts"].update(evidence_artifacts)
        inventory["decision_point_counts"].update(decision_points)

        if any(scope in SUBSTANTIVE_AUTHORITY_SCOPES for scope in authority_scope):
            inventory["authority_terms"].append(record)
        delegation_related = 'delegation_and_scope' in authority_scope or any(
            "delegat" in item.lower() for item in authority_scope + decision_points + lifecycle_states + [name or ""]
        )
        if delegation_related:
            inventory["delegation_terms"].append(record)
        if gov.get("revocation_supported"):
            inventory["revocation_terms"].append(record)
        if lifecycle_states:
            inventory["lifecycle_terms"].append({**record, "states": lifecycle_states})
        if evidence_artifacts or control_evidence:
            inventory["evidence_terms"].append({**record, "evidence_artifacts": sorted(set(evidence_artifacts + control_evidence))})
        if gov.get("control_plane_role") == 'decision_plane_component' or any(dp in SUBSTANTIVE_DECISION_POINTS for dp in decision_points):
            inventory["control_plane_terms"].append({**record, "decision_points": decision_points})

    inventory["governance_profiles"] = {
        key: sorted(value, key=lambda item: item["term"].lower())
        for key, value in sorted(inventory["governance_profiles"].items())
    }
    for key in [
        "authority_terms", "delegation_terms", "revocation_terms", "lifecycle_terms", "evidence_terms", "control_plane_terms"
    ]:
        inventory[key] = sorted(inventory[key], key=lambda item: item["term"].lower())
    inventory["assurance_level_hints"] = dict(sorted(inventory["assurance_level_hints"].items()))
    inventory["authority_scope_counts"] = dict(sorted(inventory["authority_scope_counts"].items()))
    inventory["evidence_artifact_counts"] = dict(sorted(inventory["evidence_artifact_counts"].items()))
    inventory["decision_point_counts"] = dict(sorted(inventory["decision_point_counts"].items()))
    return inventory


def render_inventory_markdown(inventory):
    lines = [
        "# Governance Inventory",
        "",
        f"Total terms: **{inventory['term_count']}**",
        "",
        "## Coverage summary",
        "",
        f"- Authority-bearing terms: **{len(inventory['authority_terms'])}**",
        f"- Delegation-sensitive terms: **{len(inventory['delegation_terms'])}**",
        f"- Revocation-sensitive terms: **{len(inventory['revocation_terms'])}**",
        f"- Lifecycle-sensitive terms: **{len(inventory['lifecycle_terms'])}**",
        f"- Evidence-producing terms: **{len(inventory['evidence_terms'])}**",
        f"- Control-plane terms: **{len(inventory['control_plane_terms'])}**",
        "",
        "## Governance profiles",
        "",
    ]
    for profile, items in inventory["governance_profiles"].items():
        lines.append(f"### {profile}")
        lines.append("")
        lines.append(f"Count: **{len(items)}**")
        lines.append("")
        sample = ", ".join(item["term"] for item in items[:20])
        lines.append(sample or "None")
        lines.append("")

    def add_section(title, items, detail_key=None):
        lines.append(f"## {title}")
        lines.append("")
        for item in items[:100]:
            if detail_key and item.get(detail_key):
                detail = ", ".join(item[detail_key])
                lines.append(f"- **{item['term']}** — {detail}")
            else:
                lines.append(f"- {item['term']}")
        if len(items) > 100:
            lines.append(f"- ... and {len(items) - 100} more")
        lines.append("")

    add_section("Authority-bearing terms", inventory["authority_terms"])
    add_section("Delegation-sensitive terms", inventory["delegation_terms"])
    add_section("Revocation-sensitive terms", inventory["revocation_terms"])
    add_section("Lifecycle-sensitive terms", inventory["lifecycle_terms"], "states")
    add_section("Evidence-producing terms", inventory["evidence_terms"], "evidence_artifacts")
    add_section("Control-plane terms", inventory["control_plane_terms"], "decision_points")

    lines.append("## Assurance level hints")
    lines.append("")
    for key, count in inventory["assurance_level_hints"].items():
        lines.append(f"- `{key}`: {count}")
    lines.append("")
    return "\n".join(lines)


def render_core_operational_terms(inventory):
    core = inventory["governance_profiles"].get("core-operational", [])
    lines = [
        "# Core Operational Terms",
        "",
        f"Count: **{len(core)}**",
        "",
        "This generated view lists terms currently classified under the `core-operational` governance profile.",
        "",
    ]
    for item in core:
        lines.append(f"- {item['term']}")
    lines.append("")
    return "\n".join(lines)


def main():
    terms = load_terms()
    JSON_OUT.mkdir(parents=True, exist_ok=True)
    MD_OUT.mkdir(parents=True, exist_ok=True)
    OVERLAY_GOV.mkdir(parents=True, exist_ok=True)

    inventory = classify_terms(terms)

    (JSON_OUT / "governance-executable-glossary.json").write_text(json.dumps({"terms": terms}, indent=2), encoding="utf-8")
    (JSON_OUT / "governance-executable-glossary.catalog.json").write_text(json.dumps({
        "term_count": len(terms),
        "terms": [{
            "term": t.get("term"),
            "slug": t.get("slug"),
            "source_file": t.get("source_file"),
            "governance_profile": t.get("governance_profile"),
            "assurance_level_hint": (t.get("assurance") or {}).get("assurance_level_hint")
        } for t in terms]
    }, indent=2), encoding="utf-8")
    (JSON_OUT / "governance-executable-glossary.jsonld").write_text(json.dumps(build_jsonld(terms), indent=2), encoding="utf-8")
    (JSON_OUT / "governance-inventory.json").write_text(json.dumps(inventory, indent=2), encoding="utf-8")
    (MD_OUT / "governance-executable-glossary.md").write_text(build_markdown(terms), encoding="utf-8")
    (MD_OUT / "governance-inventory.md").write_text(render_inventory_markdown(inventory), encoding="utf-8")
    (OVERLAY_GOV / "inventory.json").write_text(json.dumps(inventory, indent=2), encoding="utf-8")
    (OVERLAY_GOV / "core-operational-terms.md").write_text(render_core_operational_terms(inventory), encoding="utf-8")

    summary = {
        "term_count": len(terms),
        "generated_json": sorted(p.name for p in JSON_OUT.glob("*.json*")),
        "generated_markdown": sorted(p.name for p in MD_OUT.glob("*.md")),
        "overlay_files": sorted(p.name for p in OVERLAY_GOV.glob("*")),
    }
    (JSON_OUT / "build-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"Built bundles and inventories for {len(terms)} terms")


if __name__ == "__main__":
    main()
