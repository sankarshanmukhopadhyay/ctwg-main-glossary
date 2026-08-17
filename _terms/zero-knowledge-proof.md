---
title: "zero-knowledge-proof"
---

# zero-knowledge-proof

A simple-English summary has not yet been added for this concept.

## Formal definition
A specific kind of cryptographic proof that proves facts about data to a verifier without revealing the underlying data itself. A common example is proving that a person is over or under a specific age without revealing the person’s exact birthdate.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **zero-knowledge proof** (`en`, `alternative`)
- **zero-knowledge proofs** (`en`, `alternative`)
- **ZKP** (`en`, `alternative`)
- **ZKPs** (`en`, `alternative`)

### Related concepts
- [verification]({{ '/terms/verification/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})
- [relying-party]({{ '/terms/relying-party/' | relative_url }})
- [trust-decision]({{ '/terms/trust-decision/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:verification`
- **related**: `urn:tig:concept:verifier`
- **related**: `urn:tig:concept:relying-party`
- **related**: `urn:tig:concept:trust-decision`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:zero-knowledge-proof`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/zero-knowledge-proof.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
zero-knowledge proof, zero-knowledge proofs, ZKP, ZKPs

### Governance profile
- **Authority scope**: verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision

### Assurance
**Evidence artifacts**
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision

- **Accountable entity**: verifier_operator

**Evidence produced**
- verification_log

### Notes
Not specified

### Supporting definitions
- Also known as: zero-knowledge protocol, [[ref: ZKP]].
- [Ethereum:](https://ethereum.org/en/zero-knowledge-proofs/) A zero-knowledge proof is a way of proving the validity of a statement without revealing the statement itself.
- [Wikipedia](https://en.wikipedia.org/wiki/Zero-knowledge_proof): a method by which one [[ref: party]] (the prover) can prove to another party (the verifier) that a given statement is true, while avoiding conveying to the [[ref: verifier]] any information beyond the mere fact of the statement's truth.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/zero-knowledge-proof.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
