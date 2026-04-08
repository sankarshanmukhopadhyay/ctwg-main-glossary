# Editing the Glossary

This repository is now published as a **Jekyll + Just the Docs + GitHub Pages** site.

The governance-executable YAML files under `glossary/terms/` are the operational source for generated glossary pages and machine-readable bundles.

## Maintenance workflow

1. Update the relevant glossary term in `glossary/terms/`
2. Run validation
3. Regenerate machine-readable bundles
4. Regenerate Jekyll markdown pages
5. Preview locally with Jekyll if needed

## Commands

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_jekyll_site.py
bundle install
bundle exec jekyll serve
```

## Publication

GitHub Pages is built through `.github/workflows/pages.yml`.

The workflow validates the glossary, rebuilds JSON and markdown artifacts, generates the Jekyll pages from the governance-executable source layer, and then deploys the site.

## Source model

- `glossary/terms/` remains the source for structured term semantics
- `_terms/` is generated and should not be edited manually unless you are intentionally applying an emergency fix
- `governance/` contains rendered governance documentation pages
- `generated/` contains consumable machine-readable outputs

## Review expectations

Any pull request that changes glossary semantics should update the relevant YAML term files and regenerate outputs so reviewers can inspect both the source semantics and the rendered publication changes.
