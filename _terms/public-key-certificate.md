---
title: "public-key-certificate"
---

> Generated file. Update `glossary/terms/public-key-certificate.yaml` and regenerate artifacts instead of editing this page directly.

# public-key-certificate

## Concept Identity
- **Concept ID**: `urn:tig:concept:public-key-certificate`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A set of data that uniquely identifies a public key (which has a corresponding private key) and an owner that is authorized to use the key pair. The certificate contains the owner’s public key and possibly other information and is digitally signed by a certification authority (i.e., a trusted party), thereby binding the public key to the owner.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **public key certificate** (`en`, `alternative`)
- **public key certificates** (`en`, `alternative`)
- **PKC** (`en`, `alternative`)
- **PKCs** (`en`, `alternative`)

## Legacy Aliases
public key certificate, public key certificates, PKC, PKCs

## Semantic Relations
- **related**: `urn:tig:concept:public-key-infrastructure`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [public key infrastructure]({{ '/terms/public-key-infrastructure/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/public_key_certificate).

## Governance Profile
- **Authority scope**: governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- revocation_decision

## Assurance
**Evidence artifacts**
- definition_change_record
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- definition_change_record
- status_record
- audit_log
- verification_log
- registry_entry

## Notes
Not specified

## Supporting Definitions
- Wikipedia : In [cryptography](https://en.wikipedia.org/wiki/Cryptography), a public key certificate, also known as a digital certificate or identity certificate, is an [electronic document](https://en.wikipedia.org/wiki/Electronic_document) used to prove the validity of a [public key](https://en.wikipedia.org/wiki/Key_authentication). The certificate includes information about the key, information about the identity of its owner (called the subject), and the [digital signature](https://en.wikipedia.org/wiki/Digital_signature) of an entity that has verified the certificate's contents (called the issuer). If the signature is valid, and the software examining the certificate trusts the issuer, then it can use that key to communicate securely with the certificate's subject. In [email encryption](https://en.wikipedia.org/wiki/Email_encryption), [code signing](https://en.wikipedia.org/wiki/Code_signing), and [e-signature](https://en.wikipedia.org/wiki/Electronic_signature) systems, a certificate's subject is typically a person or organization. However, in [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS) a certificate's subject is typically a computer or other device, though TLS certificates may identify organizations or individuals in addition to their core role in identifying devices.

## Mental Models
Not specified

## Crosswalk References
Not specified
