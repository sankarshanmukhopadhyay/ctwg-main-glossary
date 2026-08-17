---
title: "public-key-infrastructure"
---

# public-key-infrastructure

A simple-English summary has not yet been added for this concept.

## Formal definition
A set of policies, processes, server platforms, software and workstations used for the purpose of administering certificates and public-private key pairs, including the ability to issue, maintain, and revoke public key certificates. The PKI includes the hierarchy of certificate authorities that allow for the deployment of digital certificates that support encryption, digital signature and authentication to meet business and security requirements.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **public key infrastructure** (`en`, `alternative`)
- **public key infrastructures** (`en`, `alternative`)
- **PKI** (`en`, `alternative`)
- **PKIs** (`en`, `alternative`)

### Related concepts
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})
- [role-based-access-control]({{ '/terms/role-based-access-control/' | relative_url }})
- [attribute-based-access-control]({{ '/terms/attribute-based-access-control/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:permission`
- **related**: `urn:tig:concept:role-based-access-control`
- **related**: `urn:tig:concept:attribute-based-access-control`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:public-key-infrastructure`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/public_key_infrastructure).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
public key infrastructure, public key infrastructures, PKI, PKIs

### Governance profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- access_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- status_record
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- status_record
- access_decision_log

### Notes
Not specified

### Supporting definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Public_key_infrastructure): A public key infrastructure (PKI) is a set of roles, policies, hardware, software and procedures needed to create, manage, distribute, use, store and revoke [digital certificates](https://en.wikipedia.org/wiki/Public_key_certificate) and manage [public-key encryption](https://en.wikipedia.org/wiki/Public-key_cryptography). The purpose of a PKI is to facilitate the secure electronic transfer of information for a range of network activities such as e-commerce, internet banking and confidential email.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/public-key-infrastructure.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
