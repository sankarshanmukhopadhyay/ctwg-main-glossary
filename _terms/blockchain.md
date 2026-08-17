---
title: "blockchain"
---

> Generated file. Update `glossary/terms/blockchain.yaml` and regenerate artifacts instead of editing this page directly.

# blockchain

## Concept Identity
- **Concept ID**: `urn:tig:concept:blockchain`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A distributed ledger of cryptographically-signed transactions that are grouped into blocks. Each block is cryptographically linked to the previous one (making it tamper evident) after validation and undergoing a consensus decision. As new blocks are added, older blocks become more difficult to modify (creating tamper resistance). New blocks are replicated across copies of the ledger within the network, and any conflicts are resolved automatically using established rules.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **blockchains** (`en`, `alternative`)

## Legacy Aliases
blockchain, blockchains

## Semantic Relations
- **related**: `urn:tig:concept:policy`
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:requirement`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [requirement]({{ '/terms/requirement/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/blockchain)

## Governance Profile
- **Authority scope**: policy_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval

## Assurance
**Evidence artifacts**
- policy_document

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document

## Notes
Not specified

## Supporting Definitions
- [Wikipedia:](https://en.wikipedia.org/wiki/Blockchain) A [distributed ledger](https://en.wikipedia.org/wiki/Distributed_ledger) with growing lists of [records](https://en.wikipedia.org/wiki/Record_\(computer_science\)) (blocks) that are securely linked together via [cryptographic hashes](https://en.wikipedia.org/wiki/Cryptographic_hash_function). Each block contains a cryptographic hash of the previous block, a [timestamp](https://en.wikipedia.org/wiki/Trusted_timestamping), and transaction data (generally represented as a [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree), where [data nodes](https://en.wikipedia.org/wiki/Node_\(computer_science\)) are represented by leaves). Since each block contains information about the previous block, they effectively form a chain (compare [linked list](https://en.wikipedia.org/wiki/Linked_list) data structure), with each additional block linking to the ones before it. Consequently, blockchain transactions are irreversible in that, once they are recorded, the data in any given block cannot be altered retroactively without altering all subsequent blocks.

## Mental Models
Not specified

## Crosswalk References
Not specified
