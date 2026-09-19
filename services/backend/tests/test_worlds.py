from copy import deepcopy
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace
from unittest.mock import AsyncMock
import json

import pytest
from fastapi.testclient import TestClient
from ..app.main import create_app
from ..app.services.worlds import check, compute_route, world_graph
from ..app.config import ROOT
from ..app.integrations.elastic.client import ElasticClient
from ..scripts.fixtures import ScriptedModel, FixtureEvents, FixtureSearch


@pytest.fixture
def world():
    return json.loads((ROOT / 'shared/contracts/examples/demo-building.world.json').read_text(encoding='utf-8'))


@pytest.fixture
def client(settings, world):
    path = settings.wander_data_root / 'worlds' / world['id'] / 'world.json'
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(world), encoding='utf-8')
    with TestClient(create_app(settings, model=ScriptedModel([]), events=FixtureEvents(),
                              search=FixtureSearch()), headers={'X-API-Key': settings.wander_api_key}) as value:
        yield value


def test_auth_fails_closed(client):
    assert client.get('/worlds', headers={'X-API-Key': ''}).status_code == 401
    assert client.get('/worlds', headers={'X-API-Key': 'wrong'}).json() == {'detail': 'invalid api key'}


def test_world_crud_and_schema(client):
    result = client.post('/worlds', json={'id': 'test', 'name': 'Test'})
    assert result.status_code == 201
    check(result.json(), 'world.schema.json')
    assert client.post('/worlds', json={'id': 'test', 'name': 'Test'}).status_code == 409
    assert client.post('/worlds', json={'id': '..escape', 'name': 'Test'}).status_code == 400
    assert len(client.get('/worlds').json()['worlds']) == 2
    assert client.patch('/worlds/test', json={'assets': {}}).status_code == 400
    assert client.patch('/worlds/test', json={'name': 'New'}).json()['name'] == 'New'
    assert client.delete('/worlds/test').status_code == 204
    assert client.get('/worlds/test').status_code == 404


def test_graph_measurements_and_immutable_assets(client, world):
    url = '/worlds/demo-building'
    invalid = deepcopy(world['navigationGraph'])
    invalid['nodes'].append(invalid['nodes'][0])
    assert client.put(url+'/graph', json=invalid).status_code == 400
    invalid = deepcopy(world['navigationGraph'])
    invalid['edges'][0]['to'] = 'unknown'
    assert client.put(url+'/graph', json=invalid).status_code == 400
    assert client.get(url+'/measurements').json()['measurements'] == []
    measurements = {'schema': 'wander.measurements/v1', 'worldId': 'demo-building', 'measurements': [
        {'id': 'width', 'points': [[0,0,0], [1,0,0]]}]}
    assert client.put(url+'/measurements', json=measurements).status_code == 200
    check(client.get(url+'/measurements').json(), 'measurements.schema.json')
    assert client.put(url+'/v1/scene.spz', content=b'splat').status_code == 201
    assert client.put(url+'/v1/scene.spz', content=b'overwrite').status_code == 409
    asset = client.get(url+'/v1/scene.spz')
    assert asset.content == b'splat' and asset.headers['content-length'] == '5'
    assert 'immutable' in asset.headers['cache-control'] and 'etag' in asset.headers
    assert client.put(url+'/v2/scene.spz', content=b'new').status_code == 201
    updated = client.patch(url, json={'version': 'v2'})
    assert updated.json()['assets']['splat'].endswith('/v2/scene.spz')


