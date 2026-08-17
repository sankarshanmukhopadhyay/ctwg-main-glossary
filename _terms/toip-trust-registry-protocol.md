---
title: "toip-trust-registry-protocol"
---

# toip-trust-registry-protocol

A simple-English summary has not yet been added for this concept.

## Formal definition
The open standard trust task protocol defined by the ToIP Foundation to perform the trust task of querying a trust registry. The ToIP Trust Registry Protocol operates at Layer 3 of the ToIP stack.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **ToIP Trust Registry Protocol** (`en`, `alternative`)

### Related concepts
- [registry]({{ '/terms/registry/' | relative_url }})
- [trust-registry]({{ '/terms/trust-registry/' | relative_url }})
- [registration]({{ '/terms/registration/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:registry`
- **related**: `urn:tig:concept:trust-registry`
- **related**: `urn:tig:concept:registration`
- **related**: `urn:tig:concept:governance-framework`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:toip-trust-registry-protocol`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/toip-trust-registry-protocol.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
ToIP Trust Registry Protocol

### Governance profile
- **Authority scope**: registry_management
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- registration_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- registration_decision
- revocation_decision

- **Accountable entity**: registry_operator

**Evidence produced**
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

*Generated from `glossary/terms/toip-trust-registry-protocol.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
