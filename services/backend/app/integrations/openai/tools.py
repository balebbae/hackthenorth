from typing import Literal
from pydantic import Field
from ...models import Model


class SearchArgs(Model):
    query: str = Field(min_length=1, max_length=2000)


class EmptyArgs(Model):
    pass


class DestinationArgs(Model):
    destination_id: str = Field(min_length=1)
    accessible_only: bool


class EventArgs(Model):
    event_type: Literal['obstacle', 'destination_set', 'route_generated', 'arrived',
        'localization_acquired', 'localization_lost', 'assistant_query', 'assistant_action'] | None
    minutes: int = Field(ge=1, le=1440)


REGISTRY = {
    'search_building_knowledge': (SearchArgs, 'Search site building documents with hybrid retrieval; static evidence.'),
    'search_places': (SearchArgs, 'Search real mapped places, with backend distances where localized.'),
    'get_current_location': (EmptyArgs, 'Read current localization, pose, nearest waypoint and nearby entities.'),
    'get_navigation_state': (EmptyArgs, 'Read the current deterministic route, next waypoint and instruction.'),
    'set_destination': (DestinationArgs, 'Start deterministic navigation to an existing destination only when requested.'),
    'get_recent_events': (EventArgs, 'Read session event history; null type includes all event types.'),
}
TOOLS = [{'type': 'function', 'name': name, 'description': description,
          'parameters': model.model_json_schema(), 'strict': True}
         for name, (model, description) in REGISTRY.items()]
