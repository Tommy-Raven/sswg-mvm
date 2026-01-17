#!/usr/bin/env python3
"""
ai_cores/export_core.py — Shared export serialization utilities.

Provides deterministic JSON/Markdown serialization for workflow exports.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

__all__ = ["write_json", "write_markdown"]


def write_json(payload: Any, out_path: str | Path) -> str:
    """Serialize payload to JSON at the provided path."""
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return str(path)


def write_markdown(content: str, out_path: str | Path) -> str:
    """Write Markdown content to the provided path."""
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return str(path)
