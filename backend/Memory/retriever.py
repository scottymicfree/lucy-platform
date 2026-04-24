from __future__ import annotations

from backend.core.models import RetrievedContext, StructuredInput


def retrieve_context(structured_input: StructuredInput, top_k: int = 5) -> RetrievedContext:
    # v1 placeholder: returns empty context pack.
    return RetrievedContext(items=[])
