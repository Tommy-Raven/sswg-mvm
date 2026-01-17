#!/usr/bin/env python3
"""
cli package — command line interface for the SSWG workflow system.

This package exposes a small, stable surface:
- build_parser() — construct the argparse CLI for reuse in tests or other tools
- main()        — default entrypoint
"""

from __future__ import annotations

from .cli import build_parser, main

__all__ = ["build_parser", "main", "get_version"]


def get_version() -> str:
    """Return a simple version identifier for the CLI subsystem."""
    return "cli-mvm-0.1.0"
