from __future__ import annotations

from backend.core.models import MergedReasoning


def safety_check(merged: MergedReasoning) -> tuple[bool, list[str]]:
    flags: list[str] = []
    if merged.final_score < 0.35:
        flags.append("low_confidence")
    return (len(flags) == 0, flags)
