---
title: "public-key-infrastructure"
---

> Generated file. Update `glossary/terms/public-key-infrastructure.yaml` and regenerate artifacts instead of editing this page directly.

# public-key-infrastructure

## Definition
A set of policies, processes, server platforms, software and workstations used for the purpose of administering certificates and public-private key pairs, including the ability to issue, maintain, and revoke public key certificates. The PKI includes the hierarchy of certificate authorities that allow for the deployment of digital certificates that support encryption, digital signature and authentication to meet business and security requirements.

## Aliases
public key infrastructure, public key infrastructures, PKI, PKIs

## Governance Profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- status_record
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- status_record
- access_decision_log

## Notes
Not specified

## Supporting Definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Public_key_infrastructure): A public key infrastructure (PKI) is a set of roles, policies, hardware, software and procedures needed to create, manage, distribute, use, store and revoke [digital certificates](https://en.wikipedia.org/wiki/Public_key_certificate) and manage [public-key encryption](https://en.wikipedia.org/wiki/Public-key_cryptography). The purpose of a PKI is to facilitate the secure electronic transfer of information for a range of network activities such as e-commerce, internet banking and confidential email.

## Mental Models
Not specified

## See Also
- authorization
- permission
- role-based-access-control
- attribute-based-access-control

## Crosswalk References
Not specified
