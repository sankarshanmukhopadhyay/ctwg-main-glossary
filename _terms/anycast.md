---
title: "anycast"
---

# anycast

A simple-English summary has not yet been added for this concept.

## Formal definition
Anycast is a network addressing and routing methodology in which a single IP-address is shared by devices (generally servers) in multiple locations. Routers direct packets addressed to this destination to the location nearest the sender, using their normal decision-making algorithms, typically the lowest number of BGP network hops. Anycast routing is widely used by content delivery networks such as web and name servers, to bring their content closer to end users.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
None

### Related concepts
- [broadcast]({{ '/terms/broadcast/' | relative_url }})
- [multicast]({{ '/terms/multicast/' | relative_url }})
- [unicast]({{ '/terms/unicast/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:broadcast`
- **related**: `urn:tig:concept:multicast`
- **related**: `urn:tig:concept:unicast`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:anycast`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Wikipedia](https://en.wikipedia.org/wiki/Anycast).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
anycast

### Governance profile
- **Authority scope**: terminology_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: reference_term

### Enforcement points
- definition_approval

### Assurance
**Evidence artifacts**
- definition_change_record

- **Assurance level hint**: informative
- **Auditability**: basic

### Control plane
**Decision points**
- definition_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- definition_change_record

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/anycast.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
