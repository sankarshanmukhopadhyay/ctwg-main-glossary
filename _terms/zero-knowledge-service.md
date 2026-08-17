---
title: "zero-knowledge-service"
---

# zero-knowledge-service

A simple-English summary has not yet been added for this concept.

## Formal definition
In cloud computing, the term “zero-knowledge” refers to an online service that stores, transfers or manipulates data in a way that maintains a high level of confidentiality, where the data is only accessible to the data's owner (the client), and not to the service provider. This is achieved by encrypting the raw data at the client's side or end-to-end (in case there is more than one client), without disclosing the password to the service provider. This means that neither the service provider, nor any third party that might intercept the data, can decrypt and access the data without prior permission, allowing the client a higher degree of privacy than would otherwise be possible. In addition, zero-knowledge services often strive to hold as little metadata as possible, holding only that data that is functionally needed by the service.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **zero-knowledge service** (`en`, `alternative`)
- **zero-knowledge services** (`en`, `alternative`)

### Related concepts
- [glossary]({{ '/terms/glossary/' | relative_url }})
- [definition]({{ '/terms/definition/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:glossary`
- **related**: `urn:tig:concept:definition`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:zero-knowledge-service`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Wikipedia](https://en.wikipedia.org/wiki/Zero-knowledge_service).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
zero-knowledge service, zero-knowledge services

### Governance profile
- **Authority scope**: terminology_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: decision_plane_component

### Enforcement points
- definition_approval

### Assurance
**Evidence artifacts**
- definition_change_record
- policy_document
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- definition_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- definition_change_record
- policy_document
- audit_log

### Notes
Not specified

### Supporting definitions
- Also known as: no knowledge, zero access.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/zero-knowledge-service.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
