---
title: "Semantic Model"
parent: Governance Documentation
nav_order: 6
---

# Semantic Model

## Core principle

The v2 model separates **concepts** from the words used to name them.

A concept has a stable identity. A designation is a language-tagged label used to refer to that concept. Definitions, relations, mappings, provenance, and governance metadata attach to the concept.

## Stable concept identifiers

Published concepts use repository-stable identifiers of the form:

`urn:tig:concept:<slug>`

Identifiers must not be reassigned to a different meaning. A renamed preferred designation does not change the concept identifier.

## Designations

Each concept has exactly one preferred English designation in v2 and may have additional designations with these states:

- `preferred`
- `alternative`
- `deprecated`
- `discouraged`

`deprecated` means a designation should no longer be used because terminology has evolved. `discouraged` means the concept may still be valid but the particular wording should be avoided.

## Definitions

The formal `definition` remains the semantic anchor. `simple_definition` is a comprehension layer and must not silently broaden or narrow the formal meaning.

## Editorial maturity

Editorial maturity is distinct from lifecycle states described by the concept itself.

Allowed editorial states:

- `proposed`
- `draft`
- `review-needed`
- `stable`
- `deprecated`

## Semantic relations

The model follows the intent of W3C SKOS for:

- `broader`
- `narrower`
- `related`

Relations target stable concept identifiers.

## Cross-vocabulary mappings

Mappings express semantic correspondence with concepts in other vocabularies:

- `exact`
- `close`
- `broad`
- `narrow`
- `related`

`exact` must be used conservatively. Shared wording is not sufficient evidence of semantic equivalence.

## Compatibility fields

`term` and `aliases` remain for v1 consumer compatibility. In v2 they are derived compatibility representations of `designations`; consumers should migrate to `concept_id` and `designations`.
