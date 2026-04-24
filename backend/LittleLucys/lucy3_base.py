from __future__ import annotations

from backend.LittleLucys.base_agent import BaseAgent
from backend.core.models import AgentOutput, RetrievedContext, StructuredInput


class Lucy3Base(BaseAgent):
    agent_id = "lucy3_base"

    async def reason(self, structured_input: StructuredInput, context: RetrievedContext) -> AgentOutput:
        return AgentOutput(
            agent_id=self.agent_id,
            reasoning="Decomposed request into steps.",
            draft_output=f"I can help with: {structured_input.text}",
            confidence=0.78,
            relevance=0.74,
            consistency=0.76,
            novelty=0.42,
            trace=["decompose", "outline"],
        )
