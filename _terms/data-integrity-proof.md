---
title: "data-integrity-proof"
---

# data-integrity-proof

A cryptographic proof mechanism used to protect the authenticity and integrity of verifiable credentials and similar constrained digital documents.

## Formal definition
A cryptographic proof mechanism used to protect the authenticity and integrity of verifiable credentials and similar constrained digital documents.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **Data Integrity proof** (`en`, `alternative`)
- **VC Data Integrity proof** (`en`, `alternative`)

### Related concepts
- [digital-signature]({{ '/terms/digital-signature/' | relative_url }})
- [cryptographic-verifiability]({{ '/terms/cryptographic-verifiability/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [proof]({{ '/terms/proof/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:digital-signature`
- **related**: `urn:tig:concept:cryptographic-verifiability`
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:proof`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:data-integrity-proof`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Verifiable Credential Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/) (W3C; Recommendation; 1.0; 2025-05-15) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
Data Integrity proof, VC Data Integrity proof

### Governance profile
- **Authority scope**: verification_and_reliance, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision

### Assurance
**Evidence artifacts**
- verification_log
- audit_log
- attestation

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log
- audit_log
- attestation

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **W3C**: Verifiable Credential Data Integrity 1.0

</details>

---

*Generated from `glossary/terms/data-integrity-proof.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
