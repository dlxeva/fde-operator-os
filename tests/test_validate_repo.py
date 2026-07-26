from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.validate_repo import (
    _validate_case_manifests,
    extract_required_fields,
    normalize_field,
    run_checks,
)


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

    def test_go_gate_requires_all_declared_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            contract = self._write_case_fixture(
                root,
                {
                    "$schema": "../../contracts/case-manifest.schema.json",
                    "case_id": "missing-gate-artifact",
                    "synthetic": True,
                    "artifacts": {},
                    "gates": {"G0": "go"},
                },
            )

            issues = _validate_case_manifests(root, contract)

            self.assertTrue(
                any(
                    "gate 'G0' is go but missing required artifacts: mission-brief"
                    in issue
                    for issue in issues
                ),
                "\n".join(issues),
            )

    def test_malformed_manifest_reports_types_without_crashing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            contract = self._write_case_fixture(
                root,
                {
                    "$schema": 7,
                    "case_id": "",
                    "synthetic": "yes",
                    "artifacts": [],
                    "gates": [],
                    "notes": "not-an-array",
                },
            )

            issues = _validate_case_manifests(root, contract)

            self.assertTrue(any("'$schema' must be a non-empty string" in issue for issue in issues))
            self.assertTrue(any("'synthetic' must be a boolean" in issue for issue in issues))
            self.assertTrue(any("'artifacts' must be an object" in issue for issue in issues))
            self.assertTrue(any("'gates' must be an object" in issue for issue in issues))
            self.assertTrue(any(":notes: must be an array" in issue for issue in issues))

    @staticmethod
    def _write_case_fixture(root: Path, manifest: dict[str, object]) -> dict[str, object]:
        contracts_dir = root / "contracts"
        contracts_dir.mkdir(parents=True)
        (contracts_dir / "case-manifest.schema.json").write_text(
            "{}\n",
            encoding="utf-8",
        )

        case_dir = root / "examples" / "case"
        case_dir.mkdir(parents=True)
        (case_dir / "case-manifest.json").write_text(
            json.dumps(manifest),
            encoding="utf-8",
        )

        return {
            "artifacts": {
                "mission-brief": {
                    "template_markers": [],
                }
            },
            "gates": [
                {
                    "id": "G0",
                    "required_artifacts": ["mission-brief"],
                }
            ],
            "case_manifest_schema": "contracts/case-manifest.schema.json",
        }


class RepositoryContractTests(unittest.TestCase):
    def test_repository_contract(self) -> None:
        root = Path(__file__).resolve().parents[1]
        issues = run_checks(root)
        self.assertEqual([], issues, "\n".join(issues))


if __name__ == "__main__":
    unittest.main()
