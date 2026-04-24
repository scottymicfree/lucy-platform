from __future__ import annotations

from backend.LittleLucys.base_agent import BaseAgent
from backend.core.models import AgentOutput, RetrievedContext, StructuredInput


class Lucy3Eve(BaseAgent):
    agent_id = "lucy_3_eve"

    async def reason(self, structured_input: StructuredInput, context: RetrievedContext) -> AgentOutput:
        return AgentOutput(
            agent_id=self.agent_id,
            reasoning="Checked assumptions and failure modes.",
            draft_output="Before acting, confirm constraints and logs.",
            confidence=0.72,
            relevance=0.70,
            consistency=0.78,
            novelty=0.38,
            trace=["assumptions", "risks"],
        )
