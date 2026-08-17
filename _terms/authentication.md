---
title: "authentication"
---

# authentication

Verifying the identity of a user, process, or device, often as a prerequisite to allowing access to resources in an information system.

## Formal definition
Verifying the identity of a user, process, or device, often as a prerequisite to allowing access to resources in an information system.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **authenticate** (`en`, `alternative`)
- **authenticates** (`en`, `alternative`)
- **authenticated** (`en`, `alternative`)
- **authenticating** (`en`, `alternative`)

### Related concepts
- [authenticator]({{ '/terms/authenticator/' | relative_url }})
- [verifiable message]({{ '/terms/verifiable-message/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authenticator`
- **related**: `urn:tig:concept:verifiable-message`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:authentication`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/authentication).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
authentication, authenticate, authenticates, authenticated, authenticating

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
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

### Notes
Not specified

### Supporting definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Authentication): The act of proving an [assertion](https://en.wikipedia.org/wiki/Logical_assertion), such as the [identity](https://en.wikipedia.org/wiki/Digital_identity) of a computer system user.

### Mental models
Not specified

### Crosswalk references
- **NIST**: IA-2
- **ISO**: ISO/IEC 27001 A.5.17

</details>

---

*Generated from `glossary/terms/authentication.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
