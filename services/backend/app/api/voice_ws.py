"""Live audio transport with client-owned delegation to the existing Responses agent.

The native client supplies PCM16LE mono 24 kHz and plays returned PCM in order.
This endpoint is opt-in and requires a server-configured demo access token.
"""
import asyncio
import base64
import binascii
import hmac
import json
import logging
from contextlib import suppress

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from websockets.asyncio.client import connect

router = APIRouter()
logger = logging.getLogger(__name__)
LIVE_URL = 'wss://api.openai.com/v1/live/sessions'
INSTRUCTIONS = """You are the spoken interface for an indoor navigation assistant.
Delegate every building, location, accessibility, or navigation request to the
client backend. It has the current position, verified map and navigation tools.
Never invent landmarks, distances, accessible routes, or claim an action happened
without a backend result. Speak backend results concisely. If localization is
unknown, say so; do not tell the user to move based on a guessed position.
Do not treat spoken claims as updates to the verified map. Never assume a
previous route or obstacle observation remains current. You may greet the user
and ask clarifying questions directly. Do not autonomously repeat a delegation
for an action that already completed. Audio is AI-generated."""


def audio_event(message):
    if not isinstance(message, dict) or set(message) != {'type', 'audio'} or message['type'] != 'audio':
        raise ValueError('Expected {type: audio, audio: base64 PCM16LE}')
    if not isinstance(message['audio'], str) or len(message['audio']) > 65536:
        raise ValueError('Audio chunk exceeds 64 KiB encoded')
    try:
        data = base64.b64decode(message['audio'], validate=True)
    except (ValueError, binascii.Error) as error:
        raise ValueError('Invalid audio base64') from error
    if not data or len(data) % 2:
        raise ValueError('Expected nonempty 16-bit PCM samples')
    return {'type': 'session.input_audio.append', 'audio': message['audio']}


class TranscriptWindow:
    """Transcripts are fragments, not turns. Only a delegation triggers a query."""
    def __init__(self):
        self.fragments = []
        self.seen = set()

    def append(self, event):
        self.fragments.append((event['end_ms'], event['delta']))
        if sum(len(text) for _, text in self.fragments) > 8000:
            raise ValueError('Pending transcript exceeds 8000 characters; reconnect')

    def delegate(self, event):
        delegation = event['delegation']
        identity = delegation['id']
        if delegation['target'] != 'client' or identity in self.seen:
            return None
        if len(self.seen) >= 100:
            raise ValueError('Call delegation limit reached; reconnect')
        self.seen.add(identity)
        offset = event['offset_ms']
        text = ''.join(text for end, text in self.fragments if end <= offset).strip()
        self.fragments = [(end, text) for end, text in self.fragments if end > offset]
        return identity, text


async def bridge(socket, upstream, agent, session_id, model):
    await upstream.send(json.dumps({'type': 'session.start', 'session': {
        'model': model, 'instructions': INSTRUCTIONS,
        'audio': {'format': {'type': 'audio/pcm', 'rate': 24000}, 'output': {'voice': 'marin'}},
        'delegation': {'type': 'client'}}}))
    ready = json.loads(await asyncio.wait_for(upstream.recv(), timeout=20))
    if ready.get('type') != 'session.started':
        raise ValueError('Live provider did not start the session')
    await socket.send_json({'type': 'voice_ready', 'format': 'pcm16le', 'rate': 24000,
                            'channels': 1, 'ai_generated_voice': True})
    window = TranscriptWindow()
    pending = asyncio.Queue(maxsize=4)
    send_lock = asyncio.Lock()

    async def send_client(event):
        async with send_lock:
            await socket.send_json(event)

    async def audio_in():
        while True:
            raw = await socket.receive_text()
            if len(raw) > 66000:
                raise ValueError('Audio message too large')
            message = json.loads(raw)
            if message == {'type': 'close'}:
                await upstream.send(json.dumps({'type': 'session.close'}))
                return
            await upstream.send(json.dumps(audio_event(message)))

    async def provider_in():
        async for raw in upstream:
            event = json.loads(raw)
            kind = event.get('type')
            if kind == 'session.input_transcript.delta':
                window.append(event)
            elif kind == 'session.delegation.created':
                work = window.delegate(event)
                if work is not None:
                    pending.put_nowait(work)
            elif kind == 'session.output_audio.delta':
                await send_client({'type': 'audio', 'audio': event['delta']})
            elif kind == 'session.closed':
                return
            elif kind == 'error':
                raise ValueError('Live provider reported an error')
            if kind in ('session.input_transcript.delta', 'session.output_transcript.delta'):
                await send_client({'type': 'transcript', 'speaker': 'user' if 'input_' in kind else 'assistant',
                                   'delta': event['delta']})

    async def delegate():
        while True:
            identity, text = await pending.get()
            if not text:
                # The protocol has no transcript-done event. Never guess missing task text.
                answer = 'Please repeat your request; the backend did not receive its transcript.'
            else:
                result = await agent.query(session_id, text)
                await send_client({'type': 'assistant_response', **result})
                answer = result['text']
            # 100 Unicode characters remain conservatively below the 500-token event cap.
            for start in range(0, len(answer), 100):
                await upstream.send(json.dumps({'type': 'session.commentary.append',
                    'delegation_id': identity, 'content': answer[start:start + 100]}))

    tasks = [asyncio.create_task(fn()) for fn in (audio_in, provider_in, delegate)]
    try:
        done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            task.result()
    finally:
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)


@router.websocket('/ws/sessions/{session_id}/voice')
async def voice_socket(socket: WebSocket, session_id: str):
    settings = socket.app.state.settings
    await socket.accept()
    if not settings.voice_enabled or not settings.voice_access_token or not settings.openai_api_key:
        await socket.close(code=1008, reason='Voice is not configured')
        return
    try:
        # A first-message token avoids putting credentials in URLs/access logs.
        raw = await asyncio.wait_for(socket.receive_text(), timeout=10)
        if len(raw) > 2048:
            raise ValueError('Invalid authentication message')
        auth = json.loads(raw)
        if (not isinstance(auth, dict) or set(auth) != {'type', 'token'} or auth['type'] != 'auth'
                or not isinstance(auth['token'], str)
                or not hmac.compare_digest(auth['token'], settings.voice_access_token)):
            await socket.close(code=1008, reason='Unauthorized')
            return
        socket.app.state.store.get(session_id)
        async with asyncio.timeout(900):
            async with connect(LIVE_URL, additional_headers={
                    'Authorization': 'Bearer ' + settings.openai_api_key}, max_size=2**20,
                    open_timeout=20) as upstream:
                await bridge(socket, upstream, socket.app.state.agent, session_id, settings.openai_live_model)
    except WebSocketDisconnect:
        return
    except Exception as error:
        logger.warning('Voice session stopped (%s)', type(error).__name__)
        with suppress(Exception):
            await socket.send_json({'type': 'error', 'message': 'Voice unavailable or call ended; reconnect to retry.'})
    finally:
        with suppress(Exception):
            await socket.close()
