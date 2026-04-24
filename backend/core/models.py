from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


MessageType = Literal["request", "response", "event"]


class NodeMessage(BaseModel):
    """Strict node-to-node/event-bus message contract (canonical)."""

    id: str
    source: str
    target: str
    type: MessageType
    payload: dict[str, Any] = Field(default_factory=dict)
    confidence: float = 0.0
    trace: list[str] = Field(default_factory=list)
    timestamp: int


class StructuredInput(BaseModel):
    request_id: str
    session_id: str
    text: str
    source: str = "mobile"
    intent: str | None = None
    domain: str | None = None
    urgency: str = "normal"
    metadata: dict[str, Any] = Field(default_factory=dict)


class RetrievedContext(BaseModel):
    items: list[dict[str, Any]] = Field(default_factory=list)


class AgentOutput(BaseModel):
    agent_id: str
    reasoning: str
    draft_output: str
    confidence: float
    relevance: float
    consistency: float
    novelty: float
    trace: list[str] = Field(default_factory=list)


class MergedReasoning(BaseModel):
    selected_agents: list[str]
    agent_outputs: list[AgentOutput]
    final_score: float
    merged_rationale: str
    flags: list[str] = Field(default_factory=list)


class FinalResponse(BaseModel):
    request_id: str
    session_id: str
    response: str
    confidence: float
    source: str = "LucyPrime"
    flags: list[str] = Field(default_factory=list)


class TrainingRecord(BaseModel):
    request_id: str
    timestamp: int
    input: StructuredInput
    retrieved_context: list[dict[str, Any]]
    selected_agents: list[str]
    agent_outputs: list[dict[str, Any]]
    emma_scores: dict[str, Any]
    merged_reasoning: dict[str, Any]
    final_output: str
    memory_write: bool
