---
title: "verification"
---

> Generated file. Update `glossary/terms/verification.yaml` and regenerate artifacts instead of editing this page directly.

# verification

## Definition
An action an agent (of a principal) performs to determine the authenticity of a claim or other data object. Cryptographic verification uses cryptographic keys.

## Aliases
verification, verify, verifies, verified, verifying

## Governance Profile
- **Authority scope**: credential_issuance, delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- issuance_decision

## Assurance
**Evidence artifacts**
- delegation_record
- issuance_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- issuance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- issuance_log

## Notes
Not specified

## Supporting Definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#verify): The act, by or on behalf of a [party](https://essif-lab.github.io/framework/docs/terms/party), of determining whether that data is authentic (i.e. originates from the [party](https://essif-lab.github.io/framework/docs/terms/party) that authored it), timely (i.e. has not expired), and conforms to other specifications that apply to its structure.

## Mental Models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

## See Also
- validation.
- KERI scope definition of [[xref: keri1
- verification]]

## Crosswalk References
Not specified
