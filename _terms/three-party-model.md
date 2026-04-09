---
title: "three-party-model"
---

> Generated file. Update `glossary/terms/three-party-model.yaml` and regenerate artifacts instead of editing this page directly.

# three-party-model

## Definition
The issuer—holder—verifier model used by all types of physical credentials and digital credentials to enable transitive trust decisions.

## Aliases
three party model

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: issuer_operator

**Evidence produced**
- issuance_log
- verification_log

## Notes
Not specified

## Supporting Definitions
- Also known as: [[ref: trust triangle]].

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
