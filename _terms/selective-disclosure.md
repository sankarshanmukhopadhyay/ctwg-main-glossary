---
title: "selective-disclosure"
---

> Generated file. Update `glossary/terms/selective-disclosure.yaml` and regenerate artifacts instead of editing this page directly.

# selective-disclosure

## In Simple English
A privacy-preserving presentation capability that allows a holder to disclose only selected claims or attributes from a credential while preserving verifiability.

## Definition
A privacy-preserving presentation capability that allows a holder to disclose only selected claims or attributes from a credential while preserving verifiability.

## Reader Note
This bridge term improves navigation across privacy, status, provenance, and assurance concepts.

## Implementation Relevance
Use this term where evidence needs to be carried across both reader-facing documentation and machine-verifiable assurance artifacts.

## Aliases
selective disclosure

## See Also
- [sd-jwt-vc]({{ '/terms/sd-jwt-vc/' | relative_url }})
- [verifiable-presentation]({{ '/terms/verifiable-presentation/' | relative_url }})
- [zero-knowledge-proof]({{ '/terms/zero-knowledge-proof/' | relative_url }})
- [correlation-privacy]({{ '/terms/correlation-privacy/' | relative_url }})

## Standards and Source References
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative

## Governance Profile
- **Authority scope**: assurance_and_audit, verification_and_reliance
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
- **W3C**: VC Data Model v2.0
- **IETF**: RFC 9901
