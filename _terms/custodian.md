---
title: "custodian"
---

> Generated file. Update `glossary/terms/custodian.yaml` and regenerate artifacts instead of editing this page directly.

# custodian

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A third party that has been assigned rights and duties in a custodianship arrangement for the purpose of hosting and safeguarding a principal's private keys, digital wallet and digital assets on the principal’s behalf. Depending on the custodianship arrangement, the custodian may act as an exchange and provide additional services, such as staking, lending, account recovery, or security features.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
custodian, custodians

## See Also
- [custodial wallet]({{ '/terms/custodial-wallet/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/custodian.md`

## Governance Profile
- **Authority scope**: terminology_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- definition_approval

## Assurance
**Evidence artifacts**
- definition_change_record
- policy_document
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- definition_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- definition_change_record
- policy_document
- audit_log

## Notes
- While a custodian technically has the necessary access to in theory impersonate the principal, in most cases a custodian is expressly prohibited from taking any action on the principal’s account unless explicitly authorized by the principal. This is what distinguishes custodianship from guardianship.

## Supporting Definitions
- Contrast with: [[ref: guardian]], [[ref: zero-knowledge service provider]].
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/custodian): A third-party [[ref: entity]] that holds and safeguards a user’s [[ref: private keys]] or digital assets on their behalf. Depending on the system, a custodian may act as an exchange and provide additional services, such as staking, lending, account recovery, or security features.

## Mental Models
Not specified

## Crosswalk References
Not specified
