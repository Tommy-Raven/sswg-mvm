"""
Tests Orchestrator integration.
"""

from ai_core.orchestrator import Orchestrator
from ai_validation.schema_validator import validate_workflow


def test_orchestrator_runs():
    orch = Orchestrator()
    wf = orch.run({"purpose": "Integration Test"})

    assert isinstance(wf, dict)
    valid, err = validate_workflow(wf)
    assert valid, f"Schema validation failed: {err}"
