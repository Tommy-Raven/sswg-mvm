#!/usr/bin/env python3
"""
ai_cores/governance_core.py — Governance document detection utilities.

Provides deterministic scanning helpers for governance-like documents.
"""

from __future__ import annotations

import fnmatch
import re
from pathlib import Path
from typing import Iterable, List

__all__ = [
    "GOVERNANCE_FILENAME_PATTERNS",
    "GOVERNANCE_TOKEN_PATTERNS",
    "find_governance_like_files",
    "is_governance_like",
]

GOVERNANCE_FILENAME_PATTERNS = [
    "AGENTS.md",
    "TERMINOLOGY.md",
    "*CONSTITUTION*.md",
    "*POLICY*.md",
    "*GOVERNANCE*.md",
    "*GUARANTEE*.md",
    "*ARCHITECTURE*.md",
    "*REFERENCES*.md",
]

GOVERNANCE_TOKEN_PATTERNS = [
    "MUST",
    "SHALL",
    "invariant",
    "governance",
    "validator",
    "enforcement",
    "fail_closed",
]

EXCLUDED_DIRS = {".git", "directive_core", "legacy_governance"}


def _matches_filename(name: str) -> bool:
    return any(fnmatch.fnmatch(name, pattern) for pattern in GOVERNANCE_FILENAME_PATTERNS)


def _matches_tokens(payload: str) -> bool:
    for token in GOVERNANCE_TOKEN_PATTERNS:
        if re.search(rf"\b{re.escape(token)}\b", payload, flags=re.IGNORECASE):
            return True
    return False


def is_governance_like(path: Path) -> bool:
    """Return True when the file meets governance-like criteria."""
    if _matches_filename(path.name):
        return True
    try:
        payload = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return _matches_tokens(payload)


def _is_excluded(path: Path, repo_root: Path) -> bool:
    try:
        relative = path.relative_to(repo_root)
    except ValueError:
        return True
    return any(part in EXCLUDED_DIRS for part in relative.parts)


def find_governance_like_files(repo_root: Path) -> List[Path]:
    """Return governance-like files outside directive_core/docs."""
    repo_root = repo_root.resolve()
    matches: List[Path] = []
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        if _is_excluded(path, repo_root):
            continue
        if is_governance_like(path):
            matches.append(path.relative_to(repo_root))
    return sorted(matches)
