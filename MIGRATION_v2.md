# Migrating to Trust Infrastructure Glossary v2

## Project identity

Replace references to `ctwg-main-glossary` with `trust-infrastructure-glossary`.

Canonical repository:

`https://github.com/sankarshanmukhopadhyay/trust-infrastructure-glossary`

Canonical Pages site:

`https://sankarshanmukhopadhyay.github.io/trust-infrastructure-glossary/`

## Concept identity

v1 consumers often keyed entries by `term` or filename slug. v2 consumers should key by `concept_id`.

Example:

```yaml
concept_id: urn:tig:concept:delegation
```

## Labels

Use `designations` rather than assuming one English string is the concept identity.

`term` and `aliases` remain available as compatibility fields in v2.0.0.

## Artifact names

Prefer:

- `generated/json/trust-infrastructure-glossary.json`
- `generated/json/trust-infrastructure-glossary.catalog.json`
- `generated/json/trust-infrastructure-glossary.jsonld`
- `generated/rdf/trust-infrastructure-glossary.ttl`

The older `governance-executable-glossary.*` filenames remain available temporarily for migration.

## Provenance

Do not infer authority from source provenance. An adapted ToIP concept is a TIG concept whose lineage is ToIP-derived; it is not automatically governed by current ToIP terminology.

## Mappings

Do not convert a source citation into an `exact` mapping automatically. Mapping strength requires semantic review.

## Profiles

Downstream projects can pin a TIG release and consume a bounded profile from `profiles/` instead of importing the complete concept set.
