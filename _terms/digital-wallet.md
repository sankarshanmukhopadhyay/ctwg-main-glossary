---
title: "digital-wallet"
---

# digital-wallet

## Definition
A user agent, optionally including a hardware component, capable of securely storing and processing cryptographic keys, digital credentials, digital assets and other sensitive private data that enables the controller to perform cryptographically verifiable operations. A non-custodial wallet is directly in the custody of a principal. A custodial wallet is in the custody of a third party. Personal wallets are held by individual persons; enterprise wallets are held by organizations or other legal entities.

## Aliases
digital wallet, digital wallets

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance, delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- reliance_decision
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- delegation_record
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- issuance_log
- verification_log

## Notes
- In market parlance, a mobile app that performs the actions of a digital agent and has access to a set of cryptographic keys is often simply called a wallet or a digital wallet.

## Supporting Definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#wallet): a component that implements the [capability](https://essif-lab.github.io/framework/docs/terms/capability) to securely store data as requested by [colleague agents](https://essif-lab.github.io/framework/docs/terms/colleague), and to provide stored data to [colleague agents](https://essif-lab.github.io/framework/docs/terms/colleague) or [peer agents](https://essif-lab.github.io/framework/docs/terms/peer-agent), all in [compliance](https://essif-lab.github.io/framework/docs/terms/compliance) with the rules of its [principal](https://essif-lab.github.io/framework/docs/terms/principal)'s [wallet policy](https://essif-lab.github.io/framework/docs/terms/wallet-policy).
- [Wikipedia](https://en.wikipedia.org/wiki/Digital_wallet): A digital wallet, also known as an e-wallet, is an [electronic device](https://en.wikipedia.org/wiki/Consumer_electronics), [online service](https://en.wikipedia.org/wiki/Online_service_provider), or [software program](https://en.wikipedia.org/wiki/Computer_program) that allows one party to make [electronic transactions](https://en.wikipedia.org/wiki/Electronic_transaction) with another party bartering [digital currency](https://en.wikipedia.org/wiki/Digital_currency) units for [goods and services](https://en.wikipedia.org/wiki/Goods_and_services). This can include purchasing items either [online](https://en.wikipedia.org/wiki/Online_and_offline) or at the [point of sale](https://en.wikipedia.org/wiki/Point_of_sale) in a [brick and mortar](https://en.wikipedia.org/wiki/Brick_and_mortar) store, using either [mobile payment](https://en.wikipedia.org/wiki/Mobile_payment) (on a [smartphone](https://en.wikipedia.org/wiki/Smartphone) or other [mobile device](https://en.wikipedia.org/wiki/Mobile_device)) or (for online buying only) using a [laptop](https://en.wikipedia.org/wiki/Laptop) or other [personal computer](https://en.wikipedia.org/wiki/Personal_computer). Money can be deposited in the digital wallet prior to any transactions or, in other cases, an individual's bank account can be linked to the digital wallet. Users might also have their [driver's license](https://en.wikipedia.org/wiki/Driver%27s_license), [health card](https://en.wikipedia.org/wiki/Health_Care_Card), loyalty card(s) and other ID documents stored within the wallet. The credentials can be passed to a merchant's terminal wirelessly via [near field communication](https://en.wikipedia.org/wiki/Near_field_communication) (NFC).

## Mental Models
Not specified

## See Also
- digital agent
- key management system
- wallet engine.

## Crosswalk References
Not specified
