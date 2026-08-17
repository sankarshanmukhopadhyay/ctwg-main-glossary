---
title: "access-control"
---

# access-control

The process of granting or denying specific requests for obtaining and using information and related information processing services.

## Formal definition
The process of granting or denying specific requests for obtaining and using information and related information processing services.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **access control** (`en`, `alternative`)
- **access controls** (`en`, `alternative`)

### Related concepts
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})
- [role-based-access-control]({{ '/terms/role-based-access-control/' | relative_url }})
- [attribute-based-access-control]({{ '/terms/attribute-based-access-control/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:permission`
- **related**: `urn:tig:concept:role-based-access-control`
- **related**: `urn:tig:concept:attribute-based-access-control`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:access-control`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/access_control).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
access control, access controls

### Governance profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- access_decision

### Assurance
**Evidence artifacts**
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log

### Notes
Not specified

### Supporting definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Access_control): In [physical security](https://en.wikipedia.org/wiki/Physical_security) and [information security](https://en.wikipedia.org/wiki/Information_security), access control (AC) is the selective restriction of access to a place or other resource, while access management describes the process. The act of accessing may mean consuming, entering, or using. Permission to access a resource is called [[ref: authorization]].

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/access-control.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
