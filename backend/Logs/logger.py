from __future__ import annotations

import json
import os
from typing import Any


class JsonLogger:
    def __init__(self, log_dir: str, level: str = "INFO") -> None:
        self.log_dir = log_dir
        self.level = level
        os.makedirs(log_dir, exist_ok=True)
        self.path = os.path.join(log_dir, "lucy.jsonl")

    def write(self, record: dict[str, Any]) -> None:
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
