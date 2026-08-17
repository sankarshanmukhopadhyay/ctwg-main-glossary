---
title: "trusted-timestamp-authority"
---

# trusted-timestamp-authority

An authority that is trusted to provide accurate time information in the form of a timestamp.

## Formal definition
An authority that is trusted to provide accurate time information in the form of a timestamp.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **trusted timestamp authority** (`en`, `alternative`)
- **trusted timestamp authorities** (`en`, `alternative`)
- **TTA** (`en`, `alternative`)
- **TTAs** (`en`, `alternative`)

### Related concepts
- [governance]({{ '/terms/governance/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [governing-authority]({{ '/terms/governing-authority/' | relative_url }})
- [trust-registry]({{ '/terms/trust-registry/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:governance`
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:governing-authority`
- **related**: `urn:tig:concept:trust-registry`
- **related**: `urn:tig:concept:revocation`
- **related**: `urn:tig:concept:verification`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:trusted-timestamp-authority`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/trusted_timestamp_authority).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
trusted timestamp authority, trusted timestamp authorities, TTA, TTAs

### Governance profile
- **Authority scope**: governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- revocation_decision

### Assurance
**Evidence artifacts**
- definition_change_record
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- definition_change_record
- status_record
- audit_log
- verification_log
- registry_entry

### Notes
Not specified

### Supporting definitions
- Also known as: [[ref: TTA]].

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/trusted-timestamp-authority.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
