---
title: "attribute-based-access-control"
---

# attribute-based-access-control

A simple-English summary has not yet been added for this concept.

## Formal definition
An access control approach in which access is mediated based on attributes associated with subjects (requesters) and the objects to be accessed. Each object and subject has a set of associated attributes, such as location, time of creation, access rights, etc. Access to an object is authorized or denied depending upon whether the required (e.g., policy-defined) correlation can be made between the attributes of that object and of the requesting subject.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **attribute-based access control** (`en`, `alternative`)
- **attribute-based access controls** (`en`, `alternative`)

### Related concepts
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [requirement]({{ '/terms/requirement/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})
- [role-based-access-control]({{ '/terms/role-based-access-control/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:policy`
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:requirement`
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:permission`
- **related**: `urn:tig:concept:role-based-access-control`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:attribute-based-access-control`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/attribute_based_access_control).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
attribute-based access control, attribute-based access controls

### Governance profile
- **Authority scope**: policy_definition, access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- access_decision

### Assurance
**Evidence artifacts**
- policy_document
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- policy_approval
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document
- access_decision_log

### Notes
Not specified

### Supporting definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Attribute-based_access_control): Attribute-based access control (ABAC), also known as policy-based access control for [IAM](https://en.wikipedia.org/wiki/Identity_management), defines an access control paradigm whereby a subject's authorization to perform a set of operations is determined by evaluating attributes associated with the subject, object, requested operations, and, in some cases, environment attributes.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/attribute-based-access-control.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
