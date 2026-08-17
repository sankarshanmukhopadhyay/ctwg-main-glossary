---
title: "policy"
---

# policy

A rule or set of rules that says what is allowed, required, or prohibited in a defined context.

## Formal definition
Statements, rules, or assertions that specify required, permitted, prohibited, or expected behavior of an entity within a defined scope. Policies may be human-readable, machine-readable, or both, and may be interpreted, enforced, or audited by people, software, or both.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **policies** (`en`, `alternative`)

### Related concepts
- [governance framework]({{ '/terms/governance-framework/' | relative_url }})
- [governance requirement]({{ '/terms/governance-requirement/' | relative_url }})
- [rule]({{ '/terms/rule/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:governance-requirement`
- **related**: `urn:tig:concept:rule`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:policy`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/policy)

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
policy, policies

### Governance profile
- **Authority scope**: policy_definition, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- revocation_decision

### Assurance
**Evidence artifacts**
- policy_document
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- policy_approval
- revocation_decision

- **Accountable entity**: auditor

**Evidence produced**
- policy_document
- audit_log

### Notes
Not specified

### Supporting definitions
- Example: An [[ref: authorization]] policy might specify the [[ref: access control]] rules applied by a software component at runtime.

### Mental models
Not specified

### Crosswalk references
- **NIST**: PL-1
- **ISO**: ISO/IEC 42001 5.2

</details>

---

*Generated from `glossary/terms/policy.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
