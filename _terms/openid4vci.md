---
title: "openid4vci"
---

# openid4vci

An OpenID Foundation protocol that defines OAuth 2.0-based mechanisms for issuing verifiable credentials from credential issuers to wallets.

## Formal definition
An OpenID Foundation protocol that defines OAuth 2.0-based mechanisms for issuing verifiable credentials from credential issuers to wallets.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **OpenID4VCI** (`en`, `alternative`)
- **OID4VCI** (`en`, `alternative`)

### Related concepts
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [credential-offer]({{ '/terms/credential-offer/' | relative_url }})
- [credential-request]({{ '/terms/credential-request/' | relative_url }})
- [digital-wallet]({{ '/terms/digital-wallet/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:credential-offer`
- **related**: `urn:tig:concept:credential-request`
- **related**: `urn:tig:concept:digital-wallet`
- **related**: `urn:tig:concept:verifiable-credential`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:openid4vci`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [OpenID for Verifiable Credential Issuance 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2025-09-16) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
OpenID4VCI, OID4VCI

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
- policy_document
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
- policy_document
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **OPENID**: OpenID4VCI 1.0

</details>

---

*Generated from `glossary/terms/openid4vci.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
