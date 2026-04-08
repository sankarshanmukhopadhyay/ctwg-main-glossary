---
title: "verifiable"
---

# verifiable

## Definition
In the context of digital communications infrastructure, the ability to determine the authenticity of a communication (e.g., sender, contents, claims, metadata, provenance), or the underlying sociotechnical infrastructure (e.g., governance, roles, policies, authorizations, certifications).

## Aliases
verifiable, verifiability

## Governance Profile
- **Authority scope**: credential_issuance, access_decisioning, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- issuance_log
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- access_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- issuance_log
- access_decision_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- appraisable
- digital signature.

## Crosswalk References
Not specified
