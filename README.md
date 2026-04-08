# ToIP Main Glossary

The ToIP Main Glossary is the canonical terminology baseline for decentralized digital trust infrastructure work across Trust over IP working groups, adjacent specifications, and ecosystem implementations.

This repository now includes a **governance-oriented improvement set** designed to make the glossary easier to maintain, easier to implement against, and easier to evolve toward machine-verifiable usage.

## What this repository contains

- `spec/` — source markdown for glossary terms and specification content
- `docs/` — published site output plus maintainership guidance and governance-oriented improvement notes
- `schemas/` — machine-readable schema artifacts for glossary extension work
- `examples/` — example governance-aware term profiles
- `.github/workflows/` — publication and rendering workflows

## Improvement set added in this archive

This archive introduces a practical first pass at the improvements identified in the glossary review:

1. **Developer-facing repository documentation**
   - clearer repository purpose
   - clearer structure and editing workflow
   - explicit next-step areas for glossary quality improvement

2. **Governance-aware extension model**
   - machine-readable schema for extended glossary metadata
   - example term profiles for authority, delegation, issuer, verifier, policy, revocation, and trust registry

3. **Term quality uplift for core governance terms**
   - tighter definitions for authority, delegation, issuer, verifier, policy, revocation, and trust registry
   - stronger emphasis on scope, enforcement, and lifecycle semantics

4. **Maintainer guidance**
   - quality rubric for future glossary terms
   - roadmap for iterative adoption without disrupting the current publication model

## Build and publish

This repository uses `spec-up-t`.

### Local workflow

```bash
npm install
npm run render
```

Primary source configuration lives in `specs.json`.

## Recommended next implementation increments

- add machine-readable metadata to more high-value terms
- publish JSON exports for governance-aware term profiles
- align glossary terms with adjacent ToIP glossaries through crosswalk files
- add CI validation for term completeness and schema conformance
- introduce controlled versioning for machine-readable term profiles

## Governance-oriented design intent

The glossary already serves as an important human-readable terminology anchor. The additions in this archive are intended to move the repository toward:

- clearer **authority and scope** semantics
- more explicit **delegation and revocation** semantics
- stronger **evidence and auditability** pathways
- better support for future **machine-verifiable** usage

## Notes

The generated website in `docs/` remains the primary publication artifact. The new markdown and schema files provide a maintainable pathway for future publication and CI work without forcing an immediate structural rewrite of the existing glossary pipeline.
