---
title: "trust-establishment"
---

> Generated file. Update `glossary/terms/trust-establishment.yaml` and regenerate artifacts instead of editing this page directly.

# trust-establishment

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
The process two or more parties go through to establish a trust relationship. In the context of decentralized digital trust infrastructure, trust establishment takes place at two levels. At the technical trust level, it includes some form of key establishment. At the human trust level, it may be accomplished via an out-of-band introduction, the exchange of digital credentials, queries to one or more trust registries, or evaluation of some combination of human-readable and machine-readable governance frameworks.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
trust establishment

## See Also
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/trust-establishment.md`

## Governance Profile
- **Authority scope**: credential_issuance, policy_definition, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- issuance_log
- registry_entry
- audit_log
- status_record
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- issuance_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- issuance_log
- registry_entry
- audit_log
- status_record
- verification_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