def test_weighted_directed_routing_and_heading(world):
    world['navigationGraph'] = {'nodes': [
        {'id': 'a', 'position': [0,0,0]}, {'id': 'b', 'position': [0,0,-10]},
        {'id': 'c', 'position': [10,0,0]}], 'edges': [
        {'from': 'a', 'to': 'b', 'distance': 1, 'bidirectional': False},
        {'from': 'a', 'to': 'c', 'distance': 5}, {'from': 'c', 'to': 'b', 'distance': 5}]}
    route = compute_route(world, {'from': [0,0,-5], 'to': 'b'})
    check(route, 'navigation.schema.json', '#/$defs/routeResponse')
    assert route['totalMetres'] == .5 and route['legs'][0]['headingDeg'] == 0
    reverse = compute_route(world, {'from': [0,0,-5], 'to': 'a'})
    assert reverse['totalMetres'] == 10.5
    avoiding = compute_route(world, {'from': 'a', 'to': 'b', 'avoid': ['c']})
    assert avoiding['totalMetres'] == 1


def test_alignment_changes_graph_but_not_vps_pose(client, world):
    world['navigationGraph']['frame'] = 'splat'
    world['alignment']['position'] = [100,0,0]
    world['alignment']['scale'] = 2
    assert world_graph(world)['nodes'][0]['position'] == [100,0,0]
    client.patch('/worlds/demo-building', json={'nianticSiteId': 'site', 'alignment': world['alignment']})
    client.put('/worlds/demo-building/graph', json=world['navigationGraph'])
    data = {'deviceId': 'phone', 'nianticSiteId': 'site', 'confidence': .9,
            'pose': {'position': [100,0,0], 'rotation': [0,0,0,1]}, 'timestamp': datetime.now(timezone.utc).isoformat()}
    result = client.post('/worlds/demo-building/localize', json=data)
    assert result.status_code == 200
    check(result.json(), 'navigation.schema.json', '#/$defs/localizationResponse')
    assert result.json()['pose']['position'] == [100,0,0]
    assert result.json()['offGraphMetres'] == 0
    data['nianticSiteId'] = 'wrong'
    assert client.post('/worlds/demo-building/localize', json=data).status_code == 409


def test_session_progress_events_and_persistence(client, settings):
    session = client.post('/sessions', json={'worldId': 'demo-building', 'deviceId': 'phone',
                                            'destination': 'room-101'}).json()
    check(session, 'navigation.schema.json', '#/$defs/session')
    sid = session['sessionId']
    timestamp = datetime.now(timezone.utc).isoformat()
    with client.websocket_connect(f'/ws/sessions/{sid}') as ws:
        check(ws.receive_json(), 'navigation.schema.json', '#/$defs/sessionEvent')
        ws.send_json({'type': 'ping'})
        response = client.post(f'/sessions/{sid}/pose', json={'timestamp': timestamp,
            'pose': {'position': [0,0,0], 'rotation': [0,0,0,1]}, 'trackingState': 'localized'})
        assert response.status_code == 200
        check(response.json(), 'navigation.schema.json', '#/$defs/progressUpdate')
        assert ws.receive_json()['type'] == 'rerouted'
        assert ws.receive_json()['type'] == 'progress'
        assert client.post(f'/sessions/{sid}/pose', json={'timestamp': timestamp,
            'pose': {'position': [0,0,0], 'rotation': [0,0,0,1]}}).status_code == 400
    from ..app.services.worlds import WorldStore
    assert WorldStore(settings.wander_data_root).session(sid)['state'] == 'navigating'
    assert client.delete(f'/sessions/{sid}').status_code == 204
    assert client.get(f'/sessions/{sid}').json()['state'] == 'ended'


def test_invalid_quaternion_and_no_implicit_world_session(client):
    sid = client.post('/sessions', json={'worldId': 'demo-building', 'deviceId': 'phone',
                                       'destination': 'room-101'}).json()['sessionId']
    assert client.post(f'/sessions/{sid}/pose', json={'timestamp': datetime.now(timezone.utc).isoformat(),
        'pose': {'position': [0,0,0], 'rotation': [0,0,0,0]}}).status_code == 400
    assert client.post('/worlds/demo-building/route', json={'to': 'room-101'}).status_code == 400


