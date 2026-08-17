---
title: "data-schema"
---

# data-schema

A simple-English summary has not yet been added for this concept.

## Formal definition
A description of the structure of a digital document or object, typically expressed in a machine-readable language in terms of constraints on the structure and content of documents or objects of that type. A credential schema is a particular type of data schema.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **data schema** (`en`, `alternative`)
- **data schemas** (`en`, `alternative`)

### Related concepts
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:credential`
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:issuance`
- **related**: `urn:tig:concept:verifiable-credential`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:data-schema`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/data-schema.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
data schema, data schemas

### Governance profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: design
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

### Notes
Not specified

### Supporting definitions
- [Wikipedia](https://en.wikipedia.org/wiki/XML_schema): An XML schema is a description of a type of [XML](https://en.wikipedia.org/wiki/Extensible_Markup_Language) document, typically expressed in terms of constraints on the structure and content of documents of that type, above and beyond the basic syntactical constraints imposed by XML itself. These constraints are generally expressed using some combination of grammatical rules governing the order of elements, [Boolean predicates](https://en.wikipedia.org/wiki/Boolean_predicates) that the content must satisfy, data types governing the content of elements and attributes, and more specialized rules such as [uniqueness](https://en.wikipedia.org/wiki/Uniqueness_quantification) and [referential integrity](https://en.wikipedia.org/wiki/Referential_integrity) constraints.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/data-schema.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
