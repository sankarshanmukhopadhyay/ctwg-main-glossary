---
title: "authenticator-assurance-level"
---

> Generated file. Update `glossary/terms/authenticator-assurance-level.yaml` and regenerate artifacts instead of editing this page directly.

# authenticator-assurance-level

## Definition
A measure of the strength of an authentication mechanism and, therefore, the confidence in it.

## Aliases
authenticator assurance level, authenticator assurance levels, AAL, AALs

## Governance Profile
- **Authority scope**: access_decisioning, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- access_decision

## Assurance
**Evidence artifacts**
- attestation
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- attestation
- access_decision_log

## Notes
- In NIST SP 800-63-3, AAL is defined in terms of three levels: AAL1 (Some confidence), AAL2 (High confidence), AAL3 (Very high confidence).

## Supporting Definitions
- Also known as: [[ref: AAL]]

## Mental Models
Not specified

## See Also
- federation assurance level
- identity assurance level
- identity binding.

## Crosswalk References
Not specified
