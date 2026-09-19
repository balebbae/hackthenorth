"""Persistent implementation of the world/navigation contracts from main."""
import asyncio
import hashlib
import heapq
import json
import logging
import math
import re
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from ..config import ROOT

logger = logging.getLogger(__name__)
BASE = 'https://wander.app/contracts/'
SCHEMAS = {name: json.loads((ROOT / 'shared/contracts' / name).read_text(encoding='utf-8'))
           for name in ('world.schema.json', 'navigation.schema.json', 'measurements.schema.json',
                        'notes.schema.json')}
REGISTRY = Registry().with_resources([(BASE + name, Resource.from_contents(schema))
                                      for name, schema in SCHEMAS.items()])


def now():
    return datetime.now(timezone.utc).isoformat()


def check(value, schema, pointer=''):
    validator = Draft202012Validator({'$ref': BASE + schema + pointer}, registry=REGISTRY,
                                     format_checker=FormatChecker())
    errors = list(validator.iter_errors(value))
    if errors:
        raise HTTPException(400, errors[0].message)
    def finite(item):
        if isinstance(item, float) and not math.isfinite(item):
            raise HTTPException(400, 'Nonfinite numbers are not allowed')
        if isinstance(item, dict):
            for key, child in item.items():
                finite(child)
                if key == 'rotation' and isinstance(child, list):
                    if abs(sum(x*x for x in child) - 1) > 0.001:
                        raise HTTPException(400, 'Rotation must be a unit quaternion [x,y,z,w]')
        elif isinstance(item, list):
            for child in item:
                finite(child)
    finite(value)
    return value


def segment(value):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', value) or '..' in value:
        raise HTTPException(400, 'Invalid path identifier')
    return value


def rotate(point, quaternion):
    x, y, z, w = quaternion
    a, b, c = point
    tx, ty, tz = 2*(y*c-z*b), 2*(z*a-x*c), 2*(x*b-y*a)
    return [a+w*tx+y*tz-z*ty, b+w*ty+z*tx-x*tz, c+w*tz+x*ty-y*tx]


def world_graph(world):
    graph = deepcopy(world.get('navigationGraph', {'nodes': [], 'edges': []}))
    if graph.get('frame', 'world') == 'splat':
        alignment = world.get('alignment')
        if not alignment:
            raise HTTPException(409, 'Splat graph requires alignment')
        for node in graph['nodes']:
            rotated = rotate([v * alignment['scale'] for v in node['position']], alignment['rotation'])
            node['position'] = [a+b for a, b in zip(rotated, alignment['position'])]
        # Explicit distances are already specified in metres by the contract.
    return graph


def validate_graph(graph):
    check(graph, 'world.schema.json', '#/properties/navigationGraph')
    ids = [node['id'] for node in graph['nodes']]
    if len(set(ids)) != len(ids):
        raise HTTPException(400, 'Duplicate node IDs')
    if any(e['from'] not in ids or e['to'] not in ids or e['from'] == e['to'] for e in graph['edges']):
        raise HTTPException(400, 'Invalid graph edge')


def projection(point, a, b):
    delta = [y-x for x, y in zip(a, b)]
    denominator = sum(x*x for x in delta)
    t = max(0, min(1, sum((x-y)*d for x, y, d in zip(point, a, delta))/denominator)) if denominator else 0
    projected = [x+t*d for x, d in zip(a, delta)]
    return math.dist(point, projected), projected, t


def snap(graph, position, avoid=()):
    nodes = {n['id']: n for n in graph['nodes'] if n['id'] not in avoid}
    if not nodes:
        raise HTTPException(409, 'World has no usable navigation nodes')
    nearest = min(nodes.values(), key=lambda n: math.dist(position, n['position']))
    options = []
    for edge in graph['edges']:
        if edge['from'] in nodes and edge['to'] in nodes:
            d, p, t = projection(position, nodes[edge['from']]['position'], nodes[edge['to']]['position'])
            options.append((d, p, t, edge))
    # Isolated nodes remain valid starts when closer than any edge.
    fallback = (math.dist(position, nearest['position']), nearest['position'], 0, None)
    choice = min(options, key=lambda item: item[0]) if options else fallback
    if fallback[0] < choice[0]:
        choice = fallback
    return nearest, choice


