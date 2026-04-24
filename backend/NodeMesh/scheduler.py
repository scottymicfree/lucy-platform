from __future__ import annotations

import asyncio
from typing import Awaitable, Callable


class Scheduler:
    def __init__(self) -> None:
        self._sem = asyncio.Semaphore(32)

    async def run(self, coro: Awaitable):
        async with self._sem:
            return await coro

    async def gather(self, *coros: Awaitable):
        return await asyncio.gather(*[self.run(c) for c in coros])
