---
title: "control-authority"
---

# control-authority

A simple-English summary has not yet been added for this concept.

## Formal definition
In identity systems, control authority is the power to determine who controls what. It is a primary factor in determining the basis for trust in those systems.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **control authority** (`en`, `alternative`)

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
- **Concept ID**: `urn:tig:concept:control-authority`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/control-authority.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
control-authority, control authority

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
- Control authority is especially important because it identifies where effective operational power resides, including the power to change, invalidate, or reassign control relationships.

### Supporting definitions
- The entity with *control authority* takes action through operations that affect the:
- - creation (inception)
- - updating
- - rotation
- - revocation
- - deletion
- - delegation
- of authentication factors and their relation to the identifier.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/control-authority.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
