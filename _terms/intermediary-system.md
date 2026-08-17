---
title: "intermediary-system"
---

# intermediary-system

A simple-English summary has not yet been added for this concept.

## Formal definition
An intermediary system routes messages between endpoint systems but is not otherwise involved in the processing of those messages. In the context of end-to-end encryption, intermediary systems cannot decrypt the messages sent between the endpoint systems. In the ToIP stack, intermediary systems operate at ToIP Layer 2, the trust spanning layer. An intermediary system is one of three types of systems defined in the ToIP Technology Architecture Specification; the other two are endpoint systems and supporting systems.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **intermediary system** (`en`, `alternative`)
- **intermediary systems** (`en`, `alternative`)
- **intermediary** (`en`, `alternative`)
- **intermediaries** (`en`, `alternative`)

### Related concepts
- [endpoint system]({{ '/terms/endpoint-system/' | relative_url }})
- [supporting system]({{ '/terms/supporting-system/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:endpoint-system`
- **related**: `urn:tig:concept:supporting-system`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:intermediary-system`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/intermediary-system.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
intermediary system, intermediary systems, intermediary, intermediaries

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

- **Assurance level hint**: AL1+
- **Auditability**: moderate

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
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/intermediary-system.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
