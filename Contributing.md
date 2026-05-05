# Contributing

Thank you for improving the ToIP Main Glossary.

This repository is operated as a governance-executable publication system. Contributions should keep the authoritative source layer, generated artifacts, validation logic, and documentation aligned.

## Before opening a pull request

Install dependencies:

```bash
pip install pyyaml jsonschema
```

Run:

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_quality_report.py
python tools/build_jekyll_site.py
```

If generated files changed, include those generated diffs in the same pull request.

## Adding or editing a term

1. Edit the YAML artifact under `glossary/terms/`.
2. Keep the file slug aligned with the `term` value.
3. Use `examples/governance-term/` as the reference shape.
4. Use controlled values from `schemas/governance-vocabularies.yaml`.
5. Add sources and `see_also` references where they improve evidence and interpretation.
6. Pair decision points with enforcement points.
7. Add evidence artifacts that can be inspected by downstream governance or assurance tooling.

## Pull request expectations

A good pull request explains:

- what terms or controls changed;
- whether schema or vocabulary values changed;
- what generated artifacts changed;
- whether the quality report improved or intentionally changed; and
- how publication compatibility was preserved.

## Generated files

Do not manually edit generated files. Regenerate them from source using the tools above.
