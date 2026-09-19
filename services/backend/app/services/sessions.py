import asyncio
import time
from dataclasses import dataclass, field
from typing import Protocol
from uuid import uuid4
from ..models import Pose, Obstacle
from ..routing.graph import Graph, distance
from ..routing.astar import astar
from ..routing.navigation import progress


@dataclass
class Session:
    session_id: str
    site_id: str
    pose: Pose | None = None
    destination_id: str | None = None
    route: list[str] = field(default_factory=list)
    route_index: int = 0
    instruction: str | None = None
    distance_remaining_m: float | None = None
    obstacles: dict = field(default_factory=dict)
    history: list = field(default_factory=list)
    sockets: set = field(default_factory=set)
    agent_lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    def snapshot(self):
        fresh = self.pose is not None and time.time() - self.pose.timestamp <= 15
        localized = bool(fresh and self.pose.localized)
        return {
            'session_id': self.session_id, 'site_id': self.site_id,
            'pose': self.pose.model_dump() if self.pose else None,
            'localization': {**(self.pose.localization.model_dump() if self.pose else {}),
                             'localized': localized, 'stale': not fresh},
            'navigation': {
                'destination_id': self.destination_id, 'route': self.route,
                'route_index': self.route_index,
                'next_waypoint_id': self.route[self.route_index] if self.route_index < len(self.route) else None,
                'instruction': self.instruction if localized else None,
                'distance_remaining_m': self.distance_remaining_m if localized else None,
            },
            'obstacle_state': {d: o.model_dump() if (o := self.obstacles.get(d)) and time.time() - o.timestamp <= 5 else None
                               for d in ('front', 'left', 'right', 'back')},
        }


class SessionStore(Protocol):
    def create(self, site_id: str) -> Session: ...
    def get(self, session_id: str) -> Session: ...


class MemorySessionStore:
    def __init__(self):
        self.sessions: dict[str, Session] = {}

    def create(self, site_id):
        session = Session(str(uuid4()), site_id)
        self.sessions[session.session_id] = session
        return session

    def get(self, session_id):
        if session_id not in self.sessions:
            raise KeyError('Session not found')
        return self.sessions[session_id]


class NavigationService:
    def __init__(self, graph: Graph, store: SessionStore):
        self.graph, self.store = graph, store

    def create(self, site_id):
        if site_id != self.graph.site_id:
            raise ValueError('Unknown site')
        return self.store.create(site_id)

    def update_pose(self, session: Session, pose: Pose):
        if pose.localization.coordinate_frame != self.graph.coordinate_frame:
            raise ValueError('Pose coordinate frame does not match graph')
        if pose.timestamp > time.time() + 5 or time.time() - pose.timestamp > 15:
            raise ValueError('Pose timestamp must be current (15s maximum age, 5s clock skew)')
        if session.pose and pose.timestamp <= session.pose.timestamp:
            raise ValueError('Out-of-order pose')
        session.pose = pose
        self.advance(session)

    def advance(self, session):
        session.route_index, session.instruction, session.distance_remaining_m = progress(
            self.graph, session.pose, session.route, session.route_index)

    def set_destination(self, session, destination_id, accessible_only=True):
        destination = self.graph.destination(destination_id)
        if not session.snapshot()['localization']['localized']:
            raise ValueError('A fresh localized pose is required before navigation')
        start = self.graph.nearest(session.pose)
        if distance(start, session.pose) > 3:
            raise ValueError('Pose is too far from the mapped waypoint network')
        route = astar(self.graph, start.id, destination.waypoint_id, accessible_only)
        session.destination_id, session.route, session.route_index = destination_id, route, 0
        self.advance(session)
        return session.snapshot()['navigation']

    def obstacle(self, session, obstacle: Obstacle):
        if abs(time.time() - obstacle.timestamp) > 5:
            raise ValueError('Obstacle timestamp must be current')
        previous = session.obstacles.get(obstacle.direction)
        if previous and obstacle.timestamp <= previous.timestamp:
            raise ValueError('Out-of-order obstacle')
        session.obstacles[obstacle.direction] = obstacle


async def broadcast(session: Session, message: dict):
    async def send(socket):
        try:
            await asyncio.wait_for(socket.send_json(message), timeout=2)
        except Exception:
            session.sockets.discard(socket)
    await asyncio.gather(*(send(socket) for socket in tuple(session.sockets)))
