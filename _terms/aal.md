---
title: "aal"
---

# aal

See: authenticator assurance level.

## Formal definition
See: authenticator assurance level.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **AAL** (`en`, `alternative`)

### Related concepts
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})
- [role-based-access-control]({{ '/terms/role-based-access-control/' | relative_url }})
- [attribute-based-access-control]({{ '/terms/attribute-based-access-control/' | relative_url }})
- [audit]({{ '/terms/audit/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:permission`
- **related**: `urn:tig:concept:role-based-access-control`
- **related**: `urn:tig:concept:attribute-based-access-control`
- **related**: `urn:tig:concept:audit`
- **related**: `urn:tig:concept:verification`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:aal`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST SP 800-63-4 Digital Identity Guidelines](https://doi.org/10.6028/NIST.SP.800-63-4) (NIST; Final; 800-63-4; 2025-08-01) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
AAL

### Governance profile
- **Authority scope**: access_decisioning, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: decision_plane_component

### Enforcement points
- access_decision

### Assurance
**Evidence artifacts**
- attestation

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- attestation

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **NIST**: SP 800-63-4

</details>

---

*Generated from `glossary/terms/aal.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
