---
title: "access-control"
---

> Generated file. Update `glossary/terms/access-control.yaml` and regenerate artifacts instead of editing this page directly.

# access-control

## Concept Identity
- **Concept ID**: `urn:tig:concept:access-control`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
The process of granting or denying specific requests for obtaining and using information and related information processing services.

## Definition
The process of granting or denying specific requests for obtaining and using information and related information processing services.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **access control** (`en`, `alternative`)
- **access controls** (`en`, `alternative`)

## Legacy Aliases
access control, access controls

## Semantic Relations
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:permission`
- **related**: `urn:tig:concept:role-based-access-control`
- **related**: `urn:tig:concept:attribute-based-access-control`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})
- [role-based-access-control]({{ '/terms/role-based-access-control/' | relative_url }})
- [attribute-based-access-control]({{ '/terms/attribute-based-access-control/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/access_control).

## Governance Profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- access_decision

## Assurance
**Evidence artifacts**
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log

## Notes
Not specified

## Supporting Definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Access_control): In [physical security](https://en.wikipedia.org/wiki/Physical_security) and [information security](https://en.wikipedia.org/wiki/Information_security), access control (AC) is the selective restriction of access to a place or other resource, while access management describes the process. The act of accessing may mean consuming, entering, or using. Permission to access a resource is called [[ref: authorization]].

## Mental Models
Not specified

## Crosswalk References
Not specified
