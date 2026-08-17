---
title: "qualified-electronic-attestation-of-attributes"
---

> Generated file. Update `glossary/terms/qualified-electronic-attestation-of-attributes.yaml` and regenerate artifacts instead of editing this page directly.

# qualified-electronic-attestation-of-attributes

## Concept Identity
- **Concept ID**: `urn:tig:concept:qualified-electronic-attestation-of-attributes`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
An attestation of attributes issued under qualified trust service rules in the European digital identity framework.

## Definition
An attestation of attributes issued under qualified trust service rules in the European digital identity framework.

## Reader Note
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

## Implementation Relevance
Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Alternative Designations
- **QEAA** (`en`, `alternative`)
- **qualified attribute attestation** (`en`, `alternative`)

## Legacy Aliases
QEAA, qualified attribute attestation

## Semantic Relations
- **related**: `urn:tig:concept:attestation`
- **related**: `urn:tig:concept:eudi-wallet`
- **related**: `urn:tig:concept:trust-service-provider`
- **related**: `urn:tig:concept:credential`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [attestation]({{ '/terms/attestation/' | relative_url }})
- [eudi-wallet]({{ '/terms/eudi-wallet/' | relative_url }})
- [trust-service-provider]({{ '/terms/trust-service-provider/' | relative_url }})
- [credential]({{ '/terms/credential/' | relative_url }})

## Standards and Source References
- [EUDI Wallet Architecture and Reference Framework 2.0](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) (European Commission; Architecture Reference Framework; 2.0; 2025-05-29) — normative

## Governance Profile
- **Authority scope**: credential_issuance, governance_recognition, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- registration_decision
- reliance_decision

## Assurance
**Evidence artifacts**
- attestation
- issuance_log
- registry_entry
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
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

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **EU**: EUDI ARF 2.0, eIDAS 2.0