def heading(a, b):
    return math.degrees(math.atan2(b[0]-a[0], -(b[2]-a[2]))) % 360


def node_ref(node):
    return {k: v for k, v in node.items() if k in ('id', 'name', 'kind', 'position')}


def compute_route(world, request):
    check(request, 'navigation.schema.json', '#/$defs/routeRequest')
    graph = world_graph(world)
    nodes = {n['id']: node_ref(n) for n in graph['nodes']}
    destination, start = request['to'], request.get('from')
    if destination not in nodes:
        raise HTTPException(404, 'Destination node not found')
    if start is None:
        raise HTTPException(400, 'Specify from; a world route has no implicit session')
    avoid = set(request.get('avoid', []))
    if destination in avoid:
        raise HTTPException(422, 'Destination is avoided')
    adjacency = {key: [] for key in nodes}
    for edge in graph['edges']:
        a, b = edge['from'], edge['to']
        if a in avoid or b in avoid:
            continue
        weight = edge.get('distance', math.dist(nodes[a]['position'], nodes[b]['position']))
        adjacency[a].append((b, weight))
        if edge.get('bidirectional', True):
            adjacency[b].append((a, weight))
    if isinstance(start, list):
        nearest, (_, point, t, edge) = snap(graph, start, avoid)
        if edge is None:
            start = nearest['id']
        elif t <= 1e-9:
            start = edge['from']
        elif t >= 1-1e-9:
            start = edge['to']
        else:
            start = 'start-' + uuid4().hex
            nodes[start] = {'id': start, 'position': point, 'kind': 'waypoint'}
            weight = edge.get('distance', math.dist(nodes[edge['from']]['position'], nodes[edge['to']]['position']))
            adjacency[start] = [(edge['to'], weight*(1-t))]
            if edge.get('bidirectional', True):
                adjacency[start].append((edge['from'], weight*t))
    if start not in nodes:
        raise HTTPException(404, 'Start node not found')
    if start in avoid:
        raise HTTPException(422, 'Start is avoided')
    costs, previous, queue = {start: 0}, {}, [(0, start)]
    while queue:
        cost, current = heapq.heappop(queue)
        if cost != costs[current]:
            continue
        if current == destination:
            break
        for target, weight in adjacency[current]:
            if cost+weight < costs.get(target, float('inf')):
                costs[target] = cost+weight
                previous[target] = (current, weight)
                heapq.heappush(queue, (cost+weight, target))
    if destination not in costs:
        raise HTTPException(422, 'Destination unreachable')
    path = [destination]
    while path[-1] != start:
        path.append(previous[path[-1]][0])
    path.reverse()
    legs = [{'from': a, 'to': b, 'distanceMetres': previous[b][1],
             'headingDeg': heading(nodes[a]['position'], nodes[b]['position'])} for a, b in zip(path, path[1:])]
    for i, leg in enumerate(legs):
        if math.dist(nodes[leg['from']]['position'], nodes[leg['to']]['position']) < 1e-9:
            leg['headingDeg'] = legs[i-1]['headingDeg'] if i else 0
    instructions = []
    for i, leg in enumerate(legs):
        angle = (leg['headingDeg']-legs[i-1]['headingDeg']+180) % 360-180 if i else 0
        magnitude = abs(angle)
        turn = ('straight' if magnitude < 20 else 'u-turn' if magnitude >= 160 else
                ('slight-' if magnitude < 45 else 'sharp-' if magnitude > 120 else '') +
                ('right' if angle > 0 else 'left'))
        instructions.append({'atNode': leg['from'], 'turn': turn,
            'text': f"{turn.replace('-', ' ').capitalize()}; continue {leg['distanceMetres']:.1f} metres.",
            'distanceMetres': legs[i-1]['distanceMetres'] if i else 0})
    instructions.append({'atNode': destination, 'turn': 'arrive', 'text': 'You have arrived.',
                         'distanceMetres': legs[-1]['distanceMetres'] if legs else 0})
    return {'nodes': [nodes[key] for key in path], 'legs': legs,
            'totalMetres': costs[destination], 'instructions': instructions}


