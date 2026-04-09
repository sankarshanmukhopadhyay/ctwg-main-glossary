---
title: "assurance-level"
---

> Generated file. Update `glossary/terms/assurance-level.yaml` and regenerate artifacts instead of editing this page directly.

# assurance-level

## Definition
A level of confidence in a claim that may be relied on by others. Different types of assurance levels are defined for different types of trust assurance mechanisms. Examples include authenticator assurance level, federation assurance level, and identity assurance level.

## Aliases
assurance level, assurance levels

## Governance Profile
- **Authority scope**: credential_issuance, access_decisioning, assurance_and_audit
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
- attestation

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- attestation

## Notes
- Assurance levels are most useful when the criteria for each level are explicit, testable, and supported by inspectable evidence.

## Supporting Definitions
- For verifiable credentials, an assurance level measures the degree of certainty in an identity's authenticity or a credential's validity. It is influenced by the strength of the identity assurance process, the robustness of the authentication process, the management of the credential issuer, and the evidence available to support those assessments.

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
- **NIST**: IA-8
- **ISO**: ISO/IEC 29115
