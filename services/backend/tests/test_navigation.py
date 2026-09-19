import time
import pytest
from ..app.models import Pose, Point, Obstacle
from ..app.routing.graph import Graph
from ..app.routing.astar import astar
from ..app.routing.navigation import instruction, progress


@pytest.mark.parametrize('mutation', ['duplicate', 'bad_edge', 'bad_destination', 'empty', 'nan'])
def test_graph_validation(graph, mutation):
    data = graph.model_dump()
    if mutation == 'duplicate':
        data['waypoints'].append(data['waypoints'][0])
    elif mutation == 'bad_edge':
        data['edges'][0]['target'] = 'invented'
    elif mutation == 'bad_destination':
        data['destinations'][0]['waypoint_id'] = 'invented'
    elif mutation == 'empty':
        data['waypoints'] = []
    else:
        data['waypoints'][0]['x'] = float('nan')
    with pytest.raises(ValueError):
        Graph.model_validate(data)


def test_nearest_and_shortest_path(graph):
    assert graph.nearest(Point(x=3.8, y=0, z=8)).id == 'east_elevator'
    assert astar(graph, 'entrance', 'east_elevator') == ['entrance', 'hall_corner', 'east_elevator']
    assert astar(graph, 'entrance', 'entrance') == ['entrance']
    with pytest.raises(ValueError):
        astar(graph, 'entrance', 'stairs')
    assert astar(graph, 'entrance', 'stairs', False)[-1] == 'stairs'


def test_disconnected_and_invalid(graph):
    graph.edges = [e for e in graph.edges if 'east_elevator' not in (e.source, e.target)]
    with pytest.raises(ValueError, match='disconnected'):
        astar(graph, 'entrance', 'east_elevator')
    with pytest.raises(ValueError, match='Unknown'):
        astar(graph, 'entrance', 'fake')


@pytest.mark.parametrize('heading,expected', [(0, 'continue'), (90, 'turn_left'), (270, 'turn_right'), (180, 'turn_around')])
def test_turns(pose, heading, expected):
    pose.heading = heading
    assert instruction(pose, Point(x=0, y=0, z=8)) == expected


def test_progress_and_no_shortcuts(graph, pose):
    route = ['entrance', 'hall_corner', 'east_elevator']
    assert progress(graph, pose, route, 0) == (1, 'continue', 12)
    pose.z = 8
    assert progress(graph, pose, route, 1) == (2, 'turn_right', 4)
    pose.x = 4
    assert progress(graph, pose, route, 2) == (3, 'arrived', 0)
    # Teleporting to the end must not skip an unvisited corner.
    assert progress(graph, pose, route, 1)[1] != 'arrived'
    pose.localized = False
    assert progress(graph, pose, route, 1) == (1, None, None)


def test_session_isolation(navigation, pose):
    one, two = navigation.create('demo_building'), navigation.create('demo_building')
    navigation.update_pose(one, pose)
    navigation.set_destination(one, 'east_elevator')
    assert one.distance_remaining_m == 12
    assert two.pose is None and two.route == [] and two.history == []
    with pytest.raises(ValueError):
        navigation.set_destination(one, 'invented')
    assert one.destination_id == 'east_elevator'
    with pytest.raises(ValueError):
        navigation.set_destination(two, 'east_elevator')
    with pytest.raises(ValueError):
        navigation.create('unknown')


def test_localization_guards(navigation, pose):
    session = navigation.create('demo_building')
    navigation.update_pose(session, pose)
    with pytest.raises(ValueError, match='Out-of-order'):
        navigation.update_pose(session, pose)
    pose2 = pose.model_copy(deep=True)
    pose2.timestamp += .01
    pose2.localization.coordinate_frame = 'camera'
    with pytest.raises(ValueError, match='frame'):
        navigation.update_pose(session, pose2)
    session.pose.timestamp = time.time() - 60
    assert session.snapshot()['localization']['localized'] is False
    with pytest.raises(ValueError, match='fresh'):
        navigation.set_destination(session, 'east_elevator')


def test_obstacles_expire(navigation):
    session = navigation.create('demo_building')
    obstacle = Obstacle(direction='front', distance_m=1, description='chair', timestamp=time.time())
    navigation.obstacle(session, obstacle)
    assert session.snapshot()['obstacle_state']['front']['description'] == 'chair'
    obstacle.timestamp -= 10
    assert session.snapshot()['obstacle_state']['front'] is None


def test_astar_chooses_shorter_of_competing_paths():
    graph = Graph.model_validate({'site_id': 's', 'waypoints': [
        {'id': 'a', 'x': 0, 'y': 0, 'z': 0}, {'id': 'b', 'x': 10, 'y': 0, 'z': 0},
        {'id': 'c', 'x': 0, 'y': 0, 'z': 1}, {'id': 'd', 'x': 0, 'y': 0, 'z': 2}],
        'edges': [{'source': 'a', 'target': 'b'}, {'source': 'b', 'target': 'd'},
                  {'source': 'a', 'target': 'c'}, {'source': 'c', 'target': 'd'}], 'destinations': []})
    assert astar(graph, 'a', 'd') == ['a', 'c', 'd']


def test_arrival_clears_when_user_moves_away(graph, pose):
    pose.x, pose.z = 4, 8
    assert progress(graph, pose, ['east_elevator'], 1) == (1, 'arrived', 0)
    pose.x = 0
    assert progress(graph, pose, ['east_elevator'], 1) == (0, 'turn_right', 4)


@pytest.mark.parametrize('timestamp', [0, time.time() + 3600])
def test_invalid_pose_timestamps(navigation, pose, timestamp):
    session = navigation.create('demo_building')
    pose.timestamp = timestamp
    with pytest.raises(ValueError, match='timestamp'):
        navigation.update_pose(session, pose)
