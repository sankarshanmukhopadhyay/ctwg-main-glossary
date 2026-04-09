---
title: "autonomic-namespace"
---

> Generated file. Update `glossary/terms/autonomic-namespace.yaml` and regenerate artifacts instead of editing this page directly.

# autonomic-namespace

## Definition
a namespace that is self-certifying and hence self-administrating. An AN has a self-certifying prefix that provides cryptographic verification of root control authority over its namespace. All derived AIDs in the same AN share the same root-of-trust, source-of-truth, and locus-of-control (RSL). The governance of the namespace is, therefore, unified into one entity, that is, the controller who is/holds the root authority over the namespace.

## Aliases
autonomic-namespace, autonomic namespace

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

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- definition_change_record

## Notes
Not specified

## Supporting Definitions
- Namespaces are, therefore, portable and truly self-sovereign.

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
