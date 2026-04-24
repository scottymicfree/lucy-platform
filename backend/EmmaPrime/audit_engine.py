from __future__ import annotations

from typing import Any

from backend.core.models import MergedReasoning


def build_audit(merged: MergedReasoning) -> dict[str, Any]:
    return {
        "selected_agents": merged.selected_agents,
        "final_score": merged.final_score,
        "flags": merged.flags,
    }
