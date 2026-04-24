from __future__ import annotations

from backend.LittleLucys.lucy3_3 import Lucy33
from backend.LittleLucys.lucy3_ai_os import Lucy3AIOS
from backend.LittleLucys.lucy3_base import Lucy3Base
from backend.LittleLucys.lucy_3_eve import Lucy3Eve


def get_agent(agent_id: str):
    mapping = {
        "lucy3_base": Lucy3Base,
        "lucy_3_eve": Lucy3Eve,
        "lucy3_ai_os": Lucy3AIOS,
        "lucy3_3": Lucy33,
    }
    return mapping[agent_id]()
