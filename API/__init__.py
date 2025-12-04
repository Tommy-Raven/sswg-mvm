#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API Package Initialization — SSWG-MVM v.09.mvm.25

This package provides a stable, public-facing Python API layer for
programmatic access to workflow loading, validation, refinement, export,
and metadata inspection.

It exposes high-level helper functions for developers, external agents,
and automated CI/CD systems.

Authors:
    Tommy Raven / Thomas Byers
    Raven Recordings, LLC © 2025

Version:
    v.09.mvm.25
"""

from .workflows import (
    load_workflow_file,
    load_template,
    validate,
    refine,
    export,
    generate_mermaid,
    get_metadata,
    get_phases,
    get_dependency_graph,
)

__all__ = [
    "load_workflow_file",
    "load_template",
    "validate",
    "refine",
    "export",
    "generate_mermaid",
    "get_metadata",
    "get_phases",
    "get_dependency_graph",
]
