from __future__ import annotations

from fastapi import APIRouter, Depends, Header, HTTPException

from backend.MobileAPI.schemas import HealthResponse, InputRequest, InputResponse
from backend.MobileAPI.session_state import SessionState


def auth(x_lucy_token: str | None = Header(default=None), required_token: str | None = None):
    if required_token and x_lucy_token != required_token:
        raise HTTPException(status_code=401, detail="unauthorized")


def build_routes(orchestrator, state: SessionState, required_token: str | None):
    router = APIRouter()

    @router.get("/health", response_model=HealthResponse)
    async def health():
        return HealthResponse(ok=True)

    @router.post("/input", response_model=InputResponse)
    async def post_input(req: InputRequest, x_lucy_token: str | None = Header(default=None)):
        auth(x_lucy_token=x_lucy_token, required_token=required_token)
        request_id, session_id, _final = await orchestrator.handle_input(req.text, req.source, req.session_id)
        state.latest = _final
        return InputResponse(request_id=request_id, session_id=session_id)

    @router.get("/response")
    async def get_response(x_lucy_token: str | None = Header(default=None)):
        auth(x_lucy_token=x_lucy_token, required_token=required_token)
        return state.latest.model_dump() if state.latest else {"status": "empty"}

    @router.get("/state")
    async def get_state(x_lucy_token: str | None = Header(default=None)):
        auth(x_lucy_token=x_lucy_token, required_token=required_token)
        return {"lucy_state": "ready", "has_response": state.latest is not None}

    return router
