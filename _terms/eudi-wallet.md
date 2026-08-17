---
title: "eudi-wallet"
---

# eudi-wallet

A wallet ecosystem component under the European Digital Identity framework for storing and presenting person identification data, attestations, and credentials across EU contexts.

## Formal definition
A wallet ecosystem component under the European Digital Identity framework for storing and presenting person identification data, attestations, and credentials across EU contexts.

## Why this concept matters
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Names and relationships

### Alternative designations
- **European Digital Identity Wallet** (`en`, `alternative`)
- **EUDI Wallet** (`en`, `alternative`)
- **EUDIW** (`en`, `alternative`)

### Related concepts
- [digital-wallet]({{ '/terms/digital-wallet/' | relative_url }})
- [pid]({{ '/terms/pid/' | relative_url }})
- [qualified-electronic-attestation-of-attributes]({{ '/terms/qualified-electronic-attestation-of-attributes/' | relative_url }})
- [eidas]({{ '/terms/eidas/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:digital-wallet`
- **related**: `urn:tig:concept:pid`
- **related**: `urn:tig:concept:qualified-electronic-attestation-of-attributes`
- **related**: `urn:tig:concept:eidas`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:eudi-wallet`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [EUDI Wallet Architecture and Reference Framework 2.0](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) (European Commission; Architecture Reference Framework; 2.0; 2025-05-29) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
European Digital Identity Wallet, EUDI Wallet, EUDIW

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision
- reliance_decision
- registration_decision

### Assurance
**Evidence artifacts**
- policy_document
- issuance_log
- verification_log
- registry_entry
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- issuance_decision
- reliance_decision
- registration_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document
- issuance_log
- verification_log
- registry_entry
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **EU**: EUDI ARF 2.0, eIDAS 2.0
- **OPENID**: OpenID4VCI, OpenID4VP

</details>

---

*Generated from `glossary/terms/eudi-wallet.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
