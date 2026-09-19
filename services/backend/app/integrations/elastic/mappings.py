def mappings(dims: int) -> dict:
    common = {'id': {'type': 'keyword'}, 'site_id': {'type': 'keyword'}}
    searchable = {**common, 'title': {'type': 'text'}, 'text': {'type': 'text'},
                  'embedding': {'type': 'dense_vector', 'dims': dims, 'index': True, 'similarity': 'cosine'}}
    return {
        'building_knowledge': {'properties': {**searchable, 'document_id': {'type': 'keyword'}}},
        'map_entities': {'properties': {**searchable, 'name': {'type': 'text'}, 'aliases': {'type': 'text'},
            'entity_type': {'type': 'keyword'}, 'waypoint_id': {'type': 'keyword'},
            'description': {'type': 'text'}, 'tags': {'type': 'keyword'}, 'floor': {'type': 'integer'},
            'x': {'type': 'float'}, 'y': {'type': 'float'}, 'z': {'type': 'float'}}},
        'live_events': {'properties': {**common, 'session_id': {'type': 'keyword'},
            'event_type': {'type': 'keyword'}, 'timestamp': {'type': 'date'},
            'summary': {'type': 'text'}, 'data': {'type': 'object', 'enabled': False}}},
    }
