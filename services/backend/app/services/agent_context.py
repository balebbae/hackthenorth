from typing import Any
from pydantic import BaseModel


class AgentContext(BaseModel):
    session: dict[str, str]
    localization: dict[str, Any]
    pose: dict | None
    navigation: dict
    obstacle_state: dict
    localization_context: dict


class AgentContextBuilder:
    def __init__(self, store, localization_context=None):
        self.store = store
        # Operator-supplied descriptions of map alignment, anchors, provider semantics.
        # Provider metadata received from clients stays nested in localization.
        self.localization_context = localization_context or {}

    async def build(self, session_id: str) -> AgentContext:
        state = self.store.get(session_id).snapshot()
        return AgentContext(session={'session_id': state['session_id'], 'site_id': state['site_id']},
            localization=state['localization'], pose=state['pose'], navigation=state['navigation'],
            obstacle_state=state['obstacle_state'], localization_context=self.localization_context)
