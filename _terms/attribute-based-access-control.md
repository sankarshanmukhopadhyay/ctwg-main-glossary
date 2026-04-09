---
title: "attribute-based-access-control"
---

> Generated file. Update `glossary/terms/attribute-based-access-control.yaml` and regenerate artifacts instead of editing this page directly.

# attribute-based-access-control

## Definition
An access control approach in which access is mediated based on attributes associated with subjects (requesters) and the objects to be accessed. Each object and subject has a set of associated attributes, such as location, time of creation, access rights, etc. Access to an object is authorized or denied depending upon whether the required (e.g., policy-defined) correlation can be made between the attributes of that object and of the requesting subject.

## Aliases
attribute-based access control, attribute-based access controls

## Governance Profile
- **Authority scope**: policy_definition, access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- access_decision

## Assurance
**Evidence artifacts**
- policy_document
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document
- access_decision_log

## Notes
Not specified

## Supporting Definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Attribute-based_access_control): Attribute-based access control (ABAC), also known as policy-based access control for [IAM](https://en.wikipedia.org/wiki/Identity_management), defines an access control paradigm whereby a subject's authorization to perform a set of operations is determined by evaluating attributes associated with the subject, object, requested operations, and, in some cases, environment attributes.

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
