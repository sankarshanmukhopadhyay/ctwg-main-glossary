---
title: "identity-assurance-level"
---

> Generated file. Update `glossary/terms/identity-assurance-level.yaml` and regenerate artifacts instead of editing this page directly.

# identity-assurance-level

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A category that conveys the degree of confidence that a person’s claimed identity is their real identity, for example as defined in NIST SP 800-63-3 in terms of three levels: IAL 1 (Some confidence), IAL 2 (High confidence), IAL 3 (Very high confidence).

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
identity assurance level, identity assurance levels, IAL, IALs

## See Also
- [authenticator assurance level]({{ '/terms/authenticator-assurance-level/' | relative_url }})
- [federation assurance level]({{ '/terms/federation-assurance-level/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/identity_assurance_level).

## Governance Profile
- **Authority scope**: credential_issuance, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision

## Assurance
**Evidence artifacts**
- issuance_log
- attestation

- **Assurance level hint**: AL1+
- **Auditability**: moderate

## Control Plane
**Decision points**
- issuance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- attestation

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
