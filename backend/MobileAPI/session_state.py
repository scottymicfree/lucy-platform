from __future__ import annotations

from dataclasses import dataclass

from backend.core.models import FinalResponse


@dataclass
class SessionState:
    latest: FinalResponse | None = None
