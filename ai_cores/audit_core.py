"""Shared audit helpers for hashing and timestamps."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path

__all__ = ["hash_file", "utc_timestamp"]


def hash_file(path: Path) -> str:
    """Hash file contents using SHA-256."""
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def utc_timestamp() -> str:
    """Return an ISO-8601 UTC timestamp with Z suffix."""
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
