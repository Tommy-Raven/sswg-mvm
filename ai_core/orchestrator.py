from generator.main import generate_workflow
from ai_memory.memory_store import MemoryStore
from ai_validation.schema_validator import validate_workflow
from ai_monitoring.cli_dashboard import CLIDashboard
from ai_monitoring.telemetry import TelemetryLogger
from generator.utils import log


class Orchestrator:
    def __init__(self):
        # Initialize memory and CLI dashboard
        self.memory = MemoryStore()
        self.dashboard = CLIDashboard()
        
        self.telemetry = TelemetryLogger()

    def run(self, user_config, recursive=False):
        log("Starting workflow orchestration…")

        self.telemetry.record("workflow_start", {"config": user_config})

        # Generate workflow
        wf = generate_workflow(user_config)

        self.telemetry.record("workflow_created", {"id": wf.get("workflow_id")})

        # Validate generated workflow
        valid, err = validate_workflow(wf)

        if not valid:
            log(f"Schema validation failed: {err}", level="ERROR")
            self.dashboard.record_cycle(success=False)

            self.telemetry.record("validation_error", {"error": err})

            raise ValueError(f"Invalid workflow schema: {err}")

        # Save valid workflow to memory
        self.memory.save(wf)
        log(f"Workflow {wf.get('workflow_id', '<no-id>')} stored in memory.")
        self.dashboard.record_cycle(success=True)

        self.telemetry.record("workflow_saved", {"id": wf["workflow_id"]})

        # Handle optional recursive expansions
        if recursive and "expansion_mode" in user_config:
            for mode in user_config["expansion_mode"]:
                log(f"Running recursive mode: {mode}")

                self.telemetry.record("recursive_mode_start", {"mode": mode})

                # (placeholder for recursion logic)
                # Example: wf = recursive_expand(wf, mode)

                self.telemetry.record("recursive_mode_end", {"mode": mode})

                self.dashboard.record_cycle(success=True)

        # Render CLI dashboard summary
        self.dashboard.render()

        self.telemetry.record("workflow_complete", {"workflow_id": wf["workflow_id"]})

        log("Workflow orchestration complete.")
        return wf
