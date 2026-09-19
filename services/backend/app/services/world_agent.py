"""Keep the OpenAI tool loop grounded in the current persisted world manifest."""
from fastapi import HTTPException
from ..models import Pose, Localization
from ..integrations.openai.tools import REGISTRY
from ..routing.heading import horizontal, legacy_heading, yaw
from .sessions import Session
from .worlds import world_graph, compute_route


class WorldAgentTools:
    def __init__(self, fallback, worlds, navigation, memory):
        self.fallback, self.worlds, self.navigation, self.memory = fallback, worlds, navigation, memory
        self.events = fallback.events

    def exists(self, session_id):
        return self.worlds.path('sessions', session_id + '.json').is_file()

    def refresh(self, session_id):
        if not self.exists(session_id):
            return
        data = self.worlds.session(session_id)
        if data['state'] == 'ended':
            raise ValueError('Session ended')
        session = self.memory.sessions.setdefault(session_id, Session(session_id, data['worldId']))
        session.destination_id = data.get('destination')
        session.route = [n['id'] for n in data.get('route', {}).get('nodes', [])]
        meta = self.navigation.metadata(session_id)
        session.route_index = meta.get('leg', 0)
        progress = data.get('lastProgress', {})
        session.instruction = progress.get('instruction', {}).get('text')
        session.distance_remaining_m = progress.get('remainingMetres')
        if 'lastPose' in data:
            point = data['lastPose']['position']
            facing = yaw(data['lastPose']['rotation'])
            session.pose = Pose(x=point[0], y=point[1], z=point[2],
                heading=legacy_heading(facing) if facing is not None else 0,
                localized=data['state'] not in ('lost', 'ended'), timestamp=meta.get('timestamp', 0),
                localization=Localization(provider='niantic', coordinate_frame='world',
                    provider_metadata={'heading_convention': 'legacy contract 0=+Z, converted from world heading 0=-Z',
                                       'world_heading_deg': facing}))

    async def execute(self, session, name, arguments):
        if not self.exists(session.session_id):
            return await self.fallback.execute(session, name, arguments)
        if name not in REGISTRY:
            raise ValueError('Unknown tool')
        args = REGISTRY[name][0].model_validate_json(arguments, strict=True)
        data = self.worlds.session(session.session_id)
        world = self.worlds.world(data['worldId'])
        nodes = {n['id']: n for n in world_graph(world)['nodes']}
        sources, actions = [], []
        localized = session.snapshot()['localization']['localized']
        if name == 'get_current_location':
            nearest = min(nodes.values(), key=lambda n: horizontal(n['position'], data['lastPose']['position'])) if localized and nodes else None
            result = {'pose': data.get('lastPose') if localized else None, 'localized': localized,
                      'frame': 'world', 'nearestNode': nearest}
        elif name == 'get_navigation_state':
            result = {'state': data['state'], 'destination': data.get('destination'),
                      'route': data.get('route'), 'progress': data.get('lastProgress'),
                      'localized': localized}
        elif name == 'search_places':
            near = None
            if localized:
                position = data['lastPose']['position']
                near = {'x': position[0], 'y': position[1], 'z': position[2]}
            hits = await self.fallback.search.search('map_entities', data['worldId'], args.query, near=near)
            result = []
            for hit in hits:
                if hit['id'] not in nodes:
                    continue
                node = nodes[hit['id']]
                record = {**node, 'route_distance_m': None}
                if localized:
                    try:
                        route = compute_route(world, self.navigation.route_request(data['lastPose'], node['id']))
                        record['route_distance_m'] = route['totalMetres']
                    except HTTPException:
                        record['unreachable'] = True
                # Metadata is evidence, never an alternative source for graph coordinates.
                record['description'] = hit.get('description', '')
                record['tags'] = hit.get('tags', [])
                result.append(record)
                sources.append({'type': 'map_entity', 'id': node['id']})
        elif name == 'set_destination':
            if not localized:
                raise ValueError('A fresh localized pose is required before navigation')
            if args.accessible_only:
                raise ValueError('This world contract has no edge accessibility metadata; cannot verify a step-free route. Ask before using an unverified route.')
            result = await self.navigation.destination(session.session_id, args.destination_id)
            self.refresh(session.session_id)
            actions.append({'type': 'set_destination', 'destination_id': args.destination_id, 'accessible_only': False})
            sources.append({'type': 'map_entity', 'id': args.destination_id})
        else:
            return await self.fallback.execute(session, name, arguments)
        return {'data': result, 'sources': sources, 'actions': actions}
