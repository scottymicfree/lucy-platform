from __future__ import annotations

from backend.LittleLucys.base_agent import BaseAgent
from backend.core.models import AgentOutput, RetrievedContext, StructuredInput


class Lucy33(BaseAgent):
    agent_id = "lucy3_3"

    async def reason(self, structured_input: StructuredInput, context: RetrievedContext) -> AgentOutput:
        return AgentOutput(
            agent_id=self.agent_id,
            reasoning="Synthesized a user-friendly explanation.",
            draft_output="Here’s the simplest next action you can take safely.",
            confidence=0.68,
            relevance=0.66,
            consistency=0.73,
            novelty=0.55,
            trace=["simplify", "teach"],
        )
