from __future__ import annotations

from backend.Memory.episodic import EpisodicStore
from backend.Memory.retriever import retrieve_context
from backend.core.models import RetrievedContext, StructuredInput


class MemoryManager:
    def __init__(self, data_dir: str) -> None:
        self.episodic = EpisodicStore(data_dir=data_dir)

    def retrieve(self, structured_input: StructuredInput) -> RetrievedContext:
        return retrieve_context(structured_input)

    def write_episode(self, structured_input: StructuredInput, final_output: str) -> None:
        self.episodic.append({"input": structured_input.model_dump(), "final_output": final_output})
