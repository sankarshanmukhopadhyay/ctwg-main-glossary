---
title: "secured-verifiable-credential"
---

# secured-verifiable-credential

A simple-English summary has not yet been added for this concept.

## Formal definition
A verifiable credential protected by a securing mechanism such as Data Integrity proofs, JOSE, COSE, or SD-JWT so that authenticity and integrity can be verified.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **secured VC** (`en`, `alternative`)
- **secured credential** (`en`, `alternative`)

### Related concepts
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [data-integrity-proof]({{ '/terms/data-integrity-proof/' | relative_url }})
- [sd-jwt-vc]({{ '/terms/sd-jwt-vc/' | relative_url }})
- [cryptographic-verifiability]({{ '/terms/cryptographic-verifiability/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:data-integrity-proof`
- **related**: `urn:tig:concept:sd-jwt-vc`
- **related**: `urn:tig:concept:cryptographic-verifiability`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:secured-verifiable-credential`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Securing Verifiable Credentials using JOSE and COSE](https://www.w3.org/TR/vc-jose-cose/) (W3C; Recommendation; 1.0; 2025-05-15) — normative
- [Verifiable Credential Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/) (W3C; Recommendation; 1.0; 2025-05-15) — normative
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
secured VC, secured credential

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision
- reliance_decision

### Assurance
**Evidence artifacts**
- issuance_log
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- issuance_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- verification_log
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **W3C**: VC JOSE COSE, VC Data Integrity
- **IETF**: RFC 9901

</details>

---

*Generated from `glossary/terms/secured-verifiable-credential.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
