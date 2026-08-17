---
title: "registration"
---

> Generated file. Update `glossary/terms/registration.yaml` and regenerate artifacts instead of editing this page directly.

# registration

## In Simple English
The process by which a registrant submits a record to a registry.

## Definition
The process by which a registrant submits a record to a registry.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
registration, registrations

## See Also
- [registry]({{ '/terms/registry/' | relative_url }})
- [trust-registry]({{ '/terms/trust-registry/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/registration.md`

## Governance Profile
- **Authority scope**: registry_management
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- registration_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- registration_decision
- revocation_decision

- **Accountable entity**: registry_operator

**Evidence produced**
- registry_entry

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
