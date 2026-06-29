---
title: "sender-constrained-token"
---

> Generated file. Update `glossary/terms/sender-constrained-token.yaml` and regenerate artifacts instead of editing this page directly.

# sender-constrained-token

## Definition
A token whose use is cryptographically constrained to a specific sender or key holder, reducing replay risk if the token is copied.

## Reader Note
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

## Implementation Relevance
Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Aliases
sender constrained token

## See Also
- [dpop]({{ '/terms/dpop/' | relative_url }})
- [proof-of-possession]({{ '/terms/proof-of-possession/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [access-control]({{ '/terms/access-control/' | relative_url }})

## Standards and Source References
- [OAuth 2.0 Demonstrating Proof of Possession](https://www.rfc-editor.org/rfc/rfc9449.html) (IETF; RFC; 9449; 2023-09) — normative

## Governance Profile
- **Authority scope**: access_decisioning, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- access_decision
- reliance_decision

## Assurance
**Evidence artifacts**
- access_decision_log
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- access_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log
- verification_log
- audit_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **IETF**: RFC 9449
