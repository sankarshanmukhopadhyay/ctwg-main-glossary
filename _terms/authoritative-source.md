---
title: "authoritative-source"
---

> Generated file. Update `glossary/terms/authoritative-source.yaml` and regenerate artifacts instead of editing this page directly.

# authoritative-source

## Definition
A source of information that a relying party considers to be authoritative for that information. In ToIP architecture, the trust registry authorized by the governance framework for a trust community is typically considered an authoritative source by the members of that trust community. A system of record is an authoritative source for the data records it holds. A trust anchor is an authoritative source for the beginning of a trust chain.

## Aliases
authoritative source, authoritative sources

## Governance Profile
- **Authority scope**: verification_and_reliance, policy_definition, registry_management, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- registration_decision
- reliance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- registry_entry
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- registration_decision
- reliance_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- registry_entry
- verification_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- verification
- verifier
- relying-party
- trust-decision
- policy
- governance-framework

## Crosswalk References
Not specified
