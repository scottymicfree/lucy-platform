from __future__ import annotations

from backend.core.models import StructuredInput


def process_input(raw_text: str, request_id: str, session_id: str, source: str = "mobile") -> StructuredInput:
    text = (raw_text or "").strip()
    intent = "debug_request" if "debug" in text.lower() else "general_request"
    domain = "system" if "gpu" in text.lower() else "general"
    return StructuredInput(
        request_id=request_id,
        session_id=session_id,
        text=text,
        source=source,
        intent=intent,
        domain=domain,
        urgency="normal",
        metadata={"entities": []},
    )
