#!/usr/bin/env python3
"""
Quick scanner for JSON Schemas under ./schemas to detect bad $ref / $id values.

It will print any $ref or $id whose value is NOT a string, which is exactly
the kind of thing that can cause jsonschema's resolver to blow up with
'TypeError: unhashable type: dict'.
"""

from __future__ import annotations

from pathlib import Path
import json
from typing import Any, Tuple

SCHEMAS_DIR = Path("schemas")  # adjust if your schemas live elsewhere


def walk_for_key(
    obj: Any,
    key_name: str,
    file_name: str,
    path: Tuple[str, ...] = (),
) -> None:
    """
    Recursively walk a JSON-like structure and print any occurrence
    of key_name whose value is not a string.
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_path = path + (k,)
            if k == key_name and not isinstance(v, str):
                print(
                    f"Non-string {key_name} in {file_name} at "
                    f"{' -> '.join(new_path)}: {v!r}"
                )
            walk_for_key(v, key_name, file_name, new_path)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            walk_for_key(item, key_name, file_name, path + (f"[{i}]",))


def main() -> int:
    """
    Entry point for the schema URI scanner.

    Scans all *.json files under SCHEMAS_DIR and reports any $ref or $id
    whose value is not a string.
    """
    if not SCHEMAS_DIR.exists():
        print(f"Schemas directory not found at: {SCHEMAS_DIR}")
        return 1

    print(f"Scanning schemas in: {SCHEMAS_DIR.resolve()}")
    any_issues = False

    for schema_path in sorted(SCHEMAS_DIR.glob("*.json")):
        file_name = schema_path.name
        try:
            data = json.loads(schema_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"Failed to load {schema_path}: {exc}")
            any_issues = True
            continue

        # Look for bad $ref and $id values
        walk_for_key(data, "$ref", file_name)
        walk_for_key(data, "$id", file_name)

    print("Scan complete.")
    return 1 if any_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
