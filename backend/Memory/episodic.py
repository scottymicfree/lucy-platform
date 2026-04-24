from __future__ import annotations

import json
import os
from typing import Any


class EpisodicStore:
    def __init__(self, data_dir: str) -> None:
        self.path = os.path.join(data_dir, "episodic.jsonl")
        os.makedirs(data_dir, exist_ok=True)

    def append(self, record: dict[str, Any]) -> None:
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
