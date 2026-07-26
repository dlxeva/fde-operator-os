#!/usr/bin/env python3
"""Validate the repository's artifact contract, templates, examples, and links.

The validator intentionally uses only the Python standard library so it can run
in local agent environments and GitHub Actions without dependency setup.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_TEMPLATE_SECTIONS = (
    "Use",
    "Required Fields",
    "Typical Anti-Pattern",
    "Completion Standard",
    "Template",
)
CASE_MANIFEST_KEYS = {
    "$schema",
    "case_id",
    "title",
    "synthetic",
    "artifacts",
    "gates",
    "notes",
}
ALLOWED_GATE_STATUSES = {"pass", "conditional", "fail", "hold", "not-run"}
FIELD_RE = re.compile(r"^\s*-\s+(.+?)\s*$")
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REPOSITORY_PATH_RE = re.compile(
    r"`((?:assets|references|skills|aliases|contracts|examples|tools|tests|agents)/[^`\s]*)`"
)


def normalize_field(value: str) -> str:
    """Normalize field labels while preserving meaningful words."""

    value = value.strip().lower().replace("&", " ")
    value = re.sub(r"[`*_]", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def extract_section(text: str, heading: str) -> str | None:
    """Return a level-two Markdown section without its heading."""

    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group("body").strip() if match else None


def extract_required_fields(text: str) -> list[str]:
    """Extract bullets from a template's Required Fields section."""

    section = extract_section(text, "Required Fields")
    if section is None:
        return []
    fields: list[str] = []
    for line in section.splitlines():
        match = FIELD_RE.match(line)
        if match:
            fields.append(match.group(1).strip())
    return fields


def load_contract(root: Path = ROOT) -> dict[str, Any]:
    path = root / "contracts" / "artifacts.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _is_placeholder_path(value: str) -> bool:
    return any(token in value for token in ("<", ">", "{", "}", "*", "$"))


def _validate_string_list(value: Any, label: str, *, allow_empty: bool = False) -> list[str]:
    issues: list[str] = []
    if not isinstance(value, list):
        return [f"{label}: must be an array"]
    if not value and not allow_empty:
        issues.append(f"{label}: must not be empty")
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            issues.append(f"{label}[{index}]: must be a non-empty string")
    return issues


