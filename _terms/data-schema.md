---
title: "data-schema"
---

> Generated file. Update `glossary/terms/data-schema.yaml` and regenerate artifacts instead of editing this page directly.

# data-schema

## Definition
A description of the structure of a digital document or object, typically expressed in a machine-readable language in terms of constraints on the structure and content of documents or objects of that type. A credential schema is a particular type of data schema.

## Aliases
data schema, data schemas

## Governance Profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: design
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

## Notes
Not specified

## Supporting Definitions
- [Wikipedia](https://en.wikipedia.org/wiki/XML_schema): An XML schema is a description of a type of [XML](https://en.wikipedia.org/wiki/Extensible_Markup_Language) document, typically expressed in terms of constraints on the structure and content of documents of that type, above and beyond the basic syntactical constraints imposed by XML itself. These constraints are generally expressed using some combination of grammatical rules governing the order of elements, [Boolean predicates](https://en.wikipedia.org/wiki/Boolean_predicates) that the content must satisfy, data types governing the content of elements and attributes, and more specialized rules such as [uniqueness](https://en.wikipedia.org/wiki/Uniqueness_quantification) and [referential integrity](https://en.wikipedia.org/wiki/Referential_integrity) constraints.

## Mental Models
Not specified

## See Also
- credential
- issuer
- issuance
- verifiable-credential

## Crosswalk References
Not specified
