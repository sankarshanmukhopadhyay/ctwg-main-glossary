# Contributing

Thank you for contributing to the ToIP Main Glossary.

## Contribution model

This repository is maintained as an executable publication system. A high-quality contribution updates the authoritative source, regenerates dependent outputs, and leaves documentation aligned with the new state of the repository.

## Authoritative and generated paths

### Authoritative

- `glossary/terms/`
- `governance/`
- `tools/`
- selected top-level documentation files such as `README.md` and `artifacts.md`

### Generated

- `_terms/`
- `generated/json/`
- `generated/markdown/`
- `terms-index.md`
- `terms/*/index.md`
- generated governance overlay files under `glossary/overlays/governance/`

Do not hand-edit generated files unless you are also changing the generator and regenerating the output in the same change set.

## Required local workflow

Run the full maintainer sequence before opening a pull request.

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_jekyll_site.py
```

For site preview work:

```bash
bundle install
bundle exec jekyll serve
```

## Pull request expectations

Every pull request should answer the following:

- What source files changed?
- What generated outputs changed as a result?
- What validation was run?
- What documentation changed?
- Are the generated artifacts fully in sync with source?

## Review checklist

- term metadata is structurally valid
- slugs and filenames remain deterministic
- aliases do not create collisions
- governance fields are internally coherent
- generated inventories and indexes were rebuilt
- documentation remains current

## Commit discipline

Prefer substantive commits that keep source, generated output, and documentation synchronized. Avoid splitting generator changes from regenerated artifacts unless there is a strong reason to do so.
