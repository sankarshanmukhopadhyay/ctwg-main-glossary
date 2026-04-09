---
title: "presentation"
---

> Generated file. Update `glossary/terms/presentation.yaml` and regenerate artifacts instead of editing this page directly.

# presentation

## Definition
A verifiable message that a holder may send to a verifier containing proofs of one or more claims derived from one or more digital credentials from one or more issuers as a response to a specific presentation request from a  verifier.

## Aliases
presentation, presentations, present, presents, presenting, presented

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: issuer_operator

**Evidence produced**
- issuance_log
- verification_log

## Notes
Not specified

## Supporting Definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/terms/presentation): A (signed) digital [[ref: message]] that a [[ref: holder]] component may send to a [[ref: verifier]] component that contains [[ref: data]] derived from one or more [[ref: verifiable credentials]] (that (a [colleague](https://essif-lab.github.io/framework/docs/terms/colleague) component of) the [holder](https://essif-lab.github.io/framework/docs/terms/holder) component has received from [issuer](https://essif-lab.github.io/framework/docs/terms/issuer) components of one or more [parties](https://essif-lab.github.io/framework/docs/terms/party)), as a response to a specific [[ref: presentation request]] of a  [[ref: verifier ]]component.

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
