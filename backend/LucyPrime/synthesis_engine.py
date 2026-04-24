from __future__ import annotations

from backend.core.models import FinalResponse, MergedReasoning, StructuredInput


def synthesize(merged: MergedReasoning, structured_input: StructuredInput, safety_flags: list[str]) -> FinalResponse:
    # Minimal: pick best draft_output by agent ordering, then format.
    best = merged.agent_outputs[0].draft_output if merged.agent_outputs else "No output."
    response_text = best
    if safety_flags:
        response_text = f"(Flags: {', '.join(safety_flags)})\n" + response_text

    return FinalResponse(
        request_id=structured_input.request_id,
        session_id=structured_input.session_id,
        response=response_text,
        confidence=max(0.1, min(0.99, merged.final_score)),
        flags=safety_flags,
    )
