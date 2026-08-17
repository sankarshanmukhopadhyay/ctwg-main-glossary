---
title: "governance-framework"
---

> Generated file. Update `glossary/terms/governance-framework.yaml` and regenerate artifacts instead of editing this page directly.

# governance-framework

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A collection of one or more governance documents published by the governing body of a trust community that defines the rules, roles, responsibilities, and decision rights under which that community operates.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
governance framework, governance frameworks

## See Also
- [policy]({{ '/terms/policy/' | relative_url }})
- [requirement]({{ '/terms/requirement/' | relative_url }})
- [governance]({{ '/terms/governance/' | relative_url }})
- [governing-authority]({{ '/terms/governing-authority/' | relative_url }})
- [trust-registry]({{ '/terms/trust-registry/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/governance-framework.md`

## Governance Profile
- **Authority scope**: policy_definition, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- audit_log
- status_record
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- audit_log
- status_record
- verification_log
- registry_entry

## Notes
- In the digital identity industry specifically, a governance framework is better known as a trust framework. ToIP-conformant governance frameworks conform to the ToIP Governance Architecture Specification and follow the ToIP Governance Metamodel.

## Supporting Definitions
- Also known as: [[ref: trust framework]].

## Mental Models
Not specified

## Crosswalk References
Not specified
