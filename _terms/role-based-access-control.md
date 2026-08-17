---
title: "role-based-access-control"
---

# role-based-access-control

A simple-English summary has not yet been added for this concept.

## Formal definition
Access control based on user roles (i.e., a collection of access authorizations a user receives based on an explicit or implicit assumption of a given role). Role permissions may be inherited through a role hierarchy and typically reflect the permissions needed to perform defined functions within an organization. A given role may apply to a single individual or to several individuals.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **role-based access control** (`en`, `alternative`)
- **role-based access controls** (`en`, `alternative`)

### Related concepts
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})
- [attribute-based-access-control]({{ '/terms/attribute-based-access-control/' | relative_url }})
- [access-control]({{ '/terms/access-control/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:permission`
- **related**: `urn:tig:concept:attribute-based-access-control`
- **related**: `urn:tig:concept:access-control`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:role-based-access-control`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/role_based_access_control).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
role-based access control, role-based access controls

### Governance profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- access_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

### Notes
Not specified

### Supporting definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Role-based_access_control): In computer systems security, role-based access control (RBAC) or role-based security is an approach to restricting system access to authorized users, and to implementing [mandatory access control](https://en.wikipedia.org/wiki/Mandatory_access_control) (MAC) or [discretionary access control](https://en.wikipedia.org/wiki/Discretionary_access_control) (DAC).

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/role-based-access-control.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
