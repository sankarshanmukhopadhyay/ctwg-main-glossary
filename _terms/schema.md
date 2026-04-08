---
title: "schema"
---

# schema

## Definition
A framework, pattern, or set of rules for enforcing a specific structure on a digital object or a set of digital data. There are many types of schemas, e.g., data schema, credential verification schema, database schema.

## Aliases
schema, schemas

## Governance Profile
- **Authority scope**: credential_issuance, policy_definition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- issuance_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document
- issuance_log

## Notes
- `credentialSchema` is a Property Definition in the W3C VC Data Model. See section 3.2.1.

## Supporting Definitions
- For more information, see: W3C [Data Schemas](https://www.w3.org/TR/vc-data-model/#data-schemas).

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
