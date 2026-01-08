from __future__ import annotations

from pathlib import Path

CANONICAL_GOVERNANCE_ORDER = [
    "TERMINOLOGY.md",
    "SSWG_CONSTITUTION.md",
    "AGENTS.md",
    "ARCHITECTURE.md",
    "FORMAL_GUARANTEES.md",
    "REFERENCES.md",
    "deprecated_nomenclature.md",
]


class GovernanceIngestionError(RuntimeError):
    pass


def validate_governance_ingestion_order(
    docs_dir: Path,
    expected_order: list[str],
) -> bool:
    """
    Enforces canonical governance ingestion order.
    Fail-closed on any deviation.
    """

    if not docs_dir.exists() or not docs_dir.is_dir():
        raise GovernanceIngestionError(
            f"[governance_violation] docs directory not found: {docs_dir}"
        )

    present = sorted(
        p.name for p in docs_dir.iterdir() if p.is_file() and p.suffix == ".md"
    )

    expected_set = set(expected_order)
    present_set = set(present)

    missing = expected_set - present_set
    if missing:
        raise GovernanceIngestionError(
            f"[governance_violation] missing governance documents: {sorted(missing)}"
        )

    present_ordered = [name for name in present if name in expected_set]

    if present_ordered != expected_order:
        raise GovernanceIngestionError(
            "[governance_violation] governance ingestion order mismatch\n"
            f"expected: {expected_order}\n"
            f"found:    {present_ordered}"
        )

    return True
