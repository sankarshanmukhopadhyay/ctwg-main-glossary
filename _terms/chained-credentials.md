---
title: "chained-credentials"
---

> Generated file. Update `glossary/terms/chained-credentials.yaml` and regenerate artifacts instead of editing this page directly.

# chained-credentials

## In Simple English
Two or more credentials linked together to create a trust chain between the credentials that is cryptographically verifiable.

## Definition
Two or more credentials linked together to create a trust chain between the credentials that is cryptographically verifiable.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
chained credentials

## See Also
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/chained-credentials.md`

## Governance Profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: design
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
- ACDCs are a type of digital credential that explicitly supports chaining.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
