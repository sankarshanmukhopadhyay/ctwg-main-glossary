---
title: "status-record"
---

> Generated file. Update `glossary/terms/status-record.yaml` and regenerate artifacts instead of editing this page directly.

# status-record

## Concept Identity
- **Concept ID**: `urn:tig:concept:status-record`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
An inspectable record that represents the validity, suspension, revocation, or lifecycle status of a credential, authorization, registration, or governed object.

## Definition
An inspectable record that represents the validity, suspension, revocation, or lifecycle status of a credential, authorization, registration, or governed object.

## Reader Note
This bridge term improves navigation across privacy, status, provenance, and assurance concepts.

## Implementation Relevance
Use this term where evidence needs to be carried across both reader-facing documentation and machine-verifiable assurance artifacts.

## Alternative Designations
- **status record** (`en`, `alternative`)

## Legacy Aliases
status record

## Semantic Relations
- **related**: `urn:tig:concept:revocation`
- **related**: `urn:tig:concept:bitstring-status-list`
- **related**: `urn:tig:concept:audit-log`
- **related**: `urn:tig:concept:verification`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [revocation]({{ '/terms/revocation/' | relative_url }})
- [bitstring-status-list]({{ '/terms/bitstring-status-list/' | relative_url }})
- [audit-log]({{ '/terms/audit-log/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})

## Standards and Source References
- [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (W3C; Recommendation; 2.0; 2025-05-15) — normative

## Governance Profile
- **Authority scope**: assurance_and_audit, verification_and_reliance
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

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **W3C**: VC Data Model v2.0
