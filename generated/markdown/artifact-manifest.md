# Artifact Manifest

> Generated file. Update `tools/build_governance_glossary.py` and regenerate artifacts instead of editing this manifest directly.

Terms covered: **534**

| Artifact | Type | Origin | Generator | Consumer use case | Stability |
|---|---|---|---|---|---|
| `generated/json/governance-executable-glossary.json` | `json_bundle` | `generated` | `tools/build_governance_glossary.py` | Complete machine-readable glossary corpus for indexing, policy mapping, and downstream assurance tooling. | `stable_generated` |
| `generated/json/governance-executable-glossary.catalog.json` | `json_catalog` | `generated` | `tools/build_governance_glossary.py` | Lightweight term discovery, version comparison, and adoption dashboards. | `stable_generated` |
| `generated/json/governance-executable-glossary.jsonld` | `jsonld_bundle` | `generated` | `tools/build_governance_glossary.py` | Linked-data publication of defined terms and governance metadata. | `experimental_semantic_mapping` |
| `generated/json/governance-inventory.json` | `json_inventory` | `generated` | `tools/build_governance_glossary.py` | Authority, delegation, revocation, lifecycle, evidence, and control-plane coverage analysis. | `stable_generated` |
| `generated/json/governance-quality-report.json` | `json_quality_report` | `generated` | `tools/build_quality_report.py` | Assurance-readiness findings for source attribution, evidence quality, revocation inspectability, and term cross-reference hygiene. | `stable_generated` |
| `generated/markdown/governance-executable-glossary.md` | `markdown_bundle` | `generated` | `tools/build_governance_glossary.py` | Human-readable full corpus export. | `stable_generated` |
| `generated/markdown/governance-inventory.md` | `markdown_inventory` | `generated` | `tools/build_governance_glossary.py` | Maintainer-readable governance inventory review. | `stable_generated` |
| `generated/markdown/governance-quality-report.md` | `markdown_quality_report` | `generated` | `tools/build_quality_report.py` | Maintainer-readable quality and assurance-readiness review. | `stable_generated` |
| `_terms/*.md` | `jekyll_collection_pages` | `generated` | `tools/build_jekyll_site.py` | Published GitHub Pages term pages. | `stable_generated` |
