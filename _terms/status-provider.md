---
title: "status-provider"
---

# status-provider

An entity that provides status information such as suspension or revocation for a credential.

## Formal definition
An entity that provides status information such as suspension or revocation for a credential.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **credential status provider** (`en`, `alternative`)
- **status provider** (`en`, `alternative`)

### Related concepts
- [bitstring-status-list]({{ '/terms/bitstring-status-list/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})
- [status-record]({{ '/terms/status-record/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:bitstring-status-list`
- **related**: `urn:tig:concept:revocation`
- **related**: `urn:tig:concept:status-record`
- **related**: `urn:tig:concept:verifiable-credential`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:status-provider`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative
- [Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/) (W3C; Recommendation; 1.0; 2025-05-15) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
credential status provider, status provider

### Governance profile
- **Authority scope**: registry_management, verification_and_reliance
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
- registry_entry
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
- registry_entry
- verification_log
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **IETF**: RFC 9901
- **W3C**: Bitstring Status List v1.0

</details>

---

*Generated from `glossary/terms/status-provider.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
