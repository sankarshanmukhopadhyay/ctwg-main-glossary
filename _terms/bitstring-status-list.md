---
title: "bitstring-status-list"
---

# bitstring-status-list

A W3C status mechanism for publishing credential status information such as revocation or suspension using compressed bitstrings.

## Formal definition
A W3C status mechanism for publishing credential status information such as revocation or suspension using compressed bitstrings.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this term when modelling inspectable credential status evidence without exposing unnecessary holder-specific information.

## Names and relationships

### Alternative designations
- **Bitstring Status List** (`en`, `alternative`)
- **BSL** (`en`, `alternative`)

### Related concepts
- [credential]({{ '/terms/credential/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})
- [status-record]({{ '/terms/status-record/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:credential`
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:revocation`
- **related**: `urn:tig:concept:status-record`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:bitstring-status-list`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/) (W3C; Recommendation; 1.0; 2025-05-15) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
Bitstring Status List, BSL

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance
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
- registry_entry

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
- registry_entry

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **W3C**: Bitstring Status List v1.0

</details>

---

*Generated from `glossary/terms/bitstring-status-list.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
