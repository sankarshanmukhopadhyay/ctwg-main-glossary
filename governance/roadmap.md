---
title: "Governance Improvement Roadmap"
parent: "Project"
nav_order: 3
---

# Governance Improvement Roadmap

## Completed: v2.0.0 independent concept system

- renamed and repositioned the project as the **Trust Infrastructure Glossary**
- replaced upstream synchronization with governed source intake and provenance review
- preserved Trust over IP lineage without retaining upstream authority
- introduced stable `urn:tig:concept:*` identifiers
- separated concepts from language-tagged designations
- introduced designation states: preferred, alternative, deprecated, discouraged
- separated editorial maturity from represented lifecycle semantics
- introduced adopted, adapted, locally defined, and mapped provenance classifications
- added SKOS-aligned semantic relations and cross-vocabulary mapping relations
- added JSON-LD and SKOS-compatible Turtle generation
- added vocabulary profiles and profile validation
- retained v1 compatibility fields and artifact filenames during migration
- refreshed reader navigation, governance docs, contribution guidance, release metadata, and Pages identity

## Next: v2.1 source-corpus mapping

- review priority concepts against W3C SKOS/DCMI, OpenSSF, CNCF, Schema.org, SPDX, ToIP, DTG, CAWG, OpenID, IETF, C2PA, EUDI, DIF, NIST, and ISO sources
- populate `exact`, `close`, `broad`, `narrow`, and `related` mappings only after semantic review
- convert more legacy source strings to structured citations
- add machine-readable source-corpus inventories and license metadata

## Next: plain-English coverage

- extend `simple_definition` coverage
- add comprehension checks that do not treat readability formulas as semantic truth
- add explicit review status for simple-language quality

## Next: localization readiness

- document translation governance
- support more than one preferred designation by language while preserving one preferred designation per language
- define translation provenance and review expectations

## Future: profile and namespace ecosystem

- allow downstream projects to publish interoperable TIG-derived profiles
- document local concept namespaces and mapping expectations
- add versioned compatibility guidance for profile consumers
- consider stable HTTP concept identifiers if long-term hosting governance is established
