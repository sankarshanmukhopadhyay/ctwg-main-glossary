---
title: "openid4vci"
---

> Generated file. Update `glossary/terms/openid4vci.yaml` and regenerate artifacts instead of editing this page directly.

# openid4vci

## Concept Identity
- **Concept ID**: `urn:tig:concept:openid4vci`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
An OpenID Foundation protocol that defines OAuth 2.0-based mechanisms for issuing verifiable credentials from credential issuers to wallets.

## Definition
An OpenID Foundation protocol that defines OAuth 2.0-based mechanisms for issuing verifiable credentials from credential issuers to wallets.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **OpenID4VCI** (`en`, `alternative`)
- **OID4VCI** (`en`, `alternative`)

## Legacy Aliases
OpenID4VCI, OID4VCI

## Semantic Relations
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:credential-offer`
- **related**: `urn:tig:concept:credential-request`
- **related**: `urn:tig:concept:digital-wallet`
- **related**: `urn:tig:concept:verifiable-credential`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [credential-offer]({{ '/terms/credential-offer/' | relative_url }})
- [credential-request]({{ '/terms/credential-request/' | relative_url }})
- [digital-wallet]({{ '/terms/digital-wallet/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})

## Standards and Source References
- [OpenID for Verifiable Credential Issuance 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2025-09-16) — normative

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
- issuance_log
- verification_log
- policy_document
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- verification_log
- policy_document
- audit_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **OPENID**: OpenID4VCI 1.0
