#!/usr/bin/env python3
"""
generator/cache_manager.py — Async-aware Cache Manager for SSWG.

Provides a small file-based cache used by the generator to store
intermediate or final artifacts between runs.
"""

from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Optional


class CacheManager:
    """Async-aware file cache manager for storing and retrieving workflow artifacts."""

    def __init__(self, storage_path: Optional[Path] = None) -> None:
        """
        Args:
            storage_path:
                Path to the cache file. If None, caching is disabled.
        """
        self.storage_path = storage_path

        if self.storage_path is not None:
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)

    async def save(self, data: str) -> None:
        """
        Save data to the cache asynchronously.

        Args:
            data:
                Serialized data to write.
        """
        if self.storage_path is None:
            return

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(
            None,
            self.storage_path.write_text,
            data,
        )

    async def load(self) -> Optional[str]:
        """
        Load data from the cache asynchronously.

        Returns:
            Cached content, or None if the cache file does not exist.
        """
        if self.storage_path is None or not self.storage_path.exists():
            return None

        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None,
            self.storage_path.read_text,
        )

    async def clear(self) -> None:
        """
        Clear the cache asynchronously by deleting the underlying file.
        """
        if self.storage_path is None or not self.storage_path.exists():
            return

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(
            None,
            self.storage_path.unlink,
        )
