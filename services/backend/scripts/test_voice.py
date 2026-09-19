"""Paid voice smoke test: send a recorded PCM WAV, save the spoken reply as WAV."""
import argparse
import asyncio
import base64
import json
import wave
from pathlib import Path

import httpx
from websockets.asyncio.client import connect
from ..app.config import Settings


async def run(args):
    settings = Settings()
    if not settings.voice_access_token:
        raise ValueError('Set VOICE_ACCESS_TOKEN to match the backend')
    with wave.open(str(args.input), 'rb') as source:
        if (source.getnchannels(), source.getsampwidth(), source.getframerate()) != (1, 2, 24000):
            raise ValueError('Input must be a mono PCM16 WAV at 24000 Hz')
        audio = source.readframes(source.getnframes())
    if len(audio) > 60 * 48000:
        raise ValueError('Smoke-test recordings must be at most 60 seconds')
    async with httpx.AsyncClient(headers={'X-API-Key': settings.wander_api_key}) as http:
        response = await http.post(args.base_url + '/sessions', json={'worldId': args.site, 'deviceId': 'voice-smoke-test'})
        response.raise_for_status()
        session = response.json()['sessionId']
    url = args.base_url.replace('https://', 'wss://').replace('http://', 'ws://')
    output = bytearray()
    async with connect(f'{url}/ws/sessions/{session}/voice', additional_headers={'X-API-Key': settings.wander_api_key}) as socket:
        await socket.send(json.dumps({'type': 'auth', 'token': settings.voice_access_token}))
        ready = json.loads(await socket.recv())
        if ready.get('type') != 'voice_ready':
            raise ValueError('Voice did not become ready')

        async def send():
            # Pace input at real-time speed, followed by silence for turn detection.
            data = audio + b'\0' * 48000 * args.wait_seconds
            for offset in range(0, len(data), 4800):
                await socket.send(json.dumps({'type': 'audio',
                    'audio': base64.b64encode(data[offset:offset + 4800]).decode()}))
                await asyncio.sleep(0.1)
            await socket.send(json.dumps({'type': 'close'}))

        async def receive():
            async for raw in socket:
                event = json.loads(raw)
                if event['type'] == 'audio':
                    output.extend(base64.b64decode(event['audio']))
                elif event['type'] == 'transcript':
                    print(event['speaker'] + ': ' + event['delta'])
                elif event['type'] == 'assistant_response':
                    print('Backend:', event['text'])
                elif event['type'] == 'error':
                    raise ValueError(event['message'])
        await asyncio.gather(send(), receive())
    if not output:
        raise ValueError('No output audio received')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(args.output), 'wb') as target:
        target.setnchannels(1)
        target.setsampwidth(2)
        target.setframerate(24000)
        target.writeframes(output)
    print(args.output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=Path('artifacts/voice-reply.wav'))
    parser.add_argument('--base-url', default='http://127.0.0.1:8000')
    parser.add_argument('--site', default='demo-building')
    parser.add_argument('--wait-seconds', type=int, default=30)
    args = parser.parse_args()
    if not 5 <= args.wait_seconds <= 120:
        parser.error('wait-seconds must be 5..120')
    asyncio.run(run(args))


if __name__ == '__main__':
    main()
