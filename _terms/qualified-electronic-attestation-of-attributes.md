---
title: "qualified-electronic-attestation-of-attributes"
---

# qualified-electronic-attestation-of-attributes

An attestation of attributes issued under qualified trust service rules in the European digital identity framework.

## Formal definition
An attestation of attributes issued under qualified trust service rules in the European digital identity framework.

## Why this concept matters
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Names and relationships

### Alternative designations
- **QEAA** (`en`, `alternative`)
- **qualified attribute attestation** (`en`, `alternative`)

### Related concepts
- [attestation]({{ '/terms/attestation/' | relative_url }})
- [eudi-wallet]({{ '/terms/eudi-wallet/' | relative_url }})
- [trust-service-provider]({{ '/terms/trust-service-provider/' | relative_url }})
- [credential]({{ '/terms/credential/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:attestation`
- **related**: `urn:tig:concept:eudi-wallet`
- **related**: `urn:tig:concept:trust-service-provider`
- **related**: `urn:tig:concept:credential`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:qualified-electronic-attestation-of-attributes`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [EUDI Wallet Architecture and Reference Framework 2.0](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) (European Commission; Architecture Reference Framework; 2.0; 2025-05-29) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
QEAA, qualified attribute attestation

### Governance profile
- **Authority scope**: credential_issuance, governance_recognition, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision
- registration_decision
- reliance_decision

### Assurance
**Evidence artifacts**
- attestation
- issuance_log
- registry_entry
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- issuance_decision
- registration_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- attestation
- issuance_log
- registry_entry
- verification_log
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **EU**: EUDI ARF 2.0, eIDAS 2.0

</details>

---

*Generated from `glossary/terms/qualified-electronic-attestation-of-attributes.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
