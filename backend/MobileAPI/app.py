from __future__ import annotations

from fastapi import FastAPI

from backend.MobileAPI.routes import build_routes
from backend.MobileAPI.session_state import SessionState


def create_app(orchestrator, required_token: str | None = None) -> FastAPI:
    app = FastAPI(title="Lucy MobileAPI")
    state = SessionState()
    app.include_router(build_routes(orchestrator, state, required_token))
    return app
