---
title: "sd-jwt-vc"
---

# sd-jwt-vc

A verifiable credential encoded using Selective Disclosure JWT mechanisms, enabling selected claims to be disclosed while preserving cryptographic verification.

## Formal definition
A verifiable credential encoded using Selective Disclosure JWT mechanisms, enabling selected claims to be disclosed while preserving cryptographic verification.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **SD-JWT VC** (`en`, `alternative`)
- **SD-JWT-based Verifiable Credential** (`en`, `alternative`)

### Related concepts
- [selective-disclosure]({{ '/terms/selective-disclosure/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [secured-verifiable-credential]({{ '/terms/secured-verifiable-credential/' | relative_url }})
- [key-binding-jwt]({{ '/terms/key-binding-jwt/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:selective-disclosure`
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:secured-verifiable-credential`
- **related**: `urn:tig:concept:key-binding-jwt`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:sd-jwt-vc`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
SD-JWT VC, SD-JWT-based Verifiable Credential

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
- **IETF**: RFC 9901
- **OPENID**: OpenID4VCI, OpenID4VP

</details>

---

*Generated from `glossary/terms/sd-jwt-vc.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