def test_graph_updates_are_immediate_and_splat_switch_supported(client, world):
    url = '/worlds/demo-building'
    route = client.post(url+'/route', json={'from': 'entrance', 'to': 'room-101'}).json()
    graph = deepcopy(world['navigationGraph'])
    graph['edges'] = [{'from': 'entrance', 'to': 'room-101', 'distance': 2}]
    assert client.put(url+'/graph', json=graph).status_code == 200
    assert client.post(url+'/route', json={'from': 'entrance', 'to': 'room-101'}).json()['totalMetres'] == 2
    assert route['totalMetres'] > 2
    assert client.put(url+'/v2/scene.ply', content=b'ply').status_code == 201
    assert client.patch(url, json={'version': 'v2'}).json()['assets']['splat'].endswith('/scene.ply')


def test_lost_tracking_offroute_reroute_and_arrival(client):
    graph = {'nodes': [{'id': 'a', 'position': [0,0,0]}, {'id': 'b', 'position': [0,0,-10], 'kind': 'destination'}],
             'edges': [{'from': 'a', 'to': 'b'}]}
    client.put('/worlds/demo-building/graph', json=graph)
    sid = client.post('/sessions', json={'worldId': 'demo-building', 'deviceId': 'phone', 'destination': 'b'}).json()['sessionId']
    start = datetime.now(timezone.utc)-timedelta(seconds=10)
    def update(seconds, point, tracking='localized'):
        result = client.post(f'/sessions/{sid}/pose', json={'timestamp': (start+timedelta(seconds=seconds)).isoformat(),
            'trackingState': tracking, 'pose': {'position': point, 'rotation': [0,0,0,1]}})
        assert result.status_code == 200, result.text
        return result.json()
    assert update(0, [0,0,0])['state'] == 'navigating'
    assert update(1, [5,0,-2])['state'] == 'off-route'
    with client.websocket_connect(f'/ws/sessions/{sid}') as ws:
        ws.receive_json()
        assert update(7, [5,0,-3])['state'] == 'off-route'
        assert ws.receive_json()['type'] == 'rerouted'
        assert ws.receive_json()['type'] == 'progress'
    assert update(8, [0,0,-5], 'lost')['state'] == 'lost'
    assert update(9, [0,0,-10])['state'] == 'arrived'


def test_annotation_publication_uses_current_world_hash(client, world):
    from ..app.services.annotations import AnnotationBatch, Candidate, batch_digest, world_digest
    batch = AnnotationBatch(site_id=world['id'], map_revision='v1', floor=0, model='fake', candidates=[
        Candidate(id='water', frame='a.jpg', frame_sha256='abc', category='bottle_filler',
                  name='Bottle filler', description='Verified fixture', sign_text='', designation='unknown', uncertainty='')])
    review = {'site_id': world['id'], 'map_revision': 'v1', 'batch_sha256': batch_digest(batch),
        'graph_sha256': world_digest(world), 'reviews': [{'candidate_id': 'water', 'decision': 'approve',
        'waypoint_id': 'lobby', 'verified_by': 'Surveyor', 'verified_at': '2026-09-19'}]}
    result = client.put('/worlds/demo-building/annotations', json={'batch': batch.model_dump(), 'review': review})
    assert result.status_code == 200, result.text
    check(result.json(), 'world.schema.json')
    assert result.json()['navigationGraph']['nodes'][-1]['id'] == 'water'
    assert client.post('/worlds/demo-building/route', json={'from': 'entrance', 'to': 'water'}).status_code == 200
    assert client.put('/worlds/demo-building/annotations', json={'batch': batch.model_dump(), 'review': review}).status_code == 422


