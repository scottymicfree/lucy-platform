from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Dag:
    nodes: list[str]
    edges: list[tuple[str, str]]


class DagBuilder:
    def build_default(self) -> Dag:
        nodes = [
            "P_PERCEPTION",
            "M_RETRIEVER",
            "E_ROUTER",
            "L_SWARM",
            "E_MERGE",
            "LP_SYNTH",
            "O_TEXT",
        ]
        edges = list(zip(nodes, nodes[1:]))
        return Dag(nodes=nodes, edges=edges)
