#!/usr/bin/env python3
"""Build governance quality reports for the glossary source layer."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
TERMS_DIR = ROOT / "glossary" / "terms"
JSON_OUT = ROOT / "generated" / "json"
MD_OUT = ROOT / "generated" / "markdown"
GOV_OUT = ROOT / "governance"

GENERIC_EVIDENCE = {"definition_change_record"}
HIGH_IMPACT_DECISIONS = {
    "access_decision",
    "delegation_grant",
    "issuance_decision",
    "registration_decision",
    "reliance_decision",
    "revocation_decision",
}
REVOCATION_EVIDENCE = {"status_record", "audit_log", "verification_log", "registry_entry"}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "term"


def load_terms() -> list[dict]:
    terms = []
    for path in sorted(TERMS_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        data["slug"] = slugify(path.stem)
        data["path"] = str(path.relative_to(ROOT))
        terms.append(data)
    return terms


def issue(term: dict, severity: str, code: str, message: str, recommendation: str) -> dict:
    return {
        "term": term.get("term"),
        "slug": term.get("slug"),
        "path": term.get("path"),
        "severity": severity,
        "code": code,
        "message": message,
        "recommendation": recommendation,
    }


def circular_definition(term: dict) -> bool:
    name = str(term.get("term", "")).strip().lower()
    definition = str(term.get("definition", "")).strip().lower()
    if not name or not definition:
        return False
    cleaned_name = re.sub(r"[^a-z0-9 ]+", " ", name)
    cleaned_definition = re.sub(r"[^a-z0-9 ]+", " ", definition)
    words = [w for w in cleaned_name.split() if len(w) > 3]
    if not words:
        return False
    starts_with_name = cleaned_definition.startswith(cleaned_name)
    few_non_term_words = len([w for w in cleaned_definition.split() if w not in words]) <= 5
    return starts_with_name and few_non_term_words


def build_report(terms: list[dict]) -> dict:
    issues = []
    counters = Counter()
    severity_counts = Counter()

    for term in terms:
        gov = term.get("governance") or {}
        assurance = term.get("assurance") or {}
        control = term.get("control_plane") or {}
        sources = term.get("sources") or []
        see_also = term.get("see_also") or []
        evidence = set(assurance.get("evidence_artifacts") or [])
        control_evidence = set(control.get("evidence_produced") or [])
        combined_evidence = evidence | control_evidence
        decisions = set(control.get("decision_points") or [])
        enforcement = set(gov.get("enforcement_points") or [])
        hint = assurance.get("assurance_level_hint")
        profile = term.get("governance_profile")

        if not sources:
            issues.append(issue(term, "medium", "missing_sources", "Term has no source references.", "Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows."))
        if not see_also:
            issues.append(issue(term, "low", "missing_see_also", "Term has no see_also references.", "Add related terms where cross-reference navigation would improve interpretation or downstream mapping."))
        if not combined_evidence:
            issues.append(issue(term, "high", "missing_evidence", "Term has no evidence artifacts.", "Define the evidence produced or consumed when this term participates in governance decisions."))
        elif combined_evidence <= GENERIC_EVIDENCE and profile != "descriptive":
            issues.append(issue(term, "medium", "generic_evidence", "Operational or governance-supporting term only references generic definition-change evidence.", "Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable."))
        if gov.get("revocation_supported") and not (combined_evidence & REVOCATION_EVIDENCE):
            issues.append(issue(term, "high", "weak_revocation_evidence", "Revocation is supported but evidence does not include status, audit, verification, or registry evidence.", "Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable."))
        if gov.get("control_plane_role") == "decision_plane_component" and hint in {"informative", None}:
            issues.append(issue(term, "medium", "decision_plane_low_assurance", "Decision-plane term has an informative or missing assurance hint.", "Raise the assurance hint or document why the term is only descriptive despite affecting decisions."))
        if decisions & HIGH_IMPACT_DECISIONS and hint == "informative":
            issues.append(issue(term, "medium", "high_impact_informative", "High-impact decision point is paired with informative assurance hint.", "Use AL1+ or AL2+ when the term can affect authority, reliance, issuance, delegation, access, or revocation decisions."))
        if decisions and not enforcement:
            issues.append(issue(term, "medium", "decision_without_enforcement", "Term has decision points but no enforcement points.", "Align decision_points and enforcement_points so downstream implementers can test where governance becomes operational."))
        if circular_definition(term):
            issues.append(issue(term, "low", "possibly_circular_definition", "Definition may be circular or too close to the term label.", "Rewrite the definition to state the operational meaning, boundary, and governance relevance of the term."))

        counters["with_sources"] += bool(sources)
        counters["with_see_also"] += bool(see_also)
        counters["with_evidence"] += bool(combined_evidence)
        counters["revocation_supported"] += bool(gov.get("revocation_supported"))
        counters["decision_plane_component"] += gov.get("control_plane_role") == "decision_plane_component"

    for item in issues:
        severity_counts[item["severity"]] += 1

    quality_score = 100
    if terms:
        high = severity_counts.get("high", 0)
        medium = severity_counts.get("medium", 0)
        low = severity_counts.get("low", 0)
        quality_score = max(0, round(100 - ((high * 2.0 + medium * 1.0 + low * 0.25) / len(terms) * 10), 1))

    return {
        "report_type": "governance_quality_report",
        "version": "1.1.0",
        "term_count": len(terms),
        "quality_score": quality_score,
        "summary": {
            "issue_count": len(issues),
            "severity_counts": dict(sorted(severity_counts.items())),
            "coverage": dict(sorted(counters.items())),
        },
        "issue_codes": {
            "missing_sources": "No source references are present.",
            "missing_see_also": "No cross-reference terms are present.",
            "missing_evidence": "No evidence artifacts are present.",
            "generic_evidence": "Only generic definition-change evidence is present for a non-descriptive term.",
            "weak_revocation_evidence": "Revocation semantics are not backed by revocation-relevant evidence.",
            "decision_plane_low_assurance": "Decision-plane role is paired with a low assurance hint.",
            "high_impact_informative": "High-impact decision point is paired with informative assurance.",
            "decision_without_enforcement": "Decision points are not paired with enforcement points.",
            "possibly_circular_definition": "Definition appears too close to the term label.",
        },
        "issues": issues,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Governance Quality Report",
        "",
        "> Generated file. Update `glossary/terms/` or `tools/build_quality_report.py` and regenerate artifacts instead of editing this report directly.",
        "",
        "This report is an assurance-readiness view over the structured glossary source layer. It does not certify the glossary. It identifies evidence, attribution, cross-reference, revocation, and assurance-quality gaps that maintainers can prioritize.",
        "",
        "## Summary",
        "",
        f"- Terms evaluated: **{report['term_count']}**",
        f"- Quality score: **{report['quality_score']} / 100**",
        f"- Total findings: **{report['summary']['issue_count']}**",
        "",
        "## Severity counts",
        "",
    ]
    severity = report["summary"].get("severity_counts", {})
    for key in ["high", "medium", "low"]:
        lines.append(f"- `{key}`: {severity.get(key, 0)}")
    lines.extend(["", "## Coverage", ""])
    for key, value in report["summary"].get("coverage", {}).items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Finding categories", ""])
    for code, desc in report.get("issue_codes", {}).items():
        count = sum(1 for item in report["issues"] if item["code"] == code)
        lines.append(f"- `{code}`: {count} — {desc}")
    lines.extend(["", "## Prioritized findings", ""])
    order = {"high": 0, "medium": 1, "low": 2}
    for item in sorted(report["issues"], key=lambda x: (order.get(x["severity"], 9), x["code"], x["term"] or ""))[:250]:
        lines.append(f"### {item['term']} — `{item['code']}`")
        lines.append("")
        lines.append(f"- Severity: **{item['severity']}**")
        lines.append(f"- Source: `{item['path']}`")
        lines.append(f"- Finding: {item['message']}")
        lines.append(f"- Recommended action: {item['recommendation']}")
        lines.append("")
    if len(report["issues"]) > 250:
        lines.append(f"Additional findings omitted from this markdown view: **{len(report['issues']) - 250}**. See `generated/json/governance-quality-report.json` for the complete machine-readable report.")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    terms = load_terms()
    JSON_OUT.mkdir(parents=True, exist_ok=True)
    MD_OUT.mkdir(parents=True, exist_ok=True)
    GOV_OUT.mkdir(parents=True, exist_ok=True)
    report = build_report(terms)
    markdown = render_markdown(report)
    (JSON_OUT / "governance-quality-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (MD_OUT / "governance-quality-report.md").write_text(markdown, encoding="utf-8")
    page = """---
title: "Governance Quality Report"
parent: Governance Documentation
nav_order: 21
---

""" + markdown
    (GOV_OUT / "quality-report.md").write_text(page, encoding="utf-8")
    print(f"Built governance quality report with {report['summary']['issue_count']} findings")


if __name__ == "__main__":
    main()
