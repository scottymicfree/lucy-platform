from __future__ import annotations

from backend.core.models import AgentOutput, RetrievedContext, StructuredInput


class BaseAgent:
    agent_id: str

    async def reason(self, structured_input: StructuredInput, context: RetrievedContext) -> AgentOutput:
        raise NotImplementedError
