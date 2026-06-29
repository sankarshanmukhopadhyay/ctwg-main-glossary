---
title: "sd-jwt-vc"
---

> Generated file. Update `glossary/terms/sd-jwt-vc.yaml` and regenerate artifacts instead of editing this page directly.

# sd-jwt-vc

## Definition
A verifiable credential encoded using Selective Disclosure JWT mechanisms, enabling selected claims to be disclosed while preserving cryptographic verification.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
SD-JWT VC, SD-JWT-based Verifiable Credential

## See Also
- [selective-disclosure]({{ '/terms/selective-disclosure/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [secured-verifiable-credential]({{ '/terms/secured-verifiable-credential/' | relative_url }})
- [key-binding-jwt]({{ '/terms/key-binding-jwt/' | relative_url }})

## Standards and Source References
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative

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
- audit_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **IETF**: RFC 9901
- **OPENID**: OpenID4VCI, OpenID4VP
