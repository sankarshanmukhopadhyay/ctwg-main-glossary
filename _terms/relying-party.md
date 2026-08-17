---
title: "relying-party"
---

# relying-party

A simple-English summary has not yet been added for this concept.

## Formal definition
A party who accepts claims, credentials, trust graphs, or any other form of verifiable data from other parties (such as issuers, holders, trust registries, or other authoritative sources) in order to make a trust decision.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **relying party** (`en`, `alternative`)
- **relying parties** (`en`, `alternative`)

### Related concepts
- [verifier]({{ '/terms/verifier/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:verifier`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:relying-party`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/relying-party.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
relying party, relying parties

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: issuer_operator

**Evidence produced**
- issuance_log
- verification_log

### Notes
- The term “relying party” is more commonly used in federated identity architecture; the term “verifier” is more commonly used with decentralized identity architecture and verifiable credentials.

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/relying-party.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
