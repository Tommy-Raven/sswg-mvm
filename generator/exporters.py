#!/usr/bin/env python3
"""
generator/exporters.py — Export helpers for SSWG.

Supports exporting workflows to Markdown and JSON, plus async helpers
for running both exports in parallel.
"""

from __future__ import annotations

import asyncio
import json
import os
from typing import Any, Awaitable, Callable, Dict

from .utils import log


def ensure_dir_exists(path: str) -> None:
    """
    Ensure the directory for a given path exists.

    Args:
        path:
            Directory path to create if missing.
    """
    os.makedirs(path, exist_ok=True)


def export_markdown(workflow: Any, out_dir: str = "templates") -> str:
    """
    Export a workflow-like object to Markdown format.

    The workflow object is expected to expose:
    - workflow_id
    - objective
    - structured_instruction (mapping of stage -> steps)
    - modular_workflow (dict with "modules" and "dependencies")
    - evaluation_report (optional mapping)

    Args:
        workflow:
            Workflow-like object.
        out_dir:
            Output directory for the file.

    Returns:
        Path to the written Markdown file.
    """
    ensure_dir_exists(out_dir)
    filename = os.path.join(out_dir, f"{workflow.workflow_id}.md")

    log(f"Exporting workflow {workflow.workflow_id} → Markdown")
    markdown_content = f"# Workflow {workflow.workflow_id}\n\n"
    markdown_content += f"**Objective:** {workflow.objective}\n\n## Stages\n"

    for stage_name, steps in workflow.structured_instruction.items():
        markdown_content += f"### {stage_name}\n"
        for step in steps:
            markdown_content += f"- {step}\n"

    markdown_content += "\n## Modules\n"
    markdown_content += json.dumps(
        workflow.modular_workflow.get("modules", {}),
        indent=2,
    )
    markdown_content += "\n\n## Dependencies\n"
    for dependency in workflow.modular_workflow.get("dependencies", []):
        markdown_content += f"- {dependency}\n"

    markdown_content += "\n\n## Evaluation Report\n"
    for key, value in (workflow.evaluation_report or {}).items():
        markdown_content += f"- {key.capitalize()}: {value}\n"

    with open(filename, "w", encoding="utf-8") as file_handle:
        file_handle.write(markdown_content)

    log(f"Markdown saved at {filename}")
    return filename


def export_json(workflow: Any, out_dir: str = "templates") -> str:
    """
    Export a workflow-like object to JSON format.

    Args:
        workflow:
            Workflow-like object.
        out_dir:
            Output directory for the file.

    Returns:
        Path to the written JSON file.
    """
    ensure_dir_exists(out_dir)
    filename = os.path.join(out_dir, f"{workflow.workflow_id}.json")

    log(f"Exporting workflow {workflow.workflow_id} → JSON")
    data: Dict[str, Any] = {
        "workflow_id": workflow.workflow_id,
        "objective": workflow.objective,
        "stages": workflow.structured_instruction,
        "modules": workflow.modular_workflow,
        "evaluation_report": workflow.evaluation_report,
        "improved_workflow": workflow.improved_workflow,
    }

    with open(filename, "w", encoding="utf-8") as file_handle:
        json.dump(data, file_handle, indent=4)

    log(f"JSON saved at {filename}")
    return filename


# ─── Async Helpers ───────────────────────────────────────────────

async def run_task(
    task_func: Callable[..., Awaitable[Any]],
    *args: Any,
    **kwargs: Any,
) -> Any:
    """
    Run an async task and catch exceptions, logging errors.

    Returns:
        The result of the async function, or None if it failed.
    """
    try:
        return await task_func(*args, **kwargs)
    except Exception as exc:  # pylint: disable=broad-exception-caught
        log(f"Async task {task_func.__name__} failed: {exc}")
        return None


async def export_workflow_async(workflow: Any, out_dir: str = "templates") -> None:
    """
    Run both JSON and Markdown export tasks asynchronously.
    """
    await asyncio.gather(
        run_task(export_json, workflow, out_dir),
        run_task(export_markdown, workflow, out_dir),
    )
