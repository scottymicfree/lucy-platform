from __future__ import annotations

from backend.core.models import AgentOutput


def score_output(o: AgentOutput) -> float:
    return o.confidence * 0.4 + o.relevance * 0.3 + o.consistency * 0.2 + o.novelty * 0.1
