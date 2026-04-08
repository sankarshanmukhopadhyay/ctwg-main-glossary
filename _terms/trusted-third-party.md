---
title: "trusted-third-party"
---

# trusted-third-party

## Definition
In cryptography, a trusted third party (TTP) is an entity which facilitates interactions between two parties who both trust the third party; the third party reviews all critical transaction communications between the parties, based on the ease of creating fraudulent digital content. In TTP models, the relying parties use this trust to secure their own interactions. TTPs are common in any number of commercial transactions and in cryptographic digital transactions as well as cryptographic protocols, for example, a certificate authority (CA) would issue a digital certificate to one of two parties. The CA then becomes the TTP to that certificate's issuance. Likewise transactions that need a third party recordation would also need a third-party repository service of some kind.

## Aliases
trusted third party, trusted third parties, trusted 3rd party, trusted 3rd parties, TTP, TTPs

## Governance Profile
- **Authority scope**: verification_and_reliance, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- verification_log

## Notes
Not specified

## Supporting Definitions
- Also known as: [[ref: TTP]].
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/trusted_third_party): A third party, such as a CA, that is trusted by its clients to perform certain services. (By contrast, the two participants in a key-establishment transaction are considered to be the first and second parties.)

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
