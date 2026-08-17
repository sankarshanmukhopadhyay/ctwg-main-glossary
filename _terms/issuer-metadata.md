---
title: "issuer-metadata"
---

# issuer-metadata

Metadata published by a credential issuer describing issuer capabilities, credential configurations, endpoints, and supported formats.

## Formal definition
Metadata published by a credential issuer describing issuer capabilities, credential configurations, endpoints, and supported formats.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **credential issuer metadata** (`en`, `alternative`)
- **issuer metadata** (`en`, `alternative`)

### Related concepts
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [openid4vci]({{ '/terms/openid4vci/' | relative_url }})
- [credential-schema]({{ '/terms/credential-schema/' | relative_url }})
- [digital-wallet]({{ '/terms/digital-wallet/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:openid4vci`
- **related**: `urn:tig:concept:credential-schema`
- **related**: `urn:tig:concept:digital-wallet`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:issuer-metadata`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [OpenID for Verifiable Credential Issuance 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2025-09-16) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
credential issuer metadata, issuer metadata

### Governance profile
- **Authority scope**: credential_issuance, registry_management
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision
- registration_decision

### Assurance
**Evidence artifacts**
- registry_entry
- policy_document
- issuance_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- issuance_decision
- registration_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- registry_entry
- policy_document
- issuance_log
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

*Generated from `glossary/terms/issuer-metadata.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
