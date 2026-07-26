from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class StageContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = json.loads((ROOT / "contracts" / "artifacts.json").read_text(encoding="utf-8"))
        cls.skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.readme_text = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_root_skill_stage_headings_match_registry(self) -> None:
        missing = [
            f"## Stage {stage['number']}: {stage['name']}"
            for stage in self.registry["stages"]
            if f"## Stage {stage['number']}: {stage['name']}" not in self.skill_text
        ]
        self.assertEqual([], missing, f"root skill stage headings drifted from the registry: {missing}")

    def test_readme_stage_rows_match_registry(self) -> None:
        missing = [
            f"| {stage['number']}. {stage['name']} |"
            for stage in self.registry["stages"]
            if f"| {stage['number']}. {stage['name']} |" not in self.readme_text
        ]
        self.assertEqual([], missing, f"README stage rows drifted from the registry: {missing}")


if __name__ == "__main__":
    unittest.main()
