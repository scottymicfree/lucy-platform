from __future__ import annotations

from backend.NodeMesh.node import Node


class NodeManager:
    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}

    def register(self, node: Node) -> None:
        self.nodes[node.node_id] = node

    def is_registered(self, node_id: str) -> bool:
        return node_id in self.nodes
