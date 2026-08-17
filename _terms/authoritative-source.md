---
title: "authoritative-source"
---

# authoritative-source

A simple-English summary has not yet been added for this concept.

## Formal definition
A source of information that a relying party considers to be authoritative for that information. In ToIP architecture, the trust registry authorized by the governance framework for a trust community is typically considered an authoritative source by the members of that trust community. A system of record is an authoritative source for the data records it holds. A trust anchor is an authoritative source for the beginning of a trust chain.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **authoritative source** (`en`, `alternative`)
- **authoritative sources** (`en`, `alternative`)

### Related concepts
- [verification]({{ '/terms/verification/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})
- [relying-party]({{ '/terms/relying-party/' | relative_url }})
- [trust-decision]({{ '/terms/trust-decision/' | relative_url }})
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:verification`
- **related**: `urn:tig:concept:verifier`
- **related**: `urn:tig:concept:relying-party`
- **related**: `urn:tig:concept:trust-decision`
- **related**: `urn:tig:concept:policy`
- **related**: `urn:tig:concept:governance-framework`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:authoritative-source`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/authoritative-source.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
authoritative source, authoritative sources

### Governance profile
- **Authority scope**: verification_and_reliance, policy_definition, registry_management, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- registration_decision
- reliance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- policy_document
- registry_entry
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- policy_approval
- registration_decision
- reliance_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- registry_entry
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

*Generated from `glossary/terms/authoritative-source.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
