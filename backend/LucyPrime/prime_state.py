from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PrimeState:
    state: str = "idle"  # idle|thinking|synthesizing|responding
