"""Validation tests governed by deterministic agent scope per AGENTS.md §9."""
from __future__ import annotations

from pathlib import Path

import yaml

from generator.pdl_validator import validate_pdl_file
from pdl.constants import CANONICAL_PHASES
from pdl.default_pdl import load_default_phases


def test_default_pdf_validates_against_schema() -> None:
    validate_pdl_file(Path("pdl/default-pdf.yaml"))


def test_default_pdf_phase_order_matches_canonical() -> None:
    payload = yaml.safe_load(Path("pdl/default-pdf.yaml").read_text(encoding="utf-8"))
    phases = payload.get("phases", [])
    phase_names = [phase.get("name") for phase in phases]
    assert phase_names == CANONICAL_PHASES


def test_load_default_phases_matches_canonical_order() -> None:
    phases = load_default_phases()
    assert list(phases.keys()) == CANONICAL_PHASES
