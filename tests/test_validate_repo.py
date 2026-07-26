from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.validate_repo import extract_required_fields, normalize_field, run_checks


class ValidatorUnitTests(unittest.TestCase):
    def test_normalize_field_is_stable(self) -> None:
        self.assertEqual(
            normalize_field("Events / triggers"),
            normalize_field("Events & Triggers"),
        )

    def test_extract_required_fields_stops_at_next_section(self) -> None:
        text = """# Artifact

## Required Fields

- First field
- Second field

## Optional Fields

- Optional field
"""
        self.assertEqual(extract_required_fields(text), ["First field", "Second field"])

    def test_missing_contract_fails_cleanly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(
                run_checks(Path(directory)),
                ["missing contracts/artifacts.json"],
            )


class RepositoryContractTests(unittest.TestCase):
    def test_repository_contract(self) -> None:
        root = Path(__file__).resolve().parents[1]
        issues = run_checks(root)
        self.assertEqual([], issues, "\n".join(issues))


if __name__ == "__main__":
    unittest.main()
