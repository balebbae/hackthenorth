from math import atan2, degrees
from .graph import Graph, distance
from ..models import Pose


def instruction(pose: Pose, target) -> str:
    bearing = degrees(atan2(target.x - pose.x, target.z - pose.z)) % 360
    delta = (bearing - pose.heading + 180) % 360 - 180
    if abs(delta) < 25:
        return 'continue'
    if abs(delta) >= 150:
        return 'turn_around'
    return 'turn_right' if delta > 0 else 'turn_left'


def progress(graph: Graph, pose: Pose | None, route: list[str], index: int):
    if not route or pose is None or not pose.localized:
        return index, None, None
    if index == len(route) and distance(pose, graph.point(route[-1])) > 0.65:
        index -= 1
    while index < len(route) and distance(pose, graph.point(route[index])) <= 0.65:
        index += 1
    if index == len(route):
        return index, 'arrived', 0.0
    remaining = distance(pose, graph.point(route[index]))
    remaining += sum(distance(graph.point(a), graph.point(b)) for a, b in zip(route[index:], route[index + 1:]))
    return index, instruction(pose, graph.point(route[index])), round(remaining, 2)
