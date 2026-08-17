---
title: "anycast"
---

> Generated file. Update `glossary/terms/anycast.yaml` and regenerate artifacts instead of editing this page directly.

# anycast

## Concept Identity
- **Concept ID**: `urn:tig:concept:anycast`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
Anycast is a network addressing and routing methodology in which a single IP-address is shared by devices (generally servers) in multiple locations. Routers direct packets addressed to this destination to the location nearest the sender, using their normal decision-making algorithms, typically the lowest number of BGP network hops. Anycast routing is widely used by content delivery networks such as web and name servers, to bring their content closer to end users.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
None

## Legacy Aliases
anycast

## Semantic Relations
- **related**: `urn:tig:concept:broadcast`
- **related**: `urn:tig:concept:multicast`
- **related**: `urn:tig:concept:unicast`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [broadcast]({{ '/terms/broadcast/' | relative_url }})
- [multicast]({{ '/terms/multicast/' | relative_url }})
- [unicast]({{ '/terms/unicast/' | relative_url }})

## Standards and Source References
- [Wikipedia](https://en.wikipedia.org/wiki/Anycast).

## Governance Profile
- **Authority scope**: terminology_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: reference_term

## Enforcement Points
- definition_approval

## Assurance
**Evidence artifacts**
- definition_change_record

- **Assurance level hint**: informative
- **Auditability**: basic

## Control Plane
**Decision points**
- definition_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- definition_change_record

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
