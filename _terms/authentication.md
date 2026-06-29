---
title: "authentication"
---

> Generated file. Update `glossary/terms/authentication.yaml` and regenerate artifacts instead of editing this page directly.

# authentication

## Definition
Verifying the identity of a user, process, or device, often as a prerequisite to allowing access to resources in an information system.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
authentication, authenticate, authenticates, authenticated, authenticating

## See Also
- [authenticator]({{ '/terms/authenticator/' | relative_url }})
- [verifiable message]({{ '/terms/verifiable-message/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/authentication).

## Governance Profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

## Notes
Not specified

## Supporting Definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Authentication): The act of proving an [assertion](https://en.wikipedia.org/wiki/Logical_assertion), such as the [identity](https://en.wikipedia.org/wiki/Digital_identity) of a computer system user.

## Mental Models
Not specified

## Crosswalk References
- **NIST**: IA-2
- **ISO**: ISO/IEC 27001 A.5.17
