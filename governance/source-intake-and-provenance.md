---
title: "Source Intake and Provenance"
parent: Governance Documentation
nav_order: 7
---

# Source Intake and Provenance

## Purpose

TIG is an independent concept system that can learn from many external vocabularies without treating any one source repository as its governing upstream.

## Source intake lifecycle

External material moves through:

**observed → evaluated → normalized → provenance recorded → reviewed → incorporated**

There is no automatic semantic synchronization.

## Provenance classifications

- `adopted` — concept and definition are intentionally carried from a named source with attribution.
- `adapted` — a source concept materially informed the TIG concept, but wording, scope, structure, or governance semantics were changed.
- `locally_defined` — the TIG project defines the concept for its own scope, while still citing relevant evidence where available.
- `mapped` — the concept remains independently defined and is linked semantically to an external concept.

## ToIP lineage

The Trust over IP Main Glossary is a major historical source corpus. v2 does not treat it as an authoritative upstream repository. Existing ToIP-derived entries are classified as `adapted` during migration unless a later source review establishes a more precise classification.

## Licensing rule

Open availability does not by itself authorize unrestricted textual reuse. Before importing definition text, maintainers must verify the applicable license and attribution conditions.

Where licensing is unclear, prefer:

1. independent wording;
2. a citation to the source concept; and
3. a semantic mapping rather than copied text.

## Source-corpus review

Candidate corpora may include W3C, IETF, OpenID, DCMI, Schema.org, SPDX, CNCF, OpenSSF, C2PA, DIF, EUDI, ToIP, DTG, CAWG, and other relevant open standards or projects.

Admission is based on semantic relevance, not merely lexical overlap.
