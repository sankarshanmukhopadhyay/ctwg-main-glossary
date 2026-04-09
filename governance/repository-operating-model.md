---
title: "Repository Operating Model"
parent: Governance Documentation
nav_order: 5
---

# Repository Operating Model

## Purpose

This repository is operated as a controlled publishing system for glossary content with executable governance semantics.

The key objective is to keep three things aligned:

1. **authority** over what may be changed
2. **enforcement** of deterministic generation and publication integrity
3. **evidence** that generated outputs match the authoritative source layer

## Source and generated layers

### Authoritative source layer

- `glossary/terms/`
- `governance/`
- `tools/`
- top-level maintainer documentation

### Generated publication layer

- `_terms/`
- `generated/json/`
- `generated/markdown/`
- `terms-index.md`
- `terms/*/index.md`
- generated governance overlays

## Maintainer rules

### Rule 1: edit source, not renderings

The expected edit path is through `glossary/terms/` and the repository documentation files. Generated pages and bundles are outputs, not editorial surfaces.

### Rule 2: generation must be reproducible

All generated files committed to the repository must be reproducible by the build scripts in `tools/`.

### Rule 3: CI must detect drift

Repository workflows are expected to fail if validation fails or if generated outputs differ from what the build scripts produce.

### Rule 4: documentation is part of the control plane

When the operating model changes, the maintainer documentation must be updated in the same change set.

## Assurance outcomes

The operating model is designed to produce evidence for:

- term-level structural validity
- alias and slug collision detection
- bundle and inventory reproducibility
- publication-readiness of generated pages
- auditability of change effects through committed generated artifacts

## Release posture

A release-quality change should include:

- authoritative source updates where applicable
- regenerated artifacts
- refreshed documentation
- validation evidence noted in the commit or release narrative
