---
title: "issuer-metadata"
---

> Generated file. Update `glossary/terms/issuer-metadata.yaml` and regenerate artifacts instead of editing this page directly.

# issuer-metadata

## In Simple English
Metadata published by a credential issuer describing issuer capabilities, credential configurations, endpoints, and supported formats.

## Definition
Metadata published by a credential issuer describing issuer capabilities, credential configurations, endpoints, and supported formats.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
credential issuer metadata, issuer metadata

## See Also
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [openid4vci]({{ '/terms/openid4vci/' | relative_url }})
- [credential-schema]({{ '/terms/credential-schema/' | relative_url }})
- [digital-wallet]({{ '/terms/digital-wallet/' | relative_url }})

## Standards and Source References
- [OpenID for Verifiable Credential Issuance 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2025-09-16) — normative

## Governance Profile
- **Authority scope**: credential_issuance, registry_management
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- registration_decision

## Assurance
**Evidence artifacts**
- registry_entry
- policy_document
- issuance_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- registration_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- registry_entry
- policy_document
- issuance_log
- audit_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **OPENID**: OpenID4VCI 1.0
