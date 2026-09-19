import argparse
import asyncio
import json
from contextlib import suppress
import httpx
import websockets
from ..app.config import Settings
from .simulate_navigation import pose_message

QUESTIONS = ['Where can I go upstairs without using stairs?', 'Where is it?', 'Take me there.']


def offline():
    from fastapi.testclient import TestClient
    from ..app.main import create_app
    from ..app.config import Settings
    from .fixtures import FixtureSearch, FixtureEvents, demo_model
    print('OFFLINE SCRIPTED FIXTURE: verifies tool orchestration, not live model reasoning or Elastic retrieval.')
    app = create_app(Settings(_env_file=None, wander_api_key='offline', openai_api_key='', elasticsearch_url=''), model=demo_model(),
                     search=FixtureSearch(), events=FixtureEvents())
    with TestClient(app, headers={'X-API-Key': 'offline'}) as client:
        sid = client.post('/legacy/sessions', json={}).json()['session_id']
        with client.websocket_connect(f'/ws/legacy/sessions/{sid}') as nav:
            nav.receive_json()
            nav.send_json(pose_message(0, 0, 0))
            nav.receive_json()
            nav.receive_json()
            with client.websocket_connect(f'/ws/sessions/{sid}/assistant') as assistant:
                for question in QUESTIONS:
                    assistant.send_json({'type': 'assistant_message', 'text': question})
                    response = assistant.receive_json()
                    print('>', question)
                    print(response['text'])
                    print('Tools:', [call['name'] for call in response['tool_calls']])
                    print('Sources:', response['sources'])
                assert response['actions'][0]['destination_id'] == 'east_elevator'
                assert nav.receive_json()['type'] == 'route_update'
                state = client.get(f'/legacy/sessions/{sid}').json()
                assert state['navigation']['route'] == ['entrance', 'hall_corner', 'east_elevator']
                print('Verified real A* route:', state['navigation']['route'])


async def live(base, interactive):
    async with httpx.AsyncClient(base_url=base, timeout=300, headers={'X-API-Key': Settings().wander_api_key}) as client:
        created = await client.post('/legacy/sessions', json={})
        created.raise_for_status()
        sid = created.json()['session_id']
        ws_base = base.replace('http://', 'ws://').replace('https://', 'wss://')
        async with websockets.connect(f'{ws_base}/ws/legacy/sessions/{sid}', additional_headers={'X-API-Key': Settings().wander_api_key}) as nav:
            await nav.recv()
            async def heartbeat():
                while True:
                    await nav.send(json.dumps(pose_message(0, 0, 0)))
                    await asyncio.sleep(3)

            async def drain():
                async for raw in nav:
                    message = json.loads(raw)
                    if message['type'] == 'error':
                        print('Navigation error:', message)

            # Initial localization is acknowledged before the first assistant request.
            await nav.send(json.dumps(pose_message(0, 0, 0)))
            await nav.recv()
            await nav.recv()
            tasks = [asyncio.create_task(heartbeat()), asyncio.create_task(drain())]
            try:
                questions = iter(QUESTIONS)
                while True:
                    question = await asyncio.to_thread(input, '> ') if interactive else next(questions, '')
                    if not question:
                        break
                    result = await client.post('/assistant/query', json={'session_id': sid, 'text': question})
                    result.raise_for_status()
                    data = result.json()
                    print(json.dumps(data, indent=2))
                    if question == QUESTIONS[-1] and not interactive:
                        assert any(a['type'] == 'set_destination' for a in data['actions']), 'No successful navigation action'
                        break
            finally:
                for task in tasks:
                    task.cancel()
                for task in tasks:
                    with suppress(asyncio.CancelledError):
                        await task


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--interactive', action='store_true')
    parser.add_argument('--base-url', default='http://127.0.0.1:8000')
    args = parser.parse_args()
    offline() if args.offline else asyncio.run(live(args.base_url.rstrip('/'), args.interactive))
