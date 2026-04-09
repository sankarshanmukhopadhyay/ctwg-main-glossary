---
title: "digital-vault"
---

> Generated file. Update `glossary/terms/digital-vault.yaml` and regenerate artifacts instead of editing this page directly.

# digital-vault

## Definition
A secure container for data whose controller is the principal. A digital vault is most commonly used in conjunction with a digital wallet and a digital agent. A digital vault may be implemented on a local device or in the cloud; multiple digital vaults may be used by the same principal across different devices and/or the cloud; if so they may use some type of synchronization. If the capability is supported, data may flow into or out of the digital vault automatically based on subscriptions approved by the controller.

## Aliases
digital vault, digital vaults

## Governance Profile
- **Authority scope**: delegation_and_scope, access_decisioning
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- access_decision

## Assurance
**Evidence artifacts**
- delegation_record
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- access_decision_log

## Notes
Not specified

## Supporting Definitions
- Also known as: [[ref: data vault]], [[ref: encrypted data vault]].
- For more information, see: <https://en.wikipedia.org/wiki/Personal_data_service>, <https://digitalbazaar.github.io/encrypted-data-vaults/>

## Mental Models
Not specified

## See Also
- enterprise data vault
- personal data vault
- virtual vault.

## Crosswalk References
Not specified