class WorldStore:
    def __init__(self, root: Path, commit=None):
        self.root = root.resolve()
        self.commit = commit
        self.locks = {}
        self.sockets = {}

    def lock(self, key):
        return self.locks.setdefault(key, asyncio.Lock())

    def path(self, *parts):
        path = self.root
        for part in parts:
            path = path / segment(part)
            if path.is_symlink():
                raise HTTPException(400, 'Symlink paths are not allowed')
        if not path.resolve().is_relative_to(self.root):
            raise HTTPException(400, 'Invalid storage path')
        return path

    def read(self, *parts):
        path = self.path(*parts)
        try:
            return json.loads(path.read_text(encoding='utf-8'))
        except FileNotFoundError:
            raise HTTPException(404, 'Not found')

    async def write(self, value, *parts):
        path = self.path(*parts)
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name('tmp-' + uuid4().hex)
        try:
            temporary.write_text(json.dumps(value, ensure_ascii=False, allow_nan=False), encoding='utf-8')
            temporary.replace(path)
            await self.flush()
        finally:
            temporary.unlink(missing_ok=True)

    async def write_bytes(self, data, *parts):
        path = self.path(*parts)
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name('tmp-' + uuid4().hex)
        try:
            temporary.write_bytes(data)
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)

    async def flush(self):
        if self.commit:
            await asyncio.to_thread(self.commit)

    def world(self, world_id):
        world = check(self.read('worlds', world_id, 'world.json'), 'world.schema.json')
        if world['id'] != world_id:
            raise HTTPException(400, 'Manifest ID differs from its directory')
        validate_graph(world.get('navigationGraph', {'nodes': [], 'edges': []}))
        return world

    def session(self, session_id):
        return check(self.read('sessions', session_id + '.json'), 'navigation.schema.json', '#/$defs/session')

    async def save_session(self, session):
        check(session, 'navigation.schema.json', '#/$defs/session')
        await self.write(session, 'sessions', session['sessionId'] + '.json')

    async def emit(self, session, kind):
        event = {'type': kind, 'sessionId': session['sessionId'], 'timestamp': now()}
        for source, target in [('lastPose', 'pose'), ('lastProgress', 'progress'), ('route', 'route')]:
            if source in session:
                event[target] = session[source]
        async def send(socket):
            try:
                await asyncio.wait_for(socket.send_json(event), 2)
            except Exception:
                self.sockets.get(session['sessionId'], set()).discard(socket)
        await asyncio.gather(*(send(socket) for socket in tuple(self.sockets.get(session['sessionId'], ()))))
        return event


