#!/usr/bin/env python3
"""
ai_cores/module_core.py — Canonical module registry utilities for SSWG MVM.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable, Dict, Iterable, List, Optional, Union

ModuleFunc = Union[Callable[..., Any], Callable[..., Awaitable[Any]]]


@dataclass
class ModuleEntry:
    """Descriptor for a registered module."""

    module_id: str
    func: ModuleFunc
    phase_id: Optional[str] = None
    inputs: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)
    description: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


class ModuleRegistryCore:
    """In-memory module registry with lookup and listing helpers."""

    def __init__(self) -> None:
        self._modules: Dict[str, ModuleEntry] = {}

    def register(
        self,
        module_id: str,
        func: ModuleFunc,
        *,
        phase_id: Optional[str] = None,
        inputs: Optional[Iterable[str]] = None,
        outputs: Optional[Iterable[str]] = None,
        description: str = "",
        metadata: Optional[Dict[str, Any]] = None,
        overwrite: bool = False,
    ) -> ModuleEntry:
        if not overwrite and module_id in self._modules:
            raise ValueError(f"Module {module_id!r} already registered")
        entry = ModuleEntry(
            module_id=module_id,
            func=func,
            phase_id=phase_id,
            inputs=list(inputs or []),
            outputs=list(outputs or []),
            description=description,
            metadata=metadata or {},
        )
        self._modules[module_id] = entry
        return entry

    def get(self, module_id: str) -> Optional[ModuleEntry]:
        return self._modules.get(module_id)

    def require(self, module_id: str) -> ModuleEntry:
        entry = self.get(module_id)
        if entry is None:
            raise KeyError(f"Module not registered: {module_id}")
        return entry

    def list_modules(self) -> List[ModuleEntry]:
        return list(self._modules.values())

    def list_by_phase(self, phase_id: str) -> List[ModuleEntry]:
        return [entry for entry in self._modules.values() if entry.phase_id == phase_id]

    def __contains__(self, module_id: str) -> bool:
        return module_id in self._modules

    def __len__(self) -> int:
        return len(self._modules)
