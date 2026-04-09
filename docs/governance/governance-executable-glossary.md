---
title: "Governance-Executable Glossary"
parent: Governance Documentation
nav_order: 10
---

# Governance-Executable Glossary

This repository maintains a parallel machine-readable representation of the glossary that can be validated, regenerated, published, and inspected as executable governance infrastructure.

## Current operating posture

- all glossary terms under `glossary/terms/` are validated before generation
- Jekyll term pages are generated from the YAML term layer
- JSON, JSON-LD, markdown bundle, and inventory artifacts are generated under `generated/`
- governance overlay files are refreshed from the same authoritative source layer

## What the executable layer captures

Each term can carry structured semantics for:

- authority scope
- delegation mode
- revocation support
- lifecycle states
- execution role
- control-plane role
- evidence expectations
- auditability
- decision points
- accountable entity
- crosswalk references

## Assurance value

The executable layer does not turn the glossary into a normative standard by itself. It does, however, make key governance semantics inspectable, testable, and reusable by downstream tooling.

## Generated outputs

- `generated/json/governance-executable-glossary.json`
- `generated/json/governance-executable-glossary.jsonld`
- `generated/json/governance-executable-glossary.catalog.json`
- `generated/json/governance-inventory.json`
- `generated/markdown/governance-executable-glossary.md`
- `generated/markdown/governance-inventory.md`
