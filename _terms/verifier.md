---
title: "verifier"
---

# verifier

## Definition
A role an agent performs to verify one or more proofs of the claims in a digital credential or other verifiable data, and to evaluate whether the presented material satisfies applicable verification and policy criteria.

## Aliases
verifier, verifiers

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance, policy_definition, delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- delegation_grant
- reliance_decision
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- delegation_record
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- delegation_grant
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: verifier_operator

**Evidence produced**
- policy_document
- delegation_record
- issuance_log
- verification_log

## Notes
- A verifier may function as an execution-time decision point because verification outcomes can determine whether access, acceptance, recognition, or reliance is granted.

## Supporting Definitions
- [W3C VC](https://www.w3.org/TR/vc-data-model/#terminology): A role an [entity](https://www.w3.org/TR/vc-data-model/#dfn-entities) performs by receiving one or more [verifiable credentials](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-credentials), optionally inside a [verifiable presentation](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-presentations) for processing. Other specifications might refer to this concept as a [[ref: relying party]].
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#verifier): a component that implements the [capability](https://essif-lab.github.io/framework/docs/terms/capability) to request [peer agents](https://essif-lab.github.io/framework/docs/terms/peer-agent) to present (provide) data from credentials (of a specified kind, issued by specified [parties](https://essif-lab.github.io/framework/docs/terms/party)), and to verify such responses (check structure, signatures, dates), according to its [principal](https://essif-lab.github.io/framework/docs/terms/principal)'s [verifier policy](https://essif-lab.github.io/framework/docs/terms/verifier-policy).
- [NIST](https://csrc.nist.gov/glossary/term/verifier) The entity that verifies the authenticity of a digital signature using the public key.

## Mental Models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

## See Also
- relying party; issuer
- holder.

## Crosswalk References
- **NIST**: AU-10
- **ISO**: ISO/IEC 27001 A.8.15
