---
title: "guardian"
---

> Generated file. Update `glossary/terms/guardian.yaml` and regenerate artifacts instead of editing this page directly.

# guardian

## Definition
A party that has been assigned rights and duties in a guardianship arrangement for the purpose of caring for, protecting, guarding, and defending the entity that is the dependent in that guardianship arrangement. In the context of decentralized digital trust infrastructure, a guardian is issued guardianship credentials into their own digital wallet in order to perform such actions on behalf of the dependent as are required by this role.

## Aliases
guardian, guardians

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
- A guardian is a very different role than a custodian, who does not take any actions on behalf of a principal unless explicitly authorized.

## Supporting Definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Legal_guardian): A legal guardian is a person who has been appointed by a court or otherwise has the legal authority (and the corresponding [duty](https://en.wikipedia.org/wiki/Duty)) to make decisions relevant to the personal and [property](https://en.wikipedia.org/wiki/Property) interests of another person who is deemed incompetent, called a [ward](https://en.wikipedia.org/wiki/Ward_\(law\)).
- For more information, see: [On Guardianship in Self-Sovereign Identity V2.0](https://sovrin.org/wp-content/uploads/Guardianship-Whitepaper-V2.0.pdf) (April, 2023).

## Mental Models
- [eSSIF-Lab Guardianship](https://essif-lab.github.io/framework/docs/terms/pattern-guardianship)

## See Also
- custodian
- zero-knowledge service provider.

## Crosswalk References
Not specified
