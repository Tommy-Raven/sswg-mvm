#!/usr/bin/env python3
"""
data/data_parsing.py — Template loading & normalization for sswg-mvm.

Responsibilities:
- Map human-friendly template slugs (e.g. "creative") to concrete JSON files.
- Load template JSON from disk.
- Normalize it into a schema-aligned workflow dict:
  - ensure workflow_id, version
  - ensure metadata with purpose/audience
  - migrate title/template_id/description into metadata
  - convert string tasks into task-objects {id, description}
  - ensure modules/evaluation sections exist
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Mapping


# Root directory for templates
TEMPLATES_ROOT = Path("data/templates")

# Simple slug → filename mapping for MVM
TEMPLATE_INDEX: Dict[str, str] = {
    "creative": "creative_writing_template.json",
    "meta": "meta_reflection_template.json",
    "technical": "technical_procedure_template.json",
    "training": "training_curriculum_template.json",
}


def _load_raw_template(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Template JSON not found: {path}")
    content = path.read_text(encoding="utf-8")
    return json.loads(content)


def _normalize_tasks(phase: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Convert a phase's tasks into object form if they are plain strings.

    Input:
      {
        "id": "P1",
        "title": "Concept Invocation",
        "tasks": ["Do a thing", "Do another thing"]
      }

    Output:
      {
        "id": "P1",
        "title": "Concept Invocation",
        "tasks": [
          {"id": "P1_T1", "description": "Do a thing"},
          {"id": "P1_T2", "description": "Do another thing"}
        ]
      }
    """
    phase_dict: Dict[str, Any] = dict(phase)
    pid = str(phase_dict.get("id") or phase_dict.get("name") or "P")

    tasks = phase_dict.get("tasks", [])
    normalized_tasks: List[Dict[str, Any]] = []

    if isinstance(tasks, list):
        for idx, task in enumerate(tasks, start=1):
            if isinstance(task, Mapping):
                # Already object-shaped, just shallow-copy
                normalized_tasks.append(dict(task))
            else:
                # String or something else → wrap as description
                normalized_tasks.append(
                    {
                        "id": f"{pid}_T{idx}",
                        "description": str(task),
                    }
                )

    phase_dict["tasks"] = normalized_tasks
    return phase_dict


def _normalize_template_structure(raw: Dict[str, Any], slug: str) -> Dict[str, Any]:
    """
    Transform a human-friendly template JSON into a schema-aligned workflow dict.
    """
    wf: Dict[str, Any] = dict(raw)  # shallow copy

    # ---- Root identity fields ------------------------------------
    wf_id = wf.get("workflow_id")
    if not wf_id:
        # Derive from slug + timestamp
        ts_suffix = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        wf_id = f"{slug}_template_{ts_suffix}"
    wf["workflow_id"] = str(wf_id)

    version = wf.get("version") or "0.1.0"
    wf["version"] = str(version)

    # ---- Metadata -------------------------------------------------
    metadata: Dict[str, Any] = dict(wf.get("metadata") or {})
    # migrate title/template_id/description into metadata
    if "title" in wf:
        metadata.setdefault("title", wf["title"])
    if "template_id" in wf:
        metadata.setdefault("template_id", wf["template_id"])
    if "description" in wf:
        metadata.setdefault("description", wf["description"])

    # Ensure purpose / audience required by schema
    metadata.setdefault(
        "purpose",
        metadata.get("description") or f"Workflow derived from '{slug}' template.",
    )
    metadata.setdefault("audience", "general")

    wf["metadata"] = metadata

    # Remove extra root-level keys that schema dislikes
    for key in ("title", "template_id", "description"):
        wf.pop(key, None)

    # ---- Phases & tasks -------------------------------------------
    phases = wf.get("phases", [])
    normalized_phases: List[Dict[str, Any]] = []

    if isinstance(phases, list):
        for phase in phases:
            if isinstance(phase, Mapping):
                normalized_phases.append(_normalize_tasks(phase))
            else:
                # Bare string phase? Make it a minimal phase with one task.
                normalized_phases.append(
                    {
                        "id": "P_auto",
                        "title": str(phase),
                        "tasks": [
                            {"id": "P_auto_T1", "description": str(phase)},
                        ],
                    }
                )

    wf["phases"] = normalized_phases

    # ---- Modules / evaluation scaffolding -------------------------
    wf.setdefault("modules", [])
    wf.setdefault("evaluation", {})

    return wf


def load_template(slug: str) -> Dict[str, Any]:
    """
    Load a named template and normalize it into a schema-aligned workflow dict.

    Args:
        slug: Human-friendly template name, e.g. "creative", "technical".

    Returns:
        Dict representing a workflow that should validate against workflow_schema.json
        (modulo any future schema evolution).
    """
    filename = TEMPLATE_INDEX.get(slug)
    if filename is None:
        raise KeyError(
            f"Unknown template slug '{slug}'. "
            f"Known templates: {sorted(TEMPLATE_INDEX.keys())}"
        )

    path = TEMPLATES_ROOT / filename
    raw = _load_raw_template(path)
    return _normalize_template_structure(raw, slug)
