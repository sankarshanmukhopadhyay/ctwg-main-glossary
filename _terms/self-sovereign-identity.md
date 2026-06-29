---
title: "self-sovereign-identity"
---

> Generated file. Update `glossary/terms/self-sovereign-identity.yaml` and regenerate artifacts instead of editing this page directly.

# self-sovereign-identity

## Definition
Self-sovereign identity is a decentralized identity architecture that implements the Principles of SSI — principally that it puts the identity controller (e.g., a natural person or organization) directly in control of the identifiers and credentials they use to assert their digital identity.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
self-sovereign identity, SSI

## See Also
- [federated identity]({{ '/terms/federated-identity/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/self-sovereign-identity.md`

## Governance Profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
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
- Also known as: [[ref: SSI]].
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#ssi-self-sovereign-identity): SSI (Self-Sovereign Identity) is a term that has many different interpretations, and that we use to refer to concepts/ideas, architectures, processes and technologies that aim to support (autonomous) [parties](https://essif-lab.github.io/framework/docs/terms/party) as they negotiate and execute electronic [transactions](https://essif-lab.github.io/framework/docs/terms/transaction) with one another.
- [Wikipedia](https://en.wikipedia.org/wiki/Self-sovereign_identity): Self-sovereign identity (SSI) is an approach to [digital identity](https://en.wikipedia.org/wiki/Digital_identity) that gives individuals control over the information they use to prove who they are to [websites](https://en.wikipedia.org/wiki/Website), services, and [applications](https://en.wikipedia.org/wiki/Application_software) across the web. Without SSI, individuals with persistent accounts (identities) across the [internet](https://en.wikipedia.org/wiki/Internet) must rely on a number of large identity providers, such as [Facebook](https://en.wikipedia.org/wiki/Facebook) (Facebook Connect) and [Google](https://en.wikipedia.org/wiki/Google) (Google Sign-In), that have control of the information associated with their identity.

## Mental Models
Not specified

## Crosswalk References
Not specified
