from __future__ import annotations

from backend.core.models import FinalResponse


def as_mobile_payload(final: FinalResponse) -> dict:
    return asdict(final)


def asdict(final: FinalResponse) -> dict:
    return final.model_dump()
