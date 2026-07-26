from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class StageContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.stage_registry = json.loads((ROOT / "contracts" / "stages.json").read_text(encoding="utf-8"))
        cls.artifact_registry = json.loads((ROOT / "contracts" / "artifacts.json").read_text(encoding="utf-8"))
        cls.stages = cls.stage_registry["stages"]
        cls.skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.readme_text = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_stage_registry_is_sequential_and_unique(self) -> None:
        numbers = [stage["number"] for stage in self.stages]
        names = [stage["name"] for stage in self.stages]
        ids = [stage["id"] for stage in self.stages]
        self.assertEqual(list(range(1, len(self.stages) + 1)), numbers)
        self.assertEqual(len(names), len(set(names)), "stage names must be unique")
        self.assertEqual(len(ids), len(set(ids)), "stage IDs must be unique")

    def test_stage_exit_gates_exist(self) -> None:
        gate_ids = {gate["id"] for gate in self.artifact_registry["gates"]}
        unknown = [
            stage["exit_gate"]
            for stage in self.stages
            if stage["exit_gate"] is not None and stage["exit_gate"] not in gate_ids
        ]
        self.assertEqual([], unknown, f"stage registry references unknown gates: {unknown}")

    def test_artifact_and_gate_stage_references_are_valid(self) -> None:
        valid_numbers = {stage["number"] for stage in self.stages}
        invalid: list[str] = []

        def check(label: str, value: str) -> None:
            referenced = {int(number) for number in re.findall(r"\d+", value)}
            if not referenced and "post-delivery" not in value:
                invalid.append(f"{label}: {value}")
                return
            unknown = referenced - valid_numbers
            if unknown:
                invalid.append(f"{label}: {value} -> unknown {sorted(unknown)}")

        for artifact_id, artifact in self.artifact_registry["artifacts"].items():
            check(f"artifact {artifact_id}", str(artifact["stage"]))
        for gate in self.artifact_registry["gates"]:
            check(f"gate {gate['id']}", str(gate["after_stage"]))

        self.assertEqual([], invalid, f"invalid stage references: {invalid}")

    def test_root_skill_stage_headings_match_registry(self) -> None:
        missing = [
            f"## Stage {stage['number']}: {stage['name']}"
            for stage in self.stages
            if f"## Stage {stage['number']}: {stage['name']}" not in self.skill_text
        ]
        self.assertEqual([], missing, f"root skill stage headings drifted from the registry: {missing}")

    def test_readme_stage_rows_match_registry(self) -> None:
        missing = [
            f"| {stage['number']}. {stage['name']} |"
            for stage in self.stages
            if f"| {stage['number']}. {stage['name']} |" not in self.readme_text
        ]
        self.assertEqual([], missing, f"README stage rows drifted from the registry: {missing}")


if __name__ == "__main__":
    unittest.main()
