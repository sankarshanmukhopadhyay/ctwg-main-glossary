---
title: v2.0.0 Release Notes
parent: Project
nav_order: 2
permalink: /release-notes-v2-0-0/
---

# Trust Infrastructure Glossary v2.0.0

**Release date:** 17 August 2026

v2.0.0 is the independence and semantic-model release. It establishes the former ToIP-derived glossary fork as the **Trust Infrastructure Glossary (TIG)**: an independently governed, governance-executable concept system for digital trust infrastructure.

## Reader-first GitHub Pages information architecture

The v2 publication site is reorganized around four reader tasks: **Explore Concepts**, **Use TIG**, **Govern TIG**, and **Project**. Alphabetical browsing and topic browsing now sit under a single exploration hierarchy; profiles, artifacts, and downstream integration sit together; governance material is grouped into semantic authoring, assurance/quality, and operations/evolution; and project lineage, migration, releases, roadmap, and contribution guidance are separated from glossary governance.

Generated concept pages now lead with plain-English meaning, formal definition, relevance, names, and relationships. Provenance and stable identity follow, while detailed governance, assurance, control-plane, evidence, and crosswalk metadata is progressively disclosed for readers who need it.


## Breaking changes

- project identity changes from ToIP Main Glossary fork to Trust Infrastructure Glossary
- ToIP is no longer treated as a governing upstream repository
- concept identity is now explicit through stable `urn:tig:concept:*` identifiers
- `designations` become the authoritative label model; `term` and `aliases` remain compatibility fields
- provenance classification and editorial maturity are first-class fields
- semantic relations and cross-vocabulary mappings are represented explicitly
- canonical machine-readable artifact names move to `trust-infrastructure-glossary.*`

## Independence and provenance

The release removes one-way upstream synchronization automation and replaces it with source-intake governance. Historical ToIP-derived concepts retain citations and are migrated with explicit `adapted` provenance unless later reviewed into a more precise classification.

The release does not erase upstream authorship, historical source files, or applicable licensing obligations.

## Semantic model

Every concept now carries:

- `schema_version: "2.0"`
- stable `concept_id`
- language-tagged designations
- editorial status and review metadata
- provenance classification and lineage note
- optional SKOS-aligned broader/narrower/related relations
- cross-vocabulary exact/close/broad/narrow/related mapping slots
- existing governance, assurance, evidence, lifecycle, and control-plane metadata

## Open-vocabulary practices adopted

v2 incorporates design practices informed by CNCF, OpenSSF, Glossarist, W3C SKOS, DCMI, Schema.org, SPDX, MDN, and the Inclusive Naming Initiative. These influences affect the architecture and editorial model; external definition text is not bulk-imported.

## Machine-readable publication

New canonical artifacts include:

- `generated/json/trust-infrastructure-glossary.json`
- `generated/json/trust-infrastructure-glossary.catalog.json`
- `generated/json/trust-infrastructure-glossary.jsonld`
- `generated/rdf/trust-infrastructure-glossary.ttl`

Legacy v1 filenames remain generated during the migration window.

## Vocabulary profiles

v2 introduces validated selection profiles for:

- core trust infrastructure
- agent governance
- assurance and conformance

Profiles reference stable concept IDs and do not redefine concepts.

## Repository cleanup

Obsolete Spec-Up runtime scaffolding has been removed. The historical `spec/terms-definitions/` corpus is retained as provenance evidence and remains addressable by migrated source references.

## Validation

The release validates:

- 612 concept artifacts
- 1,164 aliases for collisions
- 93 structured source citations
- 3 vocabulary profiles
- schema / controlled-vocabulary alignment
- generated artifact reproducibility
- governance quality reporting

The generated governance quality report remains at 100.0/100 with zero findings under the checks currently implemented.

## Migration

See `MIGRATION_v2.md` for consumer migration guidance.
