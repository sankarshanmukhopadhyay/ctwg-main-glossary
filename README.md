# ToIP Main Glossary

The ToIP Main Glossary is a **Governance-Executable Glossary** published as a **GitHub Pages** documentation site using **Jekyll** and **Just the Docs**.

This repository now treats the structured glossary layer under `glossary/terms/` as the operational source for generated site pages and machine-readable governance artifacts.

## Operating model

- `glossary/terms/` — governance-executable YAML term artifacts
- `glossary/overlays/` — governance, assurance, and mapping overlays
- `generated/json/` — machine-readable glossary bundles
- `generated/markdown/` — generated markdown bundle artifacts
- `_terms/` — generated Jekyll pages for individual terms
- `governance/` — governance documentation rendered by GitHub Pages
- `tools/` — build and validation utilities
- `.github/workflows/pages.yml` — GitHub Pages publication workflow

## Publication architecture

The repository no longer depends on the previous Spec-Up publication stack.

Instead, publication now follows a simpler and more maintainable path:

1. validate governance-executable term artifacts
2. regenerate glossary JSON, JSON-LD, and markdown bundles
3. generate Jekyll markdown pages from the structured source layer
4. publish the site through GitHub Pages with Just the Docs

## Local maintenance workflow

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_jekyll_site.py
bundle install
bundle exec jekyll serve
```

## Generated site outputs

- landing page at `index.md`
- governance documentation under `governance/`
- glossary term pages under `_terms/`
- artifact download references under `artifacts.md`

## Governance-executable semantics

Each glossary term can express:

- authority scope
- delegation mode
- revocation support
- lifecycle states
- execution role
- control-plane role
- evidence artifacts
- assurance level hint
- auditability
- decision points
- accountable entity
- optional crosswalk references

## Contribution guidance

1. Update the relevant YAML file in `glossary/terms/`
2. Run validation and rebuild scripts
3. Review regenerated pages and artifact indexes
4. Submit the change with documentation updates when semantics changed

## Design intent

The objective is to make glossary content easier to publish, easier to maintain, and easier to consume as machine-readable governance infrastructure. Markdown remains first-class for readers. Structured term artifacts remain first-class for assurance, interoperability, and automation workflows.
