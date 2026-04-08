#!/usr/bin/env python3
"""Build machine-readable and markdown bundles from governance-executable glossary YAML artifacts."""
from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
TERMS_DIR = ROOT / "glossary" / "terms"
JSON_OUT = ROOT / "generated" / "json"
MD_OUT = ROOT / "generated" / "markdown"


def load_terms():
    terms = []
    for path in sorted(TERMS_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if data:
            terms.append(data)
    return terms


def build_jsonld(terms):
    graph = []
    for term in terms:
        graph.append({
            "@type": "DefinedTerm",
            "@id": f"urn:toip:glossary:{term.get('term','').strip().lower().replace(' ', '-')}",
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
        if gov:
            lines.append(f"- Authority scope: {', '.join(gov.get('authority_scope', [])) or 'Not specified'}")
            lines.append(f"- Delegation mode: {gov.get('delegation_mode', 'Not specified')}")
            lines.append(f"- Revocation supported: {gov.get('revocation_supported', 'Not specified')}")
            lines.append("")
    return "\n".join(lines)


def main():
    terms = load_terms()
    JSON_OUT.mkdir(parents=True, exist_ok=True)
    MD_OUT.mkdir(parents=True, exist_ok=True)

    (JSON_OUT / "governance-executable-glossary.json").write_text(json.dumps({"terms": terms}, indent=2), encoding="utf-8")
    (JSON_OUT / "governance-executable-glossary.catalog.json").write_text(json.dumps({
        "term_count": len(terms),
        "terms": [{"term": t.get("term"), "source_file": t.get("source_file"), "governance_profile": t.get("governance_profile")} for t in terms]
    }, indent=2), encoding="utf-8")
    (JSON_OUT / "governance-executable-glossary.jsonld").write_text(json.dumps(build_jsonld(terms), indent=2), encoding="utf-8")
    (MD_OUT / "governance-executable-glossary.md").write_text(build_markdown(terms), encoding="utf-8")

    print(f"Built bundles for {len(terms)} terms")


if __name__ == "__main__":
    main()
