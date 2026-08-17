---
title: "verifiable-credential-data-model-2-0"
---

> Generated file. Update `glossary/terms/verifiable-credential-data-model-2-0.yaml` and regenerate artifacts instead of editing this page directly.

# verifiable-credential-data-model-2-0

## Concept Identity
- **Concept ID**: `urn:tig:concept:verifiable-credential-data-model-2-0`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
The W3C data model for expressing verifiable credentials and verifiable presentations using common roles, properties, lifecycle semantics, and securing mechanisms.

## Definition
The W3C data model for expressing verifiable credentials and verifiable presentations using common roles, properties, lifecycle semantics, and securing mechanisms.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term when distinguishing the W3C credential data model from credential transport protocols and credential securing formats.

## Alternative Designations
- **VC Data Model 2.0** (`en`, `alternative`)
- **VCDM 2.0** (`en`, `alternative`)

## Legacy Aliases
VC Data Model 2.0, VCDM 2.0

## Semantic Relations
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:verifiable-presentation`
- **related**: `urn:tig:concept:data-integrity-proof`
- **related**: `urn:tig:concept:secured-verifiable-credential`
- **related**: `urn:tig:concept:bitstring-status-list`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [verifiable-presentation]({{ '/terms/verifiable-presentation/' | relative_url }})
- [data-integrity-proof]({{ '/terms/data-integrity-proof/' | relative_url }})
- [secured-verifiable-credential]({{ '/terms/secured-verifiable-credential/' | relative_url }})
- [bitstring-status-list]({{ '/terms/bitstring-status-list/' | relative_url }})

## Standards and Source References
- [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (W3C; Recommendation; 2.0; 2025-05-15) — normative

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- reliance_decision

## Assurance
**Evidence artifacts**
- policy_document
- issuance_log
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document
- issuance_log
- verification_log
- audit_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **W3C**: VC Data Model v2.0
- **OPENID**: OpenID4VCI, OpenID4VP
- **IETF**: SD-JWT VC
