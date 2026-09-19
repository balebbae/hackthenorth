import heapq
from .graph import Graph, distance


def astar(graph: Graph, start: str, goal: str, accessible_only: bool = True) -> list[str]:
    points = {w.id: w for w in graph.waypoints}
    if start not in points or goal not in points:
        raise ValueError('Unknown waypoint')
    adjacency = {w: [] for w in points}
    for edge in graph.edges:
        if accessible_only and not edge.accessible:
            continue
        adjacency[edge.source].append(edge.target)
        if edge.bidirectional:
            adjacency[edge.target].append(edge.source)
    queue = [(0.0, start)]
    cost, parent = {start: 0.0}, {}
    while queue:
        _, current = heapq.heappop(queue)
        if current == goal:
            path = [goal]
            while path[-1] != start:
                path.append(parent[path[-1]])
            return path[::-1]
        for neighbor in adjacency[current]:
            candidate = cost[current] + distance(points[current], points[neighbor])
            if candidate < cost.get(neighbor, float('inf')):
                cost[neighbor], parent[neighbor] = candidate, current
                heapq.heappush(queue, (candidate + distance(points[neighbor], points[goal]), neighbor))
    raise ValueError('Destination is disconnected under the selected accessibility constraint')
