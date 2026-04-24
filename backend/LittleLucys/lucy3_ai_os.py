from __future__ import annotations

from backend.LittleLucys.base_agent import BaseAgent
from backend.core.models import AgentOutput, RetrievedContext, StructuredInput


class Lucy3AIOS(BaseAgent):
    agent_id = "lucy3_ai_os"

    async def reason(self, structured_input: StructuredInput, context: RetrievedContext) -> AgentOutput:
        return AgentOutput(
            agent_id=self.agent_id,
            reasoning="Planned a minimal reproducible checklist.",
            draft_output="Run: health check → dependency check → config check → reproduce → patch.",
            confidence=0.80,
            relevance=0.77,
            consistency=0.79,
            novelty=0.33,
            trace=["plan", "checklist"],
        )
