from ai_core.orchestrator import Orchestrator
from ai_validation.schema_validator import validate_workflow

def test_orchestrator_workflow_generation(tmp_path):
    orch = Orchestrator()
    wf = orch.run({"purpose": "Test"})
    valid, err = validate_workflow(wf)
    assert valid, err