def _validate_contract_shape(contract: Any) -> list[str]:
    issues: list[str] = []
    if not isinstance(contract, dict):
        return ["contracts/artifacts.json: root must be an object"]

    for key in (
        "contract_version",
        "description",
        "artifacts",
        "source_of_truth",
        "gates",
        "case_manifest_schema",
    ):
        if key not in contract:
            issues.append(f"contracts/artifacts.json: missing key '{key}'")

    for key in ("contract_version", "description", "case_manifest_schema"):
        value = contract.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"contracts/artifacts.json: '{key}' must be a non-empty string")

    artifacts = contract.get("artifacts")
    if not isinstance(artifacts, dict) or not artifacts:
        issues.append("contracts/artifacts.json: 'artifacts' must be a non-empty object")
        return issues

    for artifact_id, artifact in artifacts.items():
        if not isinstance(artifact_id, str) or not artifact_id.strip():
            issues.append("contract: artifact IDs must be non-empty strings")
            continue
        if not isinstance(artifact, dict):
            issues.append(f"contract:{artifact_id}: artifact definition must be an object")
            continue
        for key in (
            "title",
            "stage",
            "template",
            "required_fields",
            "template_markers",
            "strict_examples",
        ):
            if key not in artifact:
                issues.append(f"contract:{artifact_id}: missing key '{key}'")

        for key in ("title", "stage", "template"):
            value = artifact.get(key)
            if not isinstance(value, str) or not value.strip():
                issues.append(
                    f"contract:{artifact_id}: '{key}' must be a non-empty string"
                )

        required_fields = artifact.get("required_fields")
        issues.extend(
            _validate_string_list(
                required_fields,
                f"contract:{artifact_id}:required_fields",
            )
        )
        if isinstance(required_fields, list):
            normalized = [
                normalize_field(item)
                for item in required_fields
                if isinstance(item, str) and item.strip()
            ]
            if len(normalized) != len(set(normalized)):
                issues.append(
                    f"contract:{artifact_id}: duplicate required fields after normalization"
                )

        issues.extend(
            _validate_string_list(
                artifact.get("template_markers"),
                f"contract:{artifact_id}:template_markers",
            )
        )

        strict_examples = artifact.get("strict_examples")
        if not isinstance(strict_examples, list):
            issues.append(f"contract:{artifact_id}:strict_examples: must be an array")
        else:
            for index, example in enumerate(strict_examples):
                label = f"contract:{artifact_id}:strict_examples[{index}]"
                if not isinstance(example, dict):
                    issues.append(f"{label}: must be an object")
                    continue
                path = example.get("path")
                if not isinstance(path, str) or not path.strip():
                    issues.append(f"{label}: 'path' must be a non-empty string")
                issues.extend(
                    _validate_string_list(
                        example.get("markers"),
                        f"{label}:markers",
                    )
                )

    aliases = contract.get("aliases", [])
    if not isinstance(aliases, list):
        issues.append("contracts/artifacts.json: 'aliases' must be an array")
    else:
        seen_aliases: set[str] = set()
        for index, alias in enumerate(aliases):
            label = f"alias[{index}]"
            if not isinstance(alias, dict):
                issues.append(f"{label}: must be an object")
                continue
            path = alias.get("path")
            canonical = alias.get("canonical")
            for key, value in (("path", path), ("canonical", canonical)):
                if not isinstance(value, str) or not value.strip():
                    issues.append(f"{label}: '{key}' must be a non-empty string")
            if isinstance(path, str) and path:
                if path in seen_aliases:
                    issues.append(f"{label}: duplicate alias path '{path}'")
                seen_aliases.add(path)

    sources = contract.get("source_of_truth")
    if not isinstance(sources, dict) or not sources:
        issues.append("contracts/artifacts.json: 'source_of_truth' must be a non-empty object")
    else:
        for name, source in sources.items():
            if not isinstance(source, dict):
                issues.append(f"source_of_truth:{name}: must be an object")
                continue
            artifact_id = source.get("artifact")
            field = source.get("field")
            if not isinstance(artifact_id, str) or not artifact_id:
                issues.append(
                    f"source_of_truth:{name}: 'artifact' must be a non-empty string"
                )
                continue
            if not isinstance(field, str) or not field:
                issues.append(
                    f"source_of_truth:{name}: 'field' must be a non-empty string"
                )
                continue
            artifact = artifacts.get(artifact_id)
            if artifact is None:
                issues.append(f"source_of_truth:{name}: unknown artifact '{artifact_id}'")
                continue
            required_fields = artifact.get("required_fields", [])
            if isinstance(required_fields, list) and normalize_field(field) not in {
                normalize_field(item)
                for item in required_fields
                if isinstance(item, str)
            }:
                issues.append(
                    f"source_of_truth:{name}: field '{field}' is not required by '{artifact_id}'"
                )

    gates = contract.get("gates")
    if not isinstance(gates, list) or not gates:
        issues.append("contracts/artifacts.json: 'gates' must be a non-empty array")
    else:
        seen_gate_ids: set[str] = set()
        for index, gate in enumerate(gates):
            label = f"gate[{index}]"
            if not isinstance(gate, dict):
                issues.append(f"{label}: must be an object")
                continue
            gate_id = gate.get("id")
            for key in ("id", "name", "after_stage"):
                value = gate.get(key)
                if not isinstance(value, str) or not value.strip():
                    issues.append(f"{label}: '{key}' must be a non-empty string")
            if isinstance(gate_id, str) and gate_id:
                if gate_id in seen_gate_ids:
                    issues.append(f"{label}: duplicate gate ID '{gate_id}'")
                seen_gate_ids.add(gate_id)
            required_artifacts = gate.get("required_artifacts")
            issues.extend(
                _validate_string_list(
                    required_artifacts,
                    f"{label}:required_artifacts",
                )
            )
            if isinstance(required_artifacts, list):
                for artifact_id in required_artifacts:
                    if isinstance(artifact_id, str) and artifact_id not in artifacts:
                        issues.append(
                            f"gate:{gate_id or '<unknown>'}: unknown artifact '{artifact_id}'"
                        )

    return issues


