---
title: "issuer"
---

> Generated file. Update `glossary/terms/issuer.yaml` and regenerate artifacts instead of editing this page directly.

# issuer

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A role an agent performs to assert a set of claims, package and digitally sign them, typically in the form of a digital credential, and transmit them to a holder under applicable policy and governance constraints.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
issuer, issuers

## See Also
- [verifier]({{ '/terms/verifier/' | relative_url }})
- [holder]({{ '/terms/holder/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/issuer.md`

## Governance Profile
- **Authority scope**: credential_issuance, policy_definition, delegation_and_scope, governance_recognition
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- delegation_grant
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- delegation_record
- status_record
- issuance_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- delegation_grant
- issuance_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- delegation_record
- status_record
- issuance_log

## Notes
- An issuer commonly bears responsibility for issuance criteria, status maintenance, and revocation handling relevant to the credentials it issues.

## Supporting Definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#issuer): a component that implements the [capability](https://essif-lab.github.io/framework/docs/terms/capability) to construct [credentials](https://essif-lab.github.io/framework/docs/terms/credential) from data objects, according to the content of its [principal](https://essif-lab.github.io/framework/docs/terms/principal)'s [issuer](https://essif-lab.github.io/framework/docs/terms/issuer)-Policy (specifically regarding the way in which the [credential](https://essif-lab.github.io/framework/docs/terms/credential) is to be digitally signed), and pass it to the [wallet](https://essif-lab.github.io/framework/docs/terms/wallet)-component of its [principal](https://essif-lab.github.io/framework/docs/terms/principal) allowing it to be issued.
- [W3C VC](https://www.w3.org/TR/vc-data-model/#terminology): A role an [entity](https://www.w3.org/TR/vc-data-model/#dfn-entities) can perform by asserting [claims](https://www.w3.org/TR/vc-data-model/#dfn-claims) about one or more [subjects](https://www.w3.org/TR/vc-data-model/#dfn-subjects), creating a [verifiable credential](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-credentials) from these [claims](https://www.w3.org/TR/vc-data-model/#dfn-claims), and transmitting the [verifiable credential](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-credentials) to a [holder](https://www.w3.org/TR/vc-data-model/#dfn-holders).

## Mental Models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

## Crosswalk References
- **NIST**: IA-5
- **ISO**: ISO/IEC 27001 A.5.16
