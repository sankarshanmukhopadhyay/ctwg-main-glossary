---
title: "digital-trust-ecosystem"
---

> Generated file. Update `glossary/terms/digital-trust-ecosystem.yaml` and regenerate artifacts instead of editing this page directly.

# digital-trust-ecosystem

## Definition
A digital ecosystem in which the participants are one or more interoperating trust communities. Governance of the various roles of governed parties within a digital trust ecosystem (e.g., issuers, holders, verifiers, certification bodies, auditors) is typically managed by a governing body using a governance framework as recommended in the ToIP Governance Stack. Many digital trust ecosystems will also maintain one or more trust lists and/or trust registries.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
digital trust ecosystem, digital trust ecosystems

## See Also
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/digital-trust-ecosystem.md`

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance, policy_definition, registry_management, assurance_and_audit, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- registration_decision
- reliance_decision
- issuance_decision

## Assurance
**Evidence artifacts**
- policy_document
- registry_entry
- issuance_log
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- registration_decision
- reliance_decision
- issuance_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- registry_entry
- issuance_log
- verification_log
- audit_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
