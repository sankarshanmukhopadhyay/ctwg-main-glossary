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

## Next: source-quality hardening

- reduce terms with empty `sources`
- improve `see_also` coverage for operational terms
- refine evidence artifacts for revocation-sensitive and decision-plane terms
- review terms flagged by `possibly_circular_definition`
- add stronger source attribution for high-impact governance concepts

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
