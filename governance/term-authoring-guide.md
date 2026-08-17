---
title: "Concept Authoring Guide"
parent: "Semantic Model & Authoring"
nav_order: 2
grand_parent: "Govern TIG"
---

# Concept Authoring Guide

TIG v2 treats the concept as the semantic object and the label as a designation.

## Required v2 shape

```yaml
schema_version: "2.0"
concept_id: urn:tig:concept:example-concept
designations:
  - label: example concept
    language: en
    status: preferred

term: example concept        # v1 compatibility
aliases: []                  # v1 compatibility
definition: A precise formal definition.
simple_definition: A shorter reader-facing explanation.

editorial:
  status: stable
  reviewed:
    domain: true
    plain_language: true
    governance: true

provenance:
  classification: locally_defined
  source_corpus: Trust Infrastructure Glossary
  lineage_note: Independently defined for TIG.

semantic_relations:
  related:
    - urn:tig:concept:another-concept

concept_mappings:
  exact: []
  close: []
  broad: []
  narrow: []
  related: []
```

Governance, assurance, control-plane, source, crosswalk, and implementation metadata continue below this semantic layer.

## Identifier rule

A published `concept_id` is stable. Changing the preferred wording does not justify changing the identifier. Never reuse an identifier for a different concept.

## Mapping rule

Use `exact` only when two concepts can be used interchangeably across the intended mapping scope. Prefer `close` when there is any material difference in scope or meaning.

## Provenance rule

Use:

- `adopted` for intentionally carried source material;
- `adapted` where external material materially informed TIG but TIG changed scope or expression;
- `locally_defined` for TIG-defined concepts;
- `mapped` when an independent TIG concept is primarily connected to an external concept through semantic mapping.

## Plain language

A simple definition is a comprehension aid, not a substitute for the formal semantic contract.

## Validation

```bash
python tools/validate_governance_glossary.py
python tools/validate_profiles.py
python tools/build_governance_glossary.py
python tools/build_quality_report.py
python tools/build_jekyll_site.py
```
