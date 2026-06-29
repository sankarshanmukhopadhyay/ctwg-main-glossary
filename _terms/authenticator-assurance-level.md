---
title: "authenticator-assurance-level"
---

> Generated file. Update `glossary/terms/authenticator-assurance-level.yaml` and regenerate artifacts instead of editing this page directly.

# authenticator-assurance-level

## Definition
A measure of the strength of an authentication mechanism and, therefore, the confidence in it.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
authenticator assurance level, authenticator assurance levels, AAL, AALs

## See Also
- [federation assurance level]({{ '/terms/federation-assurance-level/' | relative_url }})
- [identity assurance level]({{ '/terms/identity-assurance-level/' | relative_url }})
- [identity binding]({{ '/terms/identity-binding/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/authenticator_assurance_level).

## Governance Profile
- **Authority scope**: access_decisioning, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- access_decision

## Assurance
**Evidence artifacts**
- attestation
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- attestation
- access_decision_log

## Notes
- In NIST SP 800-63-3, AAL is defined in terms of three levels: AAL1 (Some confidence), AAL2 (High confidence), AAL3 (Very high confidence).

## Supporting Definitions
- Also known as: [[ref: AAL]]

## Mental Models
Not specified

## Crosswalk References
Not specified
