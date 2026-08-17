---
title: "authorization-graph"
---

# authorization-graph

A simple-English summary has not yet been added for this concept.

## Formal definition
A graph of the authorization relationships between different entities in a trust-community. In a digital trust ecosystem, the governing body is typically the trust root of an authorization graph. In some cases, an authorization graph can be traversed by making queries to one or more trust registries.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **authorization graph** (`en`, `alternative`)

### Related concepts
- [governance graph]({{ '/terms/governance-graph/' | relative_url }})
- [reputation graph]({{ '/terms/reputation-graph/' | relative_url }})
- [trust graph]({{ '/terms/trust-graph/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:governance-graph`
- **related**: `urn:tig:concept:reputation-graph`
- **related**: `urn:tig:concept:trust-graph`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:authorization-graph`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/authorization-graph.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
authorization graph

### Governance profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- access_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

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

*Generated from `glossary/terms/authorization-graph.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
