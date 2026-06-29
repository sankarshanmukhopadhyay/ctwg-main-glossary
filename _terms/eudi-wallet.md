---
title: "eudi-wallet"
---

> Generated file. Update `glossary/terms/eudi-wallet.yaml` and regenerate artifacts instead of editing this page directly.

# eudi-wallet

## Definition
A wallet ecosystem component under the European Digital Identity framework for storing and presenting person identification data, attestations, and credentials across EU contexts.

## Reader Note
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

## Implementation Relevance
Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Aliases
European Digital Identity Wallet, EUDI Wallet, EUDIW

## See Also
- [digital-wallet]({{ '/terms/digital-wallet/' | relative_url }})
- [pid]({{ '/terms/pid/' | relative_url }})
- [qualified-electronic-attestation-of-attributes]({{ '/terms/qualified-electronic-attestation-of-attributes/' | relative_url }})
- [eidas]({{ '/terms/eidas/' | relative_url }})

## Standards and Source References
- [EUDI Wallet Architecture and Reference Framework 2.0](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) (European Commission; Architecture Reference Framework; 2.0; 2025-05-29) — normative

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- reliance_decision
- registration_decision

## Assurance
**Evidence artifacts**
- policy_document
- issuance_log
- verification_log
- registry_entry
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
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

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **EU**: EUDI ARF 2.0, eIDAS 2.0
- **OPENID**: OpenID4VCI, OpenID4VP
