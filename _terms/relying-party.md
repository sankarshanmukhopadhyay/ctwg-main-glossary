---
title: "relying-party"
---

> Generated file. Update `glossary/terms/relying-party.yaml` and regenerate artifacts instead of editing this page directly.

# relying-party

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A party who accepts claims, credentials, trust graphs, or any other form of verifiable data from other parties (such as issuers, holders, trust registries, or other authoritative sources) in order to make a trust decision.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
relying party, relying parties

## See Also
- [verifier]({{ '/terms/verifier/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/relying-party.md`

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance, governance_recognition
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
- The term “relying party” is more commonly used in federated identity architecture; the term “verifier” is more commonly used with decentralized identity architecture and verifiable credentials.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
