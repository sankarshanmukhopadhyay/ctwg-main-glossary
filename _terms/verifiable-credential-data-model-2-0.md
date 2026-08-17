---
title: "verifiable-credential-data-model-2-0"
---

# verifiable-credential-data-model-2-0

The W3C data model for expressing verifiable credentials and verifiable presentations using common roles, properties, lifecycle semantics, and securing mechanisms.

## Formal definition
The W3C data model for expressing verifiable credentials and verifiable presentations using common roles, properties, lifecycle semantics, and securing mechanisms.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this term when distinguishing the W3C credential data model from credential transport protocols and credential securing formats.

## Names and relationships

### Alternative designations
- **VC Data Model 2.0** (`en`, `alternative`)
- **VCDM 2.0** (`en`, `alternative`)

### Related concepts
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [verifiable-presentation]({{ '/terms/verifiable-presentation/' | relative_url }})
- [data-integrity-proof]({{ '/terms/data-integrity-proof/' | relative_url }})
- [secured-verifiable-credential]({{ '/terms/secured-verifiable-credential/' | relative_url }})
- [bitstring-status-list]({{ '/terms/bitstring-status-list/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:verifiable-presentation`
- **related**: `urn:tig:concept:data-integrity-proof`
- **related**: `urn:tig:concept:secured-verifiable-credential`
- **related**: `urn:tig:concept:bitstring-status-list`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:verifiable-credential-data-model-2-0`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (W3C; Recommendation; 2.0; 2025-05-15) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
VC Data Model 2.0, VCDM 2.0

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
- policy_document
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
- policy_document
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
- **W3C**: VC Data Model v2.0
- **OPENID**: OpenID4VCI, OpenID4VP
- **IETF**: SD-JWT VC

</details>

---

*Generated from `glossary/terms/verifiable-credential-data-model-2-0.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