def test_publish_reindexes_and_notes_hazards_without_a_separate_index_call(settings, world):
    from ..app.services.annotations import AnnotationBatch, Candidate, batch_digest, world_digest
    path = settings.wander_data_root / 'worlds' / world['id'] / 'world.json'
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(world), encoding='utf-8')
    stub = SimpleNamespace(
        inference=SimpleNamespace(inference=AsyncMock(return_value={'text_embedding': [{'embedding': [1, 0, 0]}]})),
        index=AsyncMock(), close=AsyncMock(),
        indices=SimpleNamespace(exists=AsyncMock(return_value=True), create=AsyncMock(), put_mapping=AsyncMock()))
    elastic = ElasticClient(settings, stub)
    with TestClient(create_app(settings, model=ScriptedModel([]), events=FixtureEvents(), search=FixtureSearch(),
                              elastic=elastic), headers={'X-API-Key': settings.wander_api_key}) as client:
        batch = AnnotationBatch(site_id=world['id'], map_revision='v1', floor=0, model='fake', candidates=[
            Candidate(id='hazard-1', frame='a.jpg', frame_sha256='abc', category='obstacle',
                      name='Loose cable', description='Cable across corridor', sign_text='',
                      designation='unknown', uncertainty='Uncertain extent', navigation_role='potential_hazard')])
        review = {'site_id': world['id'], 'map_revision': 'v1', 'batch_sha256': batch_digest(batch),
            'graph_sha256': world_digest(world), 'reviews': [{'candidate_id': 'hazard-1', 'decision': 'note',
            'waypoint_id': 'lobby', 'verified_by': 'Surveyor', 'verified_at': '2026-09-19'}]}
        result = client.put(f"/worlds/{world['id']}/annotations",
                            json={'batch': batch.model_dump(), 'review': review})
        assert result.status_code == 200, result.text
    notes_path = settings.wander_data_root / 'worlds' / world['id'] / 'context-notes.json'
    assert notes_path.exists()
    notes = json.loads(notes_path.read_text())
    assert notes[0]['id'] == 'hazard-1'
    assert notes[0]['navigation_role'] == 'potential_hazard'
    # Reindex happened inline as part of publish; no separate POST /index call was made.
    assert stub.index.await_count >= 1
    indexed_ids = {call.kwargs['document']['id'] for call in stub.index.await_args_list}
    assert 'hazard-1' in indexed_ids


def test_agent_can_read_persisted_world_session(client):
    sid = client.post('/sessions', json={'worldId': 'demo-building', 'deviceId': 'phone'}).json()['sessionId']
    result = client.post('/assistant/query', json={'session_id': sid, 'text': 'Where am I?'})
    assert result.status_code == 200
    assert client.app.state.store.get(sid).site_id == 'demo-building'


def test_oversized_asset_is_not_published(client):
    client.app.state.settings.asset_max_bytes = 3
    result = client.put('/worlds/demo-building/v1/scene.spz', content=b'1234')
    assert result.status_code == 413
    assert client.get('/worlds/demo-building/v1/scene.spz').status_code == 404
    assert not list(client.app.state.worlds.path('worlds', 'demo-building', 'v1').glob('upload-*'))


def test_world_socket_authentication_and_read_only_commands(client):
    from starlette.testclient import WebSocketDenialResponse
    from starlette.websockets import WebSocketDisconnect
    sid = client.post('/sessions', json={'worldId': 'demo-building', 'deviceId': 'phone'}).json()['sessionId']
    with pytest.raises(WebSocketDenialResponse) as error:
        with client.websocket_connect(f'/ws/sessions/{sid}', headers={'X-API-Key': 'wrong'}):
            pass
    assert error.value.status_code == 401
    with client.websocket_connect(f'/ws/sessions/{sid}') as socket:
        socket.receive_json()
        socket.send_json({'type': 'set_destination', 'destination': 'room-101'})
        with pytest.raises(WebSocketDisconnect):
            socket.receive_json()


def test_api_key_unconfigured_is_not_an_auth_bypass(settings):
    settings.wander_api_key = ''
    with TestClient(create_app(settings, model=ScriptedModel([]), events=FixtureEvents())) as client:
        assert client.get('/health').status_code == 401
