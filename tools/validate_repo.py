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
CONTRACT_PATH = ROOT / "contracts" / "artifacts.json"
REQUIRED_TEMPLATE_SECTIONS = (
    "Use",
    "Required Fields",
    "Typical Anti-Pattern",
    "Completion Standard",
    "Template",
)
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


def _validate_contract_shape(contract: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    artifacts = contract.get("artifacts")
    if not isinstance(artifacts, dict) or not artifacts:
        return ["contracts/artifacts.json: 'artifacts' must be a non-empty object"]

    for artifact_id, artifact in artifacts.items():
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
        required_fields = artifact.get("required_fields", [])
        normalized = [normalize_field(item) for item in required_fields]
        if len(normalized) != len(set(normalized)):
            issues.append(
                f"contract:{artifact_id}: duplicate required fields after normalization"
            )

    for name, source in contract.get("source_of_truth", {}).items():
        artifact_id = source.get("artifact")
        field = source.get("field")
        artifact = artifacts.get(artifact_id)
        if artifact is None:
            issues.append(f"source_of_truth:{name}: unknown artifact '{artifact_id}'")
            continue
        if normalize_field(field) not in {
            normalize_field(item) for item in artifact.get("required_fields", [])
        }:
            issues.append(
                f"source_of_truth:{name}: field '{field}' is not required by '{artifact_id}'"
            )

    for gate in contract.get("gates", []):
        gate_id = gate.get("id", "<unknown>")
        for artifact_id in gate.get("required_artifacts", []):
            if artifact_id not in artifacts:
                issues.append(f"gate:{gate_id}: unknown artifact '{artifact_id}'")

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
    gate_ids = {gate["id"] for gate in contract.get("gates", [])}
    allowed_statuses = {"pass", "conditional", "fail", "hold", "not-run"}

    schema_path = root / contract.get("case_manifest_schema", "")
    if not schema_path.is_file():
        issues.append(
            f"contract: missing case manifest schema '{contract.get('case_manifest_schema', '')}'"
        )

    for manifest_path in sorted((root / "examples").glob("**/case-manifest.json")):
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append(
                f"case-manifest:{manifest_path.relative_to(root)}: invalid JSON: {exc}"
            )
            continue

        for key in ("case_id", "synthetic", "artifacts", "gates"):
            if key not in manifest:
                issues.append(
                    f"case-manifest:{manifest_path.relative_to(root)}: missing key '{key}'"
                )

        for artifact_id, relative_path in manifest.get("artifacts", {}).items():
            if artifact_id not in artifact_ids:
                issues.append(
                    f"case-manifest:{manifest_path.relative_to(root)}: unknown artifact '{artifact_id}'"
                )
                continue
            artifact_path = manifest_path.parent / relative_path
            if not artifact_path.is_file():
                issues.append(
                    f"case-manifest:{manifest_path.relative_to(root)}: missing artifact file "
                    f"'{relative_path}' for '{artifact_id}'"
                )
                continue
            artifact_text = artifact_path.read_text(encoding="utf-8")
            for marker in contract["artifacts"][artifact_id].get(
                "template_markers", []
            ):
                if marker not in artifact_text:
                    issues.append(
                        f"case-manifest:{manifest_path.relative_to(root)}: artifact "
                        f"'{relative_path}' is missing contract marker for '{artifact_id}': {marker}"
                    )

        for gate_id, status in manifest.get("gates", {}).items():
            if gate_id not in gate_ids:
                issues.append(
                    f"case-manifest:{manifest_path.relative_to(root)}: unknown gate '{gate_id}'"
                )
            if status not in allowed_statuses:
                issues.append(
                    f"case-manifest:{manifest_path.relative_to(root)}: invalid status "
                    f"'{status}' for '{gate_id}'"
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

    issues: list[str] = []
    contract_path = root / "contracts" / "artifacts.json"
    if not contract_path.is_file():
        return ["missing contracts/artifacts.json"]

    try:
        contract = load_contract(root)
    except (json.JSONDecodeError, OSError) as exc:
        return [f"cannot load contracts/artifacts.json: {exc}"]

    issues.extend(_validate_contract_shape(contract))
    if issues:
        return issues

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
