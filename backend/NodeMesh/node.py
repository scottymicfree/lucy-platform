from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    node_id: str
    description: str = ""
