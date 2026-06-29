---
title: "trust-registry"
---

> Generated file. Update `glossary/terms/trust-registry.yaml` and regenerate artifacts instead of editing this page directly.

# trust-registry

## Definition
A registry that serves as an authoritative source for trust graphs or other governed information describing one or more trust communities. A trust registry is typically authorized by a governance framework.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
trust registry, trust registries

## See Also
- [trust list]({{ '/terms/trust-list/' | relative_url }})
- [verifiable data registry]({{ '/terms/verifiable-data-registry/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/trust-registry.md`

## Governance Profile
- **Authority scope**: policy_definition, registry_management, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- registration_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- registry_entry
- status_record

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- registration_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- registry_entry
- status_record

## Notes
- In operational terms, a trust registry often functions as a governance decision-plane component because its published information may be used to determine recognition, admission, status, or reliance.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **NIST**: CA-3
- **ISO**: ISO/IEC 27001 A.5.19