class WorldNavigation:
    def __init__(self, store):
        self.store = store

    def metadata(self, session_id):
        try:
            return self.store.read('sessions', session_id + '-state.json')
        except HTTPException as error:
            if error.status_code != 404:
                raise
            return {}

    async def create(self, world_id, device_id, destination=None):
        world = self.store.world(world_id)
        if destination is not None and destination not in {n['id'] for n in world_graph(world)['nodes']}:
            raise HTTPException(404, 'Destination node not found')
        session = {'sessionId': str(uuid4()), 'worldId': world_id, 'deviceId': device_id,
                   'state': 'localizing', 'createdAt': now(), 'updatedAt': now()}
        if destination is not None:
            session['destination'] = destination
        await self.store.save_session(session)
        return session

    def ensure_active(self, session):
        if session['state'] == 'ended':
            raise HTTPException(409, 'Session ended')

    async def destination(self, session_id, destination):
        async with self.store.lock('session:' + session_id):
            session = self.store.session(session_id)
            self.ensure_active(session)
            world = self.store.world(session['worldId'])
            if destination not in {n['id'] for n in world_graph(world)['nodes']}:
                raise HTTPException(404, 'Destination node not found')
            if 'lastPose' in session and session['state'] != 'lost':
                session['route'] = compute_route(world, {'from': session['lastPose']['position'], 'to': destination})
                session['state'] = 'navigating'
            else:
                session.pop('route', None)
            session['destination'] = destination
            session.pop('lastProgress', None)
            session['updatedAt'] = now()
            meta = self.metadata(session_id)
            meta.update(leg=0, off_since=None, graph_hash=self.graph_hash(world))
            await self.store.write(meta, 'sessions', session_id + '-state.json')
            await self.store.save_session(session)
            await self.store.emit(session, 'rerouted')
            return session

    @staticmethod
    def graph_hash(world):
        return hashlib.sha256(json.dumps(world_graph(world), sort_keys=True).encode()).hexdigest()

    async def pose(self, session_id, body, allow_no_destination=False):
        check(body, 'navigation.schema.json', '#/$defs/poseUpdate')
        async with self.store.lock('session:' + session_id):
            session = self.store.session(session_id)
            self.ensure_active(session)
            if 'destination' not in session and not allow_no_destination:
                raise HTTPException(409, 'Session has no destination yet')
            timestamp = datetime.fromisoformat(body['timestamp'].replace('Z', '+00:00')).timestamp()
            age = datetime.now(timezone.utc).timestamp()-timestamp
            if age > 15 or age < -5:
                raise HTTPException(400, 'Pose timestamp is stale or in the future')
            meta = self.metadata(session_id)
            if timestamp <= meta.get('timestamp', 0):
                raise HTTPException(400, 'Out-of-order pose')
            meta['timestamp'] = timestamp
            session['lastPose'], session['updatedAt'] = body['pose'], now()
            world = self.store.world(session['worldId'])
            rerouted = False
            if body.get('trackingState', 'localized') != 'localized':
                was_lost = session['state'] == 'lost'
                session['state'] = 'lost'
                progress = {'state': 'lost', 'remainingMetres': 0}
                if not was_lost:
                    progress['speak'] = 'Tracking lost. Navigation paused.'
                meta['off_since'] = None
            elif 'destination' not in session:
                session['state'] = 'localizing'
                progress = {'state': 'localizing', 'remainingMetres': 0}
            else:
                changed = meta.get('graph_hash') != self.graph_hash(world)
                if changed or 'route' not in session or session['state'] == 'lost':
                    session['route'] = compute_route(world, {'from': body['pose']['position'], 'to': session['destination']})
                    meta.update(leg=0, off_since=None, graph_hash=self.graph_hash(world))
                    rerouted = True
                route = session['route']
                position = body['pose']['position']
                legs, nodes = route['legs'], route['nodes']
                index = min(meta.get('leg', 0), max(0, len(legs)-1))
                # Advance only along adjacent legs; do not jump across a looping path.
                while index < len(legs)-1 and math.dist(position, nodes[index+1]['position']) < 1.5:
                    index += 1
                meta['leg'] = index
                if legs:
                    off, _, fraction = projection(position, nodes[index]['position'], nodes[index+1]['position'])
                    off_all = min(projection(position, a['position'], b['position'])[0]
                                  for a, b in zip(nodes, nodes[1:]))
                    remaining = (1-fraction)*legs[index]['distanceMetres'] + sum(l['distanceMetres'] for l in legs[index+1:])
                else:
                    off = off_all = math.dist(position, nodes[-1]['position'])
                    remaining = off
                arrived = math.dist(position, nodes[-1]['position']) < 1.5 and index == max(0, len(legs)-1)
                state = 'arrived' if arrived else 'off-route' if off_all > 3 else 'navigating'
                if state == 'off-route':
                    meta['off_since'] = meta.get('off_since') or timestamp
                    if timestamp-meta['off_since'] >= 5:
                        session['route'] = compute_route(world, {'from': position, 'to': session['destination']})
                        meta.update(leg=0, off_since=timestamp)
                        rerouted = True
                        route = session['route']
                        nodes, legs = route['nodes'], route['legs']
                        index, remaining = 0, route['totalMetres']
                else:
                    meta['off_since'] = None
                cue = route['instructions'][-1] if arrived else route['instructions'][index]
                progress = {'state': state, 'remainingMetres': max(0, remaining),
                    'offRouteMetres': off_all, 'instruction': cue,
                    'nextNode': nodes[min(index+1, len(nodes)-1)],
                    'distanceToNextMetres': math.dist(position, nodes[min(index+1, len(nodes)-1)]['position'])}
                cue_id = (state, cue['atNode'], cue['turn'])
                if list(cue_id) != meta.get('last_cue'):
                    progress['speak'] = ('You are off route. Recalculating.' if state == 'off-route' else cue['text'])
                    meta['last_cue'] = list(cue_id)
                session['state'] = state
            session['lastProgress'] = progress
            await self.store.write(meta, 'sessions', session_id + '-state.json')
            await self.store.save_session(session)
            if rerouted:
                await self.store.emit(session, 'rerouted')
            await self.store.emit(session, 'progress')
            if session['state'] in ('lost', 'arrived'):
                await self.store.emit(session, session['state'])
            return progress
