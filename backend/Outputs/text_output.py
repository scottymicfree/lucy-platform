from __future__ import annotations

from backend.core.models import FinalResponse


def as_text_payload(final: FinalResponse) -> dict:
    return {
        "request_id": final.request_id,
        "session_id": final.session_id,
        "response": final.response,
        "confidence": final.confidence,
        "source": final.source,
        "flags": final.flags,
    }
