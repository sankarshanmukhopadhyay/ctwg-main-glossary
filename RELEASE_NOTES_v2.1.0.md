---
title: v2.1.0 Release Notes
parent: Project
nav_order: 1
permalink: /release-notes-v2-1-0/
---

# Trust Infrastructure Glossary v2.1.0

**Release date:** 20 August 2026

v2.1.0 is the **portfolio vocabulary foundations** release. It expands TIG from 612 to 617 governed concepts and establishes missing semantic primitives that recur across the broader trust-infrastructure portfolio.

## Added

Five foundational concepts are now first-class TIG source concepts:

- `accountability`
- `assurance`
- `decision`
- `effect`
- `evidence`

Each concept has a stable `urn:tig:concept:*` identifier, independently authored definition, plain-language explanation, provenance, governance metadata, assurance metadata, control-plane semantics, and semantic relationships.

The release also adds `governance/portfolio-vocabulary-gap-analysis.md`, a governed inventory of reusable terminology observed across TSMM, TIS, GAAM, RAHP, ARPA, ONDTF, PolicyMesh, TRQP and DTG ZKP work that is not yet represented as a first-class TIG concept.

## Why these concepts come first

The five additions are dependencies for higher-order vocabulary already used across the portfolio. Defining them first allows later additions such as `authority boundary`, `decision receipt`, `evidence bundle`, `assurance gap`, `scope attenuation`, `revocation propagation`, `semantic drift`, and `remediation manifest` to reference stable TIG concept identifiers instead of carrying repository-local definitions.

## Generated publication

All governed publication artifacts were regenerated from `glossary/terms/*.yaml`, including:

- canonical JSON and catalog outputs;
- JSON-LD and SKOS Turtle;
- governance inventories;
- quality reports;
- Jekyll concept pages;
- alphabetical indexes and term indexes.

## Validation and assurance evidence

The regenerated corpus reports:

- **617 concepts**;
- **617 concepts with evidence metadata**;
- **617 concepts with source coverage**;
- **617 concepts with cross-reference coverage**;
- **100.0 / 100 quality score**;
- **0 quality findings** under the repository's current executable quality rules.

The new concepts remain at editorial status `proposed`. Release publication establishes stable concept identity and makes them available for portfolio use; it does not claim that editorial review is complete.

## Compatibility

This is an additive minor release. The v2 concept schema and existing concept identifiers remain unchanged. Consumers of v2.0.0 artifacts can adopt v2.1.0 without migration, while gaining five additional concept records and updated generated bundles.

## Next vocabulary tranche

The next expansion should prioritize reusable cross-repository governance and assurance primitives, especially:

- authority boundary;
- decision receipt;
- evidence bundle;
- assurance gap;
- assurance proposition;
- control credit;
- scope attenuation;
- revocation propagation;
- semantic drift; and
- remediation manifest.
