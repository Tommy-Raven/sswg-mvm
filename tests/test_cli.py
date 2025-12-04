"""
Tests the SSWG CLI entrypoint.
"""

import subprocess
import sys
from pathlib import Path


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "-m", "generator.main", "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "SSWG Workflow Generator" in result.stdout
