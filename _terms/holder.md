---
title: "holder"
---

# holder

## Definition
A role an agent performs by serving as the controller of the cryptographic keys and digital credentials in a digital wallet. The holder makes issuance requests for credentials and responds to presentation requests for credentials. A holder is usually, but not always, a subject of the credentials they are holding.

## Aliases
holder, holders

## Governance Profile
- **Authority scope**: credential_issuance, delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- issuance_decision
- revocation_decision

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
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- issuance_log

## Notes
Not specified

## Supporting Definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/terms/holder): a component that implements the [capability](https://essif-lab.github.io/framework/docs/terms/capability) to handle [presentation requests](https://essif-lab.github.io/framework/docs/terms/presentation-request) from a [peer agent](https://essif-lab.github.io/framework/docs/terms/peer-agent), produce the requested data (a presentation) according to its [principal](https://essif-lab.github.io/framework/docs/terms/principal)'s [holder-policy](https://essif-lab.github.io/framework/docs/terms/holder-policy), and send that in response to the request.
- [W3C VC](https://www.w3.org/TR/vc-data-model/#dfn-holders): A role an [entity](https://www.w3.org/TR/vc-data-model/#dfn-entities) might perform by possessing one or more [verifiable credentials](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-credentials) and generating [presentations](https://www.w3.org/TR/vc-data-model/#dfn-presentations) from them. A holder is usually, but not always, a [subject](https://www.w3.org/TR/vc-data-model/#dfn-subjects) of the [verifiable credentials](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-credentials) they are holding. Holders store their [credentials](https://www.w3.org/TR/vc-data-model/#dfn-credential) in [credential repositories](https://www.w3.org/TR/vc-data-model/#dfn-credential-repository).

## Mental Models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

## See Also
- issuer
- verifier.

## Crosswalk References
Not specified
