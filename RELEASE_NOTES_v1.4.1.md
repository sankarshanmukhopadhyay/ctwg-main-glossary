# CTWG Main Glossary v1.4.1

## Publication Navigation and Term-Casing Integrity

This maintenance release fixes duplicated governance entries in the rendered GitHub Pages table of contents and restores a single authoritative publication path. It also normalizes all glossary display terms to the repository-wide lowercase convention and adds automated controls to prevent navigation duplication and casing drift from recurring.

## Fixed

- Removed the mirrored `docs/governance/` tree that caused Just the Docs to publish governance pages twice.
- Added `docs/governance/` to Jekyll exclusions as a defensive publication boundary.
- Corrected the configured GitHub Pages origin to `https://sankarshanmukhopadhyay.github.io`.
- Corrected repository, workflow badge, citation, and artifact-download references for the maintained fork.
- Normalized the 36 cross-repository terms introduced in v1.4.0 from title or sentence capitalization to lowercase display casing.

## Added

- Added a source validation rule requiring each authoritative `term` value to use lowercase display casing.
- Added `tools/validate_jekyll_navigation.py` to detect duplicate publishable navigation identities using the combination of page `title` and `parent`.
- Integrated navigation uniqueness validation into both the glossary-validation and GitHub Pages workflows.

## Generated artifacts

The release regenerates and synchronizes:

- 599 Jekyll glossary term pages;
- JSON and JSON-LD glossary bundles;
- governance inventories and overlays;
- Markdown exports;
- artifact manifests and build summaries;
- alphabetic term indexes; and
- the governance quality report.

## Assurance and validation evidence

- 599 structured glossary term files validated successfully.
- 1,155 aliases checked for collisions.
- 80 structured source citations checked.
- 599 terms confirmed to use lowercase display casing.
- 42 unique publishable Jekyll navigation identities validated with no duplicates.
- Governance quality score remains `100.0 / 100` with `0` findings.

## Upgrade notes

No schema or downstream artifact contract changes are introduced. Consumers may upgrade from v1.4.0 without migration. Implementations that display the authoritative `term` value should expect the 36 v1.4.0 additions to now appear in lowercase, consistent with the rest of the glossary.
