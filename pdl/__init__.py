#!/usr/bin/env python3
"""
pdl package — Prompt Description Language defaults for SSWG.

Provides a minimal, MVM-grade interface for:
- loading default phase definitions
- loading the default workflow spec (JSON-backed)
- executing a named phase
"""

from __future__ import annotations

from .default_pdl import (
    execute_phase,
    load_default_phases,
    load_default_workflow_spec,
)

__all__ = [
    "execute_phase",
    "load_default_phases",
    "load_default_workflow_spec",
    "get_version",
]


def get_version() -> str:
    """Return a simple version identifier for the PDL subsystem."""
    return "pdl-mvm-0.1.0"
