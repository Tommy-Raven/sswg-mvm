#!/usr/bin/env python3
"""
directive_core/directive_core_validator.py — Directive core validation gate.

Validates:
- directive_index.json against directive_index.schema.json
- canonical_path normalization against the computed directive_core root
- directive definition JSON files against their schemas
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from ai_cores.schema_core import validate_artifact

CORE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = CORE_ROOT.parent
INDEX_PATH = CORE_ROOT / "directive_index.json"
SCHEMAS_DIR = CORE_ROOT / "schemas"
DEFINITIONS_DIR = CORE_ROOT / "definitions"


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _normalize_path(value: str) -> str:
    return Path(value).as_posix().rstrip("/")


def _relative_to_repo(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _format_schema_errors(errors: Iterable[dict]) -> list[str]:
    formatted: list[str] = []
    for error in errors:
        message = error.get("message", "Schema validation error")
        path = "/".join(str(part) for part in error.get("path", []))
        formatted.append(f"{message} (path: {path or 'root'})")
    return formatted


def validate_directive_core() -> list[str]:
    errors: list[str] = []

    if not INDEX_PATH.exists():
        return [f"Missing directive index: {INDEX_PATH}"]

    index = _load_json(INDEX_PATH)
    index_errors = validate_artifact(index, SCHEMAS_DIR, "directive_index.schema.json")
    if index_errors:
        errors.extend(
            f"directive_index.json: {message}"
            for message in _format_schema_errors(index_errors)
        )

    canonical_path = _normalize_path(index.get("canonical_path", ""))
    computed_core_root = _normalize_path(_relative_to_repo(CORE_ROOT))
    if canonical_path != computed_core_root:
        errors.append(
            "directive_index.json: canonical_path mismatch "
            f"(expected '{computed_core_root}', got '{canonical_path}')"
        )

    definitions = index.get("definitions", [])
    seen_directive_ids: set[str] = set()
    listed_definition_paths: set[str] = set()

    for entry in definitions:
        directive_id = entry.get("directive_id")
        definition_path = entry.get("definition_path")
        schema_path = entry.get("schema_path")
        if directive_id in seen_directive_ids:
            errors.append(f"Duplicate directive_id in index: {directive_id}")
        seen_directive_ids.add(directive_id)

        if not definition_path or not schema_path:
            continue

        normalized_definition_path = _normalize_path(definition_path)
        listed_definition_paths.add(normalized_definition_path)
        definition_full_path = REPO_ROOT / normalized_definition_path
        schema_full_path = REPO_ROOT / _normalize_path(schema_path)

        if not definition_full_path.exists():
            errors.append(f"Missing directive definition: {definition_full_path}")
            continue
        if not schema_full_path.exists():
            errors.append(f"Missing directive schema: {schema_full_path}")
            continue

        definition = _load_json(definition_full_path)
        definition_errors = validate_artifact(
            definition,
            schema_full_path.parent,
            schema_full_path.name,
        )
        if definition_errors:
            errors.extend(
                f"{definition_full_path}: {message}"
                for message in _format_schema_errors(definition_errors)
            )

        if directive_id and definition.get("directive_id") != directive_id:
            errors.append(
                f"{definition_full_path}: directive_id mismatch "
                f"(index '{directive_id}', definition '{definition.get('directive_id')}')"
            )
        if directive_id and definition.get("anchor_id") != directive_id:
            errors.append(
                f"{definition_full_path}: anchor_id mismatch "
                f"(expected '{directive_id}', got '{definition.get('anchor_id')}')"
            )

        source_path = definition.get("source_path")
        if source_path:
            source_full_path = REPO_ROOT / _normalize_path(source_path)
            if not source_full_path.exists():
                errors.append(f"{definition_full_path}: missing source_path {source_full_path}")

    if DEFINITIONS_DIR.exists():
        for path in DEFINITIONS_DIR.rglob("*.json"):
            relative_path = _normalize_path(_relative_to_repo(path))
            if relative_path not in listed_definition_paths:
                errors.append(f"Unregistered directive definition: {relative_path}")

    return errors


def main() -> int:
    errors = validate_directive_core()
    if errors:
        for error in errors:
            print(error)
        return 1
    print("directive_core validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
