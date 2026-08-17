---
title: "autonomic-namespace"
---

# autonomic-namespace

A simple-English summary has not yet been added for this concept.

## Formal definition
a namespace that is self-certifying and hence self-administrating. An AN has a self-certifying prefix that provides cryptographic verification of root control authority over its namespace. All derived AIDs in the same AN share the same root-of-trust, source-of-truth, and locus-of-control (RSL). The governance of the namespace is, therefore, unified into one entity, that is, the controller who is/holds the root authority over the namespace.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **autonomic namespace** (`en`, `alternative`)

### Related concepts
- [governance]({{ '/terms/governance/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [governing-authority]({{ '/terms/governing-authority/' | relative_url }})
- [trust-registry]({{ '/terms/trust-registry/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:governance`
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:governing-authority`
- **related**: `urn:tig:concept:trust-registry`
- **related**: `urn:tig:concept:revocation`
- **related**: `urn:tig:concept:verification`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:autonomic-namespace`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- Dr. S.Smith, 2024

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
autonomic-namespace, autonomic namespace

### Governance profile
- **Authority scope**: governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- revocation_decision

### Assurance
**Evidence artifacts**
- definition_change_record
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- definition_change_record
- status_record
- audit_log
- verification_log
- registry_entry

### Notes
Not specified

### Supporting definitions
- Namespaces are, therefore, portable and truly self-sovereign.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/autonomic-namespace.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
