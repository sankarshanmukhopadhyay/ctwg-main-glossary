---
title: "status-record"
---

# status-record

An inspectable record that represents the validity, suspension, revocation, or lifecycle status of a credential, authorization, registration, or governed object.

## Formal definition
An inspectable record that represents the validity, suspension, revocation, or lifecycle status of a credential, authorization, registration, or governed object.

## Why this concept matters
This bridge term improves navigation across privacy, status, provenance, and assurance concepts.

Use this term where evidence needs to be carried across both reader-facing documentation and machine-verifiable assurance artifacts.

## Names and relationships

### Alternative designations
- **status record** (`en`, `alternative`)

### Related concepts
- [revocation]({{ '/terms/revocation/' | relative_url }})
- [bitstring-status-list]({{ '/terms/bitstring-status-list/' | relative_url }})
- [audit-log]({{ '/terms/audit-log/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:revocation`
- **related**: `urn:tig:concept:bitstring-status-list`
- **related**: `urn:tig:concept:audit-log`
- **related**: `urn:tig:concept:verification`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:status-record`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (W3C; Recommendation; 2.0; 2025-05-15) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
status record

### Governance profile
- **Authority scope**: assurance_and_audit, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- revocation_decision
- reliance_decision

### Assurance
**Evidence artifacts**
- status_record
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- revocation_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- status_record
- verification_log
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **W3C**: VC Data Model v2.0

</details>

---

*Generated from `glossary/terms/status-record.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
