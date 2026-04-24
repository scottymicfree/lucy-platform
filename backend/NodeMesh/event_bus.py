from __future__ import annotations

import asyncio
from collections import defaultdict
from typing import Awaitable, Callable

from backend.core.models import NodeMessage


Handler = Callable[[NodeMessage], Awaitable[None]]


class EventBus:
    """In-process async pub/sub bus.

    Contract: nodes never call each other directly; everything goes through this bus.
    """

    def __init__(self) -> None:
        self._subs: dict[str, list[Handler]] = defaultdict(list)

    def subscribe(self, target: str, handler: Handler) -> None:
        self._subs[target].append(handler)

    async def publish(self, msg: NodeMessage) -> None:
        handlers = list(self._subs.get(msg.target, []))
        if not handlers:
            return
        await asyncio.gather(*(h(msg) for h in handlers))
