"""Run with --offline for an in-process API/WebSocket test, or against a local server."""
import argparse
import asyncio
import json
import time
import httpx
import websockets

MOVES = [(0, 0, 0), (0, 8, 0), (0, 8, 90), (4, 8, 90)]


def pose_message(x, z, heading):
    return {'type': 'pose_update', 'pose': {'x': x, 'y': 0, 'z': z, 'heading': heading,
            'localized': True, 'timestamp': time.time()}}


def offline():
    from fastapi.testclient import TestClient
    from ..app.main import create_app
    from ..app.config import Settings
    from .fixtures import FixtureEvents
    with TestClient(create_app(Settings(_env_file=None, openai_api_key='', elasticsearch_url=''), events=FixtureEvents())) as client:
        sid = client.post('/sessions', json={}).json()['session_id']
        with client.websocket_connect(f'/ws/sessions/{sid}') as ws:
            ws.receive_json()
            ws.send_json(pose_message(0, 0, 0))
            ws.receive_json()
            ws.receive_json()
            ws.send_json({'type': 'set_destination', 'destination_id': 'east_elevator'})
            route = ws.receive_json()
            assert route['route'] == ['entrance', 'hall_corner', 'east_elevator'], route
            print('Route:', ' -> '.join(route['route']))
            print(ws.receive_json()['instruction'])
            for x, z, heading in MOVES[1:]:
                ws.send_json(pose_message(x, z, heading))
                ws.receive_json()
                instruction = ws.receive_json()['instruction']
                print(instruction)
            assert instruction == 'arrived'


async def live(base):
    async with httpx.AsyncClient(base_url=base) as client:
        response = await client.post('/sessions', json={})
        response.raise_for_status()
        sid = response.json()['session_id']
    ws_base = base.replace('http://', 'ws://').replace('https://', 'wss://')
    async with websockets.connect(f'{ws_base}/ws/sessions/{sid}') as ws:
        await ws.recv()
        await ws.send(json.dumps(pose_message(0, 0, 0)))
        await ws.recv()
        await ws.recv()
        await ws.send(json.dumps({'type': 'set_destination', 'destination_id': 'east_elevator'}))
        route = json.loads(await ws.recv())
        assert route['route'] == ['entrance', 'hall_corner', 'east_elevator'], route
        print('Route:', ' -> '.join(route['route']))
        print(json.loads(await ws.recv())['instruction'])
        for x, z, heading in MOVES[1:]:
            await ws.send(json.dumps(pose_message(x, z, heading)))
            await ws.recv()
            instruction = json.loads(await ws.recv())['instruction']
            print(instruction)
        assert instruction == 'arrived'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--base-url', default='http://127.0.0.1:8000')
    args = parser.parse_args()
    offline() if args.offline else asyncio.run(live(args.base_url.rstrip('/')))
