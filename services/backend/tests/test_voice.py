import asyncio
import json
from types import SimpleNamespace
from unittest.mock import AsyncMock
import pytest
from fastapi.testclient import TestClient
from ..app.api.voice_ws import TranscriptWindow, audio_event, bridge
from ..app.main import create_app


def test_audio_validation():
    assert audio_event({'type': 'audio', 'audio': 'AAA='})['type'] == 'session.input_audio.append'
    for message in ({'type': 'session.start'}, {'type': 'audio', 'audio': '!'},
                    {'type': 'audio', 'audio': 'AA=='}, {'type': 'audio', 'audio': ''}):
        with pytest.raises(ValueError):
            audio_event(message)


def test_delegation_uses_timeline_and_deduplicates():
    window = TranscriptWindow()
    window.append({'end_ms': 100, 'delta': 'Find water.'})
    window.append({'end_ms': 300, 'delta': 'New request.'})
    event = {'offset_ms': 200, 'delegation': {'id': 'd1', 'target': 'client'}}
    assert window.delegate(event) == ('d1', 'Find water.')
    assert window.delegate(event) is None
    assert window.fragments == [(300, 'New request.')]


def test_voice_disabled_by_default(settings):
    from starlette.websockets import WebSocketDisconnect
    app = create_app(settings)
    with TestClient(app, headers={'X-API-Key': settings.wander_api_key}) as client:
        with client.websocket_connect('/ws/sessions/unknown/voice') as ws:
            with pytest.raises(WebSocketDisconnect):
                ws.receive_json()


def test_voice_rejects_token_before_provider_connection(settings, monkeypatch):
    from starlette.websockets import WebSocketDisconnect
    from ..app.api import voice_ws
    settings.voice_enabled = True
    settings.voice_access_token = 'demo-token'
    settings.openai_api_key = 'fake-key'
    def forbidden(*args, **kwargs):
        raise AssertionError('Unauthorized client opened a provider connection')
    monkeypatch.setattr(voice_ws, 'connect', forbidden)
    with TestClient(create_app(settings), headers={'X-API-Key': settings.wander_api_key}) as client:
        with client.websocket_connect('/ws/sessions/unknown/voice') as ws:
            ws.send_json({'type': 'auth', 'token': 'wrong-token'})
            with pytest.raises(WebSocketDisconnect) as error:
                ws.receive_json()
            assert error.value.code == 1008


@pytest.mark.asyncio
async def test_bridge_delegates_without_blocking_audio():
    received = []
    finish = asyncio.Event()
    class Upstream:
        async def send(self, message):
            received.append(json.loads(message))
            if received[-1]['type'] == 'session.commentary.append':
                finish.set()
        async def recv(self):
            return json.dumps({'type': 'session.started'})
        def __aiter__(self):
            return self.events()
        async def events(self):
            yield json.dumps({'type': 'session.input_transcript.delta', 'end_ms': 10, 'delta': 'Find water'})
            yield json.dumps({'type': 'session.delegation.created', 'offset_ms': 20,
                              'delegation': {'id': 'd', 'target': 'client'}})
            await finish.wait()
            yield json.dumps({'type': 'session.closed'})
    class Socket:
        send_json = AsyncMock()
        async def receive_text(self):
            await asyncio.Event().wait()
    agent = SimpleNamespace(query=AsyncMock(return_value={'text': 'The fountain is mapped.',
                              'sources': [], 'actions': [], 'tool_calls': []}))
    await asyncio.wait_for(bridge(Socket(), Upstream(), agent, 'session', 'gpt-live-1'), 2)
    agent.query.assert_awaited_once_with('session', 'Find water')
    assert received[-1]['delegation_id'] == 'd'
