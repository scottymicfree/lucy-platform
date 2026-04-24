from __future__ import annotations

import asyncio

from backend.EmmaPrime.audit_engine import build_audit
from backend.EmmaPrime.merge_engine import score_output
from backend.EmmaPrime.router import select_agents
from backend.EmmaPrime.safety_gate import safety_check
from backend.LittleLucys.agent_registry import get_agent
from backend.LucyPrime.identity_core import apply_identity
from backend.LucyPrime.output_formatter import format_output
from backend.LucyPrime.synthesis_engine import synthesize
from backend.Memory.memory_manager import MemoryManager
from backend.Perception.classifier import classify
from backend.Perception.input_processor import process_input
from backend.core.models import AgentOutput, MergedReasoning
from backend.core.utils import new_id, now_ms


class Orchestrator:
    def __init__(self, memory: MemoryManager, logger, trainer) -> None:
        self.memory = memory
        self.logger = logger
        self.trainer = trainer

    async def handle_input(self, text: str, source: str, session_id: str | None):
        request_id = new_id("req")
        session_id = session_id or new_id("sess")

        structured = classify(process_input(text, request_id=request_id, session_id=session_id, source=source))
        context = self.memory.retrieve(structured)

        agent_ids = select_agents(structured)
        agents = [get_agent(aid) for aid in agent_ids]

        outputs: list[AgentOutput] = await asyncio.gather(*[a.reason(structured, context) for a in agents])

        scored = [(o, score_output(o)) for o in outputs]
        scored.sort(key=lambda t: t[1], reverse=True)
        final_score = scored[0][1] if scored else 0.0

        merged = MergedReasoning(
            selected_agents=agent_ids,
            agent_outputs=[o for o, _s in scored],
            final_score=final_score,
            merged_rationale="Merged top candidates via Emma scoring.",
            flags=[],
        )

        ok, safety_flags = safety_check(merged)
        if not ok:
            merged.flags.extend(safety_flags)

        final = synthesize(merged, structured, safety_flags=safety_flags)
        final.response = format_output(apply_identity(final.response))

        # logs + training + episodic write
        audit = build_audit(merged)
        self.logger.write({"ts": now_ms(), "event": "request", "structured": structured.model_dump(), "audit": audit})
        self.trainer.write({"ts": now_ms(), "request_id": request_id, "audit": audit, "final": final.model_dump()})
        self.memory.write_episode(structured, final.response)

        return request_id, session_id, final
