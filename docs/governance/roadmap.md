---
title: "Governance Improvement Roadmap"
parent: Governance Documentation
nav_order: 40
---

# Governance Improvement Roadmap

## Completed: v1.1.0 assurance-ready infrastructure

- schema-aware validation using `jsonschema`
- controlled vocabularies for governance and assurance fields
- schema-aligned examples under `examples/governance-term/`
- generated governance quality report
- generated artifact manifest
- CI updates for validation, generation, quality reporting, and drift detection
- refreshed maintainer and contributor documentation

## Completed: v1.2.0 standards-linked glossary refresh

- added structured citation support for standards and specifications
- expanded coverage for VC 2.0, OpenID4VCI, OpenID4VP, SD-JWT VC, OpenID Federation, EUDI Wallet, DPoP, and C2PA vocabulary
- improved generated term pages with reader notes, implementation relevance, source references, and linked related terms
- added internal `see_also` and reference-marker validation
- synchronized governance documentation and generated quality-report views

## Next: standards mapping hardening

- continue converting legacy source strings into structured citation objects
- add curated standards profiles for W3C, OpenID, IETF, C2PA, EU, ISO, NIST, DIF, and ToIP mappings
- add optional external link checking in CI when network access is available
- refine crosswalks for high-impact governance concepts

## Next: downstream consumption support

- publish stable guidance for policy engines, conformance suites, trust registries, and assurance dashboards
- document artifact versioning expectations
- define compatibility expectations for consumers of generated JSON and JSON-LD artifacts
- consider a dedicated JSON-LD context once downstream consumers stabilize

## Future: assurance and conformance alignment

- define AL3+ term-quality expectations for high-assurance ecosystems
- add optional conformance profiles for downstream consumers
- link glossary terms to external trust infrastructure schemas where appropriate
- provide machine-readable mappings for standards working groups and governance frameworks
