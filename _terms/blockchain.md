---
title: "blockchain"
---

# blockchain

A simple-English summary has not yet been added for this concept.

## Formal definition
A distributed ledger of cryptographically-signed transactions that are grouped into blocks. Each block is cryptographically linked to the previous one (making it tamper evident) after validation and undergoing a consensus decision. As new blocks are added, older blocks become more difficult to modify (creating tamper resistance). New blocks are replicated across copies of the ledger within the network, and any conflicts are resolved automatically using established rules.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **blockchains** (`en`, `alternative`)

### Related concepts
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [requirement]({{ '/terms/requirement/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:policy`
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:requirement`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:blockchain`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/blockchain)

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
blockchain, blockchains

### Governance profile
- **Authority scope**: policy_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval

### Assurance
**Evidence artifacts**
- policy_document

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- policy_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document

### Notes
Not specified

### Supporting definitions
- [Wikipedia:](https://en.wikipedia.org/wiki/Blockchain) A [distributed ledger](https://en.wikipedia.org/wiki/Distributed_ledger) with growing lists of [records](https://en.wikipedia.org/wiki/Record_\(computer_science\)) (blocks) that are securely linked together via [cryptographic hashes](https://en.wikipedia.org/wiki/Cryptographic_hash_function). Each block contains a cryptographic hash of the previous block, a [timestamp](https://en.wikipedia.org/wiki/Trusted_timestamping), and transaction data (generally represented as a [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree), where [data nodes](https://en.wikipedia.org/wiki/Node_\(computer_science\)) are represented by leaves). Since each block contains information about the previous block, they effectively form a chain (compare [linked list](https://en.wikipedia.org/wiki/Linked_list) data structure), with each additional block linking to the ones before it. Consequently, blockchain transactions are irreversible in that, once they are recorded, the data in any given block cannot be altered retroactively without altering all subsequent blocks.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/blockchain.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
