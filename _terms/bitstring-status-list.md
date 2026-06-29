---
title: "bitstring-status-list"
---

> Generated file. Update `glossary/terms/bitstring-status-list.yaml` and regenerate artifacts instead of editing this page directly.

# bitstring-status-list

## Definition
A W3C status mechanism for publishing credential status information such as revocation or suspension using compressed bitstrings.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term when modelling inspectable credential status evidence without exposing unnecessary holder-specific information.

## Aliases
Bitstring Status List, BSL

## See Also
- [credential]({{ '/terms/credential/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})
- [status-record]({{ '/terms/status-record/' | relative_url }})

## Standards and Source References
- [Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/) (W3C; Recommendation; 1.0; 2025-05-15) — normative

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance
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
- verification_log
- audit_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- revocation_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- status_record
- verification_log
- audit_log
- registry_entry

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **W3C**: Bitstring Status List v1.0
