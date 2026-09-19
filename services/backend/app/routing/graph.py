import json
from math import dist
from pathlib import Path
from pydantic import model_validator
from ..models import Model, Waypoint, Edge, Destination, Point


def distance(a: Point, b: Point) -> float:
    return dist((a.x, a.y, a.z), (b.x, b.y, b.z))


class Graph(Model):
    site_id: str
    coordinate_frame: str = 'site'
    waypoints: list[Waypoint]
    edges: list[Edge]
    destinations: list[Destination]

    @model_validator(mode='after')
    def validate_graph(self):
        ids = {w.id for w in self.waypoints}
        if not ids or len(ids) != len(self.waypoints):
            raise ValueError('Waypoints must be nonempty and unique')
        if len({d.id for d in self.destinations}) != len(self.destinations):
            raise ValueError('Duplicate destination IDs')
        if any(e.source not in ids or e.target not in ids or e.source == e.target for e in self.edges):
            raise ValueError('Invalid edge endpoint')
        if any(d.waypoint_id not in ids for d in self.destinations):
            raise ValueError('Invalid destination waypoint')
        return self

    @classmethod
    def load(cls, path: Path):
        return cls.model_validate(json.loads(path.read_text(encoding='utf-8')))

    def point(self, waypoint_id: str) -> Waypoint:
        return next(w for w in self.waypoints if w.id == waypoint_id)

    def destination(self, destination_id: str) -> Destination:
        for d in self.destinations:
            if d.id == destination_id:
                return d
        raise ValueError('Unknown destination')

    def nearest(self, pose: Point) -> Waypoint:
        return min(self.waypoints, key=lambda w: distance(w, pose))
