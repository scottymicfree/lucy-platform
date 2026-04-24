from __future__ import annotations

from backend.core.models import StructuredInput


def select_agents(structured_input: StructuredInput) -> list[str]:
    # Simple router by domain/intent.
    agents = ["lucy3_base", "lucy_3_eve", "lucy3_ai_os", "lucy3_3"]
    if structured_input.intent == "debug_request":
        return ["lucy3_ai_os", "lucy3_base", "lucy_3_eve"]
    return agents[:2]