def _validate_artifacts(root: Path, contract: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    for artifact_id, artifact in contract["artifacts"].items():
        template_path = root / artifact["template"]
        if not template_path.is_file():
            issues.append(
                f"artifact:{artifact_id}: missing template '{artifact['template']}'"
            )
            continue

        text = template_path.read_text(encoding="utf-8")
        headings = set(HEADING_RE.findall(text))
        for section in REQUIRED_TEMPLATE_SECTIONS:
            if section not in headings:
                issues.append(
                    f"artifact:{artifact_id}: template missing '## {section}' in {artifact['template']}"
                )

        actual_fields = [normalize_field(item) for item in extract_required_fields(text)]
        expected_fields = [
            normalize_field(item) for item in artifact["required_fields"]
        ]
        if actual_fields != expected_fields:
            issues.append(
                f"artifact:{artifact_id}: required fields drift in {artifact['template']}\n"
                f"  expected: {artifact['required_fields']}\n"
                f"  actual:   {extract_required_fields(text)}"
            )

        for marker in artifact["template_markers"]:
            if marker not in text:
                issues.append(
                    f"artifact:{artifact_id}: template marker missing in {artifact['template']}: {marker}"
                )

        for example in artifact["strict_examples"]:
            example_path = root / example["path"]
            if not example_path.is_file():
                issues.append(
                    f"artifact:{artifact_id}: missing strict example '{example['path']}'"
                )
                continue
            example_text = example_path.read_text(encoding="utf-8")
            for marker in example["markers"]:
                if marker not in example_text:
                    issues.append(
                        f"artifact:{artifact_id}: strict example marker missing in "
                        f"{example['path']}: {marker}"
                    )

    return issues


def _validate_aliases(root: Path, contract: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    for alias in contract.get("aliases", []):
        alias_path = root / alias["path"]
        canonical_path = root / alias["canonical"]
        if not alias_path.is_file():
            issues.append(f"alias: missing alias file '{alias['path']}'")
            continue
        if not canonical_path.is_file():
            issues.append(f"alias: missing canonical file '{alias['canonical']}'")
            continue
        text = alias_path.read_text(encoding="utf-8")
        if alias["canonical"] not in text:
            issues.append(
                f"alias:{alias['path']}: must point to canonical '{alias['canonical']}'"
            )
        if "## Required Fields" in text:
            issues.append(
                f"alias:{alias['path']}: duplicates the artifact contract; keep it as a redirect only"
            )
    return issues


def _validate_case_manifests(root: Path, contract: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    artifact_ids = set(contract["artifacts"])
    gate_requirements = {
        gate["id"]: set(gate["required_artifacts"])
        for gate in contract.get("gates", [])
    }
    gate_ids = set(gate_requirements)

    schema_path = root / contract["case_manifest_schema"]
    if not schema_path.is_file():
        issues.append(
            f"contract: missing case manifest schema '{contract['case_manifest_schema']}'"
        )

    manifest_paths = sorted((root / "examples").glob("**/case-manifest.json"))
    if not manifest_paths:
        issues.append("case-manifest: no example case manifests found")
        return issues

    for manifest_path in manifest_paths:
        relative_manifest = manifest_path.relative_to(root)
        label = f"case-manifest:{relative_manifest}"
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append(f"{label}: invalid JSON: {exc}")
            continue

        if not isinstance(manifest, dict):
            issues.append(f"{label}: root must be an object")
            continue

        unknown_keys = sorted(set(manifest) - CASE_MANIFEST_KEYS)
        for key in unknown_keys:
            issues.append(f"{label}: unknown key '{key}'")

        for key in ("$schema", "case_id", "synthetic", "artifacts", "gates"):
            if key not in manifest:
                issues.append(f"{label}: missing key '{key}'")

        schema_ref = manifest.get("$schema")
        if isinstance(schema_ref, str) and schema_ref:
            resolved_schema = (manifest_path.parent / schema_ref).resolve()
            if resolved_schema != schema_path.resolve():
                issues.append(
                    f"{label}: '$schema' must resolve to '{contract['case_manifest_schema']}'"
                )
        elif "$schema" in manifest:
            issues.append(f"{label}: '$schema' must be a non-empty string")

        case_id = manifest.get("case_id")
        if not isinstance(case_id, str) or not case_id.strip():
            issues.append(f"{label}: 'case_id' must be a non-empty string")

        if "title" in manifest and not isinstance(manifest["title"], str):
            issues.append(f"{label}: 'title' must be a string")

        if not isinstance(manifest.get("synthetic"), bool):
            issues.append(f"{label}: 'synthetic' must be a boolean")

        notes = manifest.get("notes", [])
        issues.extend(
            _validate_string_list(notes, f"{label}:notes", allow_empty=True)
        )

        artifacts = manifest.get("artifacts")
        if not isinstance(artifacts, dict):
            issues.append(f"{label}: 'artifacts' must be an object")
            artifacts = {}
        elif not artifacts:
            issues.append(f"{label}: 'artifacts' must not be empty")

        for artifact_id, relative_path in artifacts.items():
            if artifact_id not in artifact_ids:
                issues.append(f"{label}: unknown artifact '{artifact_id}'")
                continue
            if not isinstance(relative_path, str) or not relative_path.strip():
                issues.append(
                    f"{label}: artifact path for '{artifact_id}' must be a non-empty string"
                )
                continue
            artifact_path = (manifest_path.parent / relative_path).resolve()
            try:
                artifact_path.relative_to(manifest_path.parent.resolve())
            except ValueError:
                issues.append(
                    f"{label}: artifact path escapes the case directory: '{relative_path}'"
                )
                continue
            if not artifact_path.is_file():
                issues.append(
                    f"{label}: missing artifact file '{relative_path}' for '{artifact_id}'"
                )
                continue
            artifact_text = artifact_path.read_text(encoding="utf-8")
            for marker in contract["artifacts"][artifact_id]["template_markers"]:
                if marker not in artifact_text:
                    issues.append(
                        f"{label}: artifact '{relative_path}' is missing contract marker "
                        f"for '{artifact_id}': {marker}"
                    )

        gates = manifest.get("gates")
        if not isinstance(gates, dict):
            issues.append(f"{label}: 'gates' must be an object")
            gates = {}

        missing_gate_ids = sorted(gate_ids - set(gates))
        for gate_id in missing_gate_ids:
            issues.append(f"{label}: missing gate '{gate_id}'")

        for gate_id, status in gates.items():
            if gate_id not in gate_ids:
                issues.append(f"{label}: unknown gate '{gate_id}'")
                continue
            if status not in ALLOWED_GATE_STATUSES:
                issues.append(
                    f"{label}: invalid status '{status}' for '{gate_id}'"
                )
                continue
            if status == "pass":
                missing_artifacts = sorted(
                    gate_requirements[gate_id] - set(artifacts)
                )
                if missing_artifacts:
                    issues.append(
                        f"{label}: gate '{gate_id}' is pass but missing required "
                        f"artifacts: {', '.join(missing_artifacts)}"
                    )

    return issues


def _validate_markdown_links(root: Path) -> list[str]:
    issues: list[str] = []
    for markdown_path in sorted(root.rglob("*.md")):
        if ".git" in markdown_path.parts:
            continue
        text = markdown_path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target or _is_placeholder_path(target):
                continue
            resolved = (markdown_path.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                issues.append(
                    f"link:{markdown_path.relative_to(root)}: target escapes repository: {raw_target}"
                )
                continue
            if not resolved.exists():
                issues.append(
                    f"link:{markdown_path.relative_to(root)}: missing target '{raw_target}'"
                )
    return issues


def _validate_repository_path_references(root: Path) -> list[str]:
    issues: list[str] = []
    for markdown_path in sorted(root.rglob("*.md")):
        if ".git" in markdown_path.parts:
            continue
        text = markdown_path.read_text(encoding="utf-8")
        for referenced in REPOSITORY_PATH_RE.findall(text):
            referenced = referenced.rstrip(".,;:)")
            if not referenced or _is_placeholder_path(referenced):
                continue
            if not (root / referenced).exists():
                issues.append(
                    f"path-ref:{markdown_path.relative_to(root)}: missing repository path '{referenced}'"
                )
    return issues


def run_checks(root: Path = ROOT) -> list[str]:
    """Run all repository checks and return human-readable issues."""

    contract_path = root / "contracts" / "artifacts.json"
    if not contract_path.is_file():
        return ["missing contracts/artifacts.json"]

    try:
        contract = load_contract(root)
    except (json.JSONDecodeError, OSError) as exc:
        return [f"cannot load contracts/artifacts.json: {exc}"]

    issues = _validate_contract_shape(contract)
    if issues:
        return sorted(set(issues))

    issues.extend(_validate_artifacts(root, contract))
    issues.extend(_validate_aliases(root, contract))
    issues.extend(_validate_case_manifests(root, contract))
    issues.extend(_validate_markdown_links(root))
    issues.extend(_validate_repository_path_references(root))
    return sorted(set(issues))


def main() -> int:
    issues = run_checks(ROOT)
    if issues:
        print(f"FDE Operator OS validation failed with {len(issues)} issue(s):")
        for issue in issues:
            print(f"- {issue}")
        return 1

    contract = load_contract(ROOT)
    print(
        "FDE Operator OS validation passed: "
        f"{len(contract['artifacts'])} artifacts, "
        f"{len(contract.get('gates', []))} gates, "
        f"{len(contract.get('aliases', []))} compatibility alias(es)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
