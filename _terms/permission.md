---
title: "permission"
---

> Generated file. Update `glossary/terms/permission.yaml` and regenerate artifacts instead of editing this page directly.

# permission

## Concept Identity
- **Concept ID**: `urn:tig:concept:permission`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
Authorization to perform some action on a system.

## Definition
Authorization to perform some action on a system.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **permissions** (`en`, `alternative`)

## Legacy Aliases
permission, permissions

## Semantic Relations
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:role-based-access-control`
- **related**: `urn:tig:concept:attribute-based-access-control`
- **related**: `urn:tig:concept:access-control`
- **related**: `urn:tig:concept:revocation`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [role-based-access-control]({{ '/terms/role-based-access-control/' | relative_url }})
- [attribute-based-access-control]({{ '/terms/attribute-based-access-control/' | relative_url }})
- [access-control]({{ '/terms/access-control/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/permission).

## Governance Profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
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

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
