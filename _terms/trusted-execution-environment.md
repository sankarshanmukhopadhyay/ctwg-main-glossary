---
title: "trusted-execution-environment"
---

> Generated file. Update `glossary/terms/trusted-execution-environment.yaml` and regenerate artifacts instead of editing this page directly.

# trusted-execution-environment

## Definition
A trusted execution environment (TEE) is a secure area of a main processor. It helps code and data loaded inside it to be protected with respect to confidentiality and integrity. Data integrity prevents unauthorized entities from outside the TEE from altering data, while code integrity prevents code in the TEE from being replaced or modified by unauthorized entities, which may also be the computer owner itself as in certain DRM schemes.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
trusted execution environment, trusted execution environments, TEE, TEEs

## See Also
- [Secure Enclave]({{ '/terms/secure-enclave/' | relative_url }})

## Standards and Source References
- [Wikipedia](https://en.wikipedia.org/wiki/Trusted_execution_environment).

## Governance Profile
- **Authority scope**: terminology_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
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
Not specified

## Supporting Definitions
- Also known as: [[ref: TEE]].

## Mental Models
Not specified

## Crosswalk References
Not specified
