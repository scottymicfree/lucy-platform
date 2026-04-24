from __future__ import annotations

import time
import uuid
from typing import Any


def now_ms() -> int:
    return int(time.time() * 1000)


def new_id(prefix: str | None = None) -> str:
    uid = str(uuid.uuid4())
    return f"{prefix}_{uid}" if prefix else uid


def ensure_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]
