---
title: "trust-graph"
---

# trust-graph

A simple-English summary has not yet been added for this concept.

## Formal definition
A data structure describing the trust relationship between two or more entities. A simple trust graph may be expressed as a trust list. More complex trust graphs can be recorded or registered in and queried from a trust registry. Trust graphs can also be expressed using trust chains and chained credentials. Trust graphs can enable verifiers and relying parties to make transitive trust decisions.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **trust graph** (`en`, `alternative`)
- **trust graphs** (`en`, `alternative`)

### Related concepts
- [authorization graph]({{ '/terms/authorization-graph/' | relative_url }})
- [governance graph]({{ '/terms/governance-graph/' | relative_url }})
- [reputation graph]({{ '/terms/reputation-graph/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authorization-graph`
- **related**: `urn:tig:concept:governance-graph`
- **related**: `urn:tig:concept:reputation-graph`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:trust-graph`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/trust-graph.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
trust graph, trust graphs

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance, registry_management
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- registration_decision
- reliance_decision
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- registry_entry
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- registration_decision
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: verifier_operator

**Evidence produced**
- registry_entry
- issuance_log
- verification_log

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

*Generated from `glossary/terms/trust-graph.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
