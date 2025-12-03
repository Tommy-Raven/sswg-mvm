"""
SSWG PDL — Default Phase Definitions (Python)

Purpose:
    Provide a canonical placeholder for workflow phase definitions and
    utilities to load the default workflow spec (JSON-backed).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional


_DEFAULT_JSON_PATH = Path(__file__).with_name("default-pdf.json")


def load_default_phases() -> Dict[str, Dict[str, Any]]:
    """
    Load the default set of workflow phases.

    Returns:
        Mapping of phase names to placeholder definitions.
    """
    return {
        "ingest": {"description": "Collect input data / artifacts."},
        "parse": {"description": "Parse and normalize inputs."},
        "generate": {"description": "Generate workflows or outputs."},
        "output": {"description": "Persist or display generated artifacts."},
        "validate": {"description": "Run validation and sanity checks."},
        "log": {"description": "Record telemetry and logs."},
    }


def load_default_workflow_spec(path: Optional[str | Path] = None) -> Dict[str, Any]:
    """
    Load the default workflow spec from JSON.

    Args:
        path: Optional override path for the JSON spec. If omitted, the
              sibling file `default-pdf.json` is used.

    Returns:
        Parsed workflow spec dictionary.
    """
    spec_path = Path(path) if path is not None else _DEFAULT_JSON_PATH

    if not spec_path.exists():
        # Fallback: synthesize a spec using the known default phases.
        phases = list(load_default_phases().keys())
        return {
            "workflow": {
                "name": "default",
                "phases": phases,
            }
        }

    with spec_path.open("r", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def execute_phase(
    phase_name: str,
    context: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Execute a single default phase (placeholder).

    Args:
        phase_name:
            Name of the phase to execute.
        context:
            Optional context dictionary for phase execution. At MVM stage,
            this is only logged and not interpreted.
    """
    phase_definitions = load_default_phases()
    context = context or {}

    if phase_name not in phase_definitions:
        available = ", ".join(sorted(phase_definitions.keys()))
        print(f"[PDL] Unknown phase: {phase_name!r}")
        print(f"[PDL] Available phases: {available}")
        return

    context_keys = ", ".join(sorted(context.keys()))
    print(
        f"[PDL] Executing default phase: {phase_name} "
        f"(context keys: {context_keys or 'none'})"
    )
