---
title: "key-binding-jwt"
---

> Generated file. Update `glossary/terms/key-binding-jwt.yaml` and regenerate artifacts instead of editing this page directly.

# key-binding-jwt

## Definition
A JWT used to demonstrate holder control of a key associated with an SD-JWT or SD-JWT VC presentation.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
KB-JWT, Key Binding JWT

## See Also
- [holder-binding]({{ '/terms/holder-binding/' | relative_url }})
- [sd-jwt-vc]({{ '/terms/sd-jwt-vc/' | relative_url }})
- [proof-of-possession]({{ '/terms/proof-of-possession/' | relative_url }})
- [cryptographic-key]({{ '/terms/cryptographic-key/' | relative_url }})

## Standards and Source References
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative

## Governance Profile
- **Authority scope**: verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision

## Assurance
**Evidence artifacts**
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
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
