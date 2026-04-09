---
title: "certificate-authority"
---

> Generated file. Update `glossary/terms/certificate-authority.yaml` and regenerate artifacts instead of editing this page directly.

# certificate-authority

## Definition
The entity in a public key infrastructure (PKI) that is responsible for issuing public key certificates and exacting compliance to a PKI policy.

## Aliases
certificate authority, certificate authorities

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

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document

## Notes
Not specified

## Supporting Definitions
- Also known as: [[ref: certification authority]].
- [Wikipedia](https://en.wikipedia.org/wiki/Certificate_authority): In [cryptography](https://en.wikipedia.org/wiki/Cryptography), a certificate authority or certification authority (CA) is an entity that stores, signs, and issues [digital certificates](https://en.wikipedia.org/wiki/Public_key_certificate). A digital certificate certifies the ownership of a public key by the named subject of the certificate. This allows others (relying parties) to rely upon signatures or on assertions made about the private key that corresponds to the certified public key. A CA acts as a trusted third party—trusted both by the subject (owner) of the certificate and by the party relying upon the certificate.[<sup>\[1\]</sup>](https://en.wikipedia.org/wiki/Certificate_authority#cite_note-1) The format of these certificates is specified by the [X.509](https://en.wikipedia.org/wiki/X.509) or [EMV](https://en.wikipedia.org/wiki/EMV) standard.

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
