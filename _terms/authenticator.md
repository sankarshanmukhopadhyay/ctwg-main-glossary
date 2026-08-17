---
title: "authenticator"
---

> Generated file. Update `glossary/terms/authenticator.yaml` and regenerate artifacts instead of editing this page directly.

# authenticator

## In Simple English
Something the claimant possesses and controls (typically a cryptographic module or password) that is used to authenticate the claimant’s identity.

## Definition
Something the claimant possesses and controls (typically a cryptographic module or password) that is used to authenticate the claimant’s identity.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
authenticator

## See Also
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/authenticator).

## Governance Profile
- **Authority scope**: credential_issuance, access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- issuance_log
- access_decision_log
- policy_document
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- access_decision_log
- policy_document
- registry_entry
- status_record
- audit_log
- verification_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
