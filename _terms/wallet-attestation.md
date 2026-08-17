---
title: "wallet-attestation"
---

# wallet-attestation

Evidence about a wallet instance, wallet provider, or wallet capability that can be used by issuers, verifiers, or governance frameworks to make reliance decisions.

## Formal definition
Evidence about a wallet instance, wallet provider, or wallet capability that can be used by issuers, verifiers, or governance frameworks to make reliance decisions.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **wallet attestation** (`en`, `alternative`)

### Related concepts
- [digital-wallet]({{ '/terms/digital-wallet/' | relative_url }})
- [attestation]({{ '/terms/attestation/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})
- [assurance-level]({{ '/terms/assurance-level/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:digital-wallet`
- **related**: `urn:tig:concept:attestation`
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:verifier`
- **related**: `urn:tig:concept:assurance-level`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:wallet-attestation`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [EUDI Wallet Architecture and Reference Framework 2.0](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) (European Commission; Architecture Reference Framework; 2.0; 2025-05-29) — normative
- [OpenID for Verifiable Credential Issuance 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2025-09-16) — normative
- [OpenID for Verifiable Presentations 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2025-07-09) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
wallet attestation

### Governance profile
- **Authority scope**: assurance_and_audit, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision
- issuance_decision

### Assurance
**Evidence artifacts**
- attestation
- verification_log
- audit_log
- policy_document

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision
- issuance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- attestation
- verification_log
- audit_log
- policy_document

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **EU**: EUDI ARF 2.0
- **OPENID**: OpenID4VCI, OpenID4VP

</details>

---

*Generated from `glossary/terms/wallet-attestation.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
