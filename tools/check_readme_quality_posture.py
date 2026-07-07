#!/usr/bin/env python3
"""Fail when README quality posture drifts from generated report values."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "generated" / "json" / "governance-quality-report.json"
README = ROOT / "README.md"


def main() -> int:
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    readme = README.read_text(encoding="utf-8")
    expected_values = [
        str(report["term_count"]),
        f"{report['quality_score']:.1f} / 100",
        str(report["summary"]["issue_count"]),
        str(report["summary"]["coverage"]["with_sources"]),
        str(report["summary"]["coverage"]["with_see_also"]),
        str(report["summary"]["coverage"]["with_evidence"]),
        str(report["summary"]["coverage"]["revocation_supported"]),
    ]
    missing = [value for value in expected_values if value not in readme]
    if missing:
        print("README quality posture is out of sync with generated quality report.")
        for value in missing:
            print(f"Missing expected value: {value}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
