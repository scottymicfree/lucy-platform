from __future__ import annotations

from pydantic import BaseModel


class InputRequest(BaseModel):
    text: str
    source: str = "mobile"
    session_id: str | None = None


class InputResponse(BaseModel):
    request_id: str
    session_id: str


class HealthResponse(BaseModel):
    ok: bool = True
