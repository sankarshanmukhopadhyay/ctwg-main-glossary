---
title: "status-provider"
---

> Generated file. Update `glossary/terms/status-provider.yaml` and regenerate artifacts instead of editing this page directly.

# status-provider

## Definition
An entity that provides status information such as suspension or revocation for a credential.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
credential status provider, status provider

## See Also
- [bitstring-status-list]({{ '/terms/bitstring-status-list/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})
- [status-record]({{ '/terms/status-record/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})

## Standards and Source References
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative
- [Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/) (W3C; Recommendation; 1.0; 2025-05-15) — normative

## Governance Profile
- **Authority scope**: registry_management, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- revocation_decision
- reliance_decision

## Assurance
**Evidence artifacts**
- status_record
- registry_entry
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- revocation_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- status_record
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
- **IETF**: RFC 9901
- **W3C**: Bitstring Status List v1.0
