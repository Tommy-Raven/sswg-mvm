from __future__ import annotations

from pathlib import Path
import sys

import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from generator.pdl_validator import validate_pdl_file
from pdl.constants import CANONICAL_PHASES


def main() -> int:
    pdl_path = Path("pdl/default-pdf.yaml")
    validate_pdl_file(pdl_path)
    payload = yaml.safe_load(pdl_path.read_text(encoding="utf-8"))
    phases = payload.get("phases", [])
    phase_names = [phase.get("name") for phase in phases]
    if phase_names != CANONICAL_PHASES:
        raise ValueError(
            "PDL default phases do not match canonical order: "
            f"{phase_names} != {CANONICAL_PHASES}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
