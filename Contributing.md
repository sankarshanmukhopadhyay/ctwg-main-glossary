# Contributing

Thank you for improving the Trust Infrastructure Glossary.

TIG is a governance-executable concept system. Contributions must keep concept identity, provenance, generated artifacts, validation logic, and documentation aligned.

## Before opening a pull request

```bash
pip install -r requirements.txt
python tools/validate_governance_glossary.py
python tools/validate_profiles.py
python tools/build_governance_glossary.py
python tools/build_quality_report.py
python tools/build_jekyll_site.py
```

Include generated diffs when source changes affect generated artifacts.

## Adding or editing a concept

1. Edit the YAML artifact under `glossary/terms/`.
2. Keep `concept_id` stable after publication.
3. Keep exactly one English `preferred` designation aligned with the compatibility `term` field.
4. Use `alternative`, `deprecated`, or `discouraged` for other designations.
5. Preserve or improve source provenance.
6. Classify provenance as `adopted`, `adapted`, `locally_defined`, or `mapped`.
7. Use semantic relations and cross-vocabulary mappings conservatively.
8. Add a simple-English definition when feasible without weakening the formal meaning.
9. Use controlled values from `schemas/governance-vocabularies.yaml`.
10. Regenerate and review all outputs.

## Source reuse

Do not assume that public availability means definition text can be copied. Check source licensing and attribution requirements. When in doubt, independently define the TIG concept, cite the external source, and create a semantic mapping.

## Pull request expectations

Explain:

- which concepts changed;
- whether concept identity or designations changed;
- provenance and licensing implications;
- any new semantic relations or mappings;
- schema/profile changes;
- generated-artifact changes; and
- quality-report effects.

Generated files must not be edited manually.
