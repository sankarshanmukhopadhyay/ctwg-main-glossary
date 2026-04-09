---
title: "authorization"
---

> Generated file. Update `glossary/terms/authorization.yaml` and regenerate artifacts instead of editing this page directly.

# authorization

## Definition
The process of determining whether a requested action or service is approved for a specific entity under applicable policies, rules, credentials, or other governing criteria.

## Aliases
authorization, authorizations, authorize, authorized, unauthorized, authorizing, unauthorizing, authorisation, authorisations, authorise, authorised, unauthorised, authorising, unauthorising

## Governance Profile
- **Authority scope**: credential_issuance, policy_definition, access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- issuance_decision
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- issuance_log
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- issuance_decision
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document
- issuance_log
- access_decision_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- permission.

## Crosswalk References
- **NIST**: AC-2, AC-3
- **ISO**: ISO/IEC 27001 A.5.15, ISO/IEC 42001 8.2
