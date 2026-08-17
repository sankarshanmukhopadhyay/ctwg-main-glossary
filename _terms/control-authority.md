---
title: "control-authority"
---

> Generated file. Update `glossary/terms/control-authority.yaml` and regenerate artifacts instead of editing this page directly.

# control-authority

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
In identity systems, control authority is the power to determine who controls what. It is a primary factor in determining the basis for trust in those systems.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
control-authority, control authority

## See Also
- [governance]({{ '/terms/governance/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [governing-authority]({{ '/terms/governing-authority/' | relative_url }})
- [trust-registry]({{ '/terms/trust-registry/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/control-authority.md`

## Governance Profile
- **Authority scope**: governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- revocation_decision

## Assurance
**Evidence artifacts**
- definition_change_record
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- definition_change_record
- status_record
- audit_log
- verification_log
- registry_entry

## Notes
- Control authority is especially important because it identifies where effective operational power resides, including the power to change, invalidate, or reassign control relationships.

## Supporting Definitions
- The entity with *control authority* takes action through operations that affect the:
- - creation (inception)
- - updating
- - rotation
- - revocation
- - deletion
- - delegation
- of authentication factors and their relation to the identifier.

## Mental Models
Not specified

## Crosswalk References
Not specified
