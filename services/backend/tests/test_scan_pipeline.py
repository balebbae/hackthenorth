import json
from types import SimpleNamespace

import httpx
import pytest
import subprocess

from services.backend.scripts import scan_pipeline as pipeline


def test_import_resumes_without_repeating_paid_annotation(tmp_path, monkeypatch):
    splat, video = tmp_path / 'input.spz', tmp_path / 'input.mp4'
    splat.write_bytes(b'splat')
    video.write_bytes(b'video')
    state = {'world': None, 'asset': None, 'jobs': 0}

    def handle(request):
        path = request.url.path
        if path == '/health':
            if '__modal_attempt_token' not in request.url.params:
                return httpx.Response(303, headers={'location': '/health?__modal_attempt_token=test'})
            assert request.headers['X-API-Key'] == 'test'
            return httpx.Response(200, json={})
        if path == '/worlds' and request.method == 'POST':
            state['world'] = {'schema': 'wander.world/v1', 'id': 'test', 'version': 'v1',
                              'assets': {'splat': 'worlds/test/v1/scene.spz'}}
            return httpx.Response(201, json=state['world'])
        if path == '/worlds/test':
            return httpx.Response(200, json=state['world']) if state['world'] else httpx.Response(404)
        if request.method == 'PUT':
            state['asset'] = request.read()
            return httpx.Response(201, json={})
        return httpx.Response(200, content=state['asset']) if state['asset'] else httpx.Response(404)

    client = httpx.Client
    monkeypatch.setattr(pipeline.httpx, 'Client', lambda **kwargs: client(
        **kwargs, transport=httpx.MockTransport(handle)))
    monkeypatch.setattr(pipeline, 'ROOT', tmp_path)
    monkeypatch.setattr(pipeline, 'Settings', lambda: SimpleNamespace(
        wander_backend_url='https://backend.test', wander_api_key='test'))

    def command(*args):
        state['jobs'] += 1
        output = args[args.index('--output') + 1]
        pipeline.write_json(output, {'version': 1, 'site_id': 'test', 'map_revision': 'v1',
                                    'floor': 0, 'model': 'test', 'candidates': []})

    monkeypatch.setattr(pipeline, 'command', command)
    monkeypatch.setattr(pipeline.sys, 'argv', ['scan_pipeline', '--world', 'test',
                        '--splat', str(splat), '--video', str(video)])
    pipeline.main()
    review = tmp_path / 'artifacts/test/v1/review.json'
    original = review.read_text()
    pipeline.main()
    assert state['jobs'] == 1
    assert state['asset'] == b'splat'
    assert review.read_text() == original
    assert json.loads(original)['site_id'] == 'test'


def test_redirect_cannot_forward_key_to_another_origin():
    from services.backend.scripts.backend_http import check_redirect
    seen = []

    def handle(request):
        seen.append(request.url.host)
        return httpx.Response(303, headers={'location': 'https://other.test/health'})

    with httpx.Client(transport=httpx.MockTransport(handle), follow_redirects=True,
                      headers={'X-API-Key': 'test'},
                      event_hooks={'response': [check_redirect]}) as client:
        with pytest.raises(httpx.RequestError, match='another origin'):
            client.get('https://backend.test/health')
    assert seen == ['backend.test']


def test_discovery_timeout_kills_lookup(monkeypatch, capsys):
    class StuckLookup:
        killed = False

        def communicate(self, timeout=None):
            if timeout:
                raise subprocess.TimeoutExpired('lookup', timeout)
            return '', ''

        def poll(self):
            return 1 if self.killed else None

        def kill(self):
            self.killed = True

    process = StuckLookup()
    monkeypatch.setattr(pipeline.subprocess, 'Popen', lambda *a, **kw: process)
    with pytest.raises(TimeoutError, match='45 seconds'):
        pipeline.discover_backend_url()
    assert process.killed
    assert '(5/45 seconds)' in capsys.readouterr().out


def test_discovery_saves_endpoint(tmp_path, monkeypatch):
    class Lookup:
        returncode = 0

        def communicate(self, timeout=None):
            return 'WANDER_ENDPOINT=https://test.modal.run\n', ''

        def poll(self):
            return 0

    (tmp_path / 'services/backend').mkdir(parents=True)
    monkeypatch.setattr(pipeline, 'ROOT', tmp_path)
    monkeypatch.setattr(pipeline.subprocess, 'Popen', lambda *a, **kw: Lookup())
    assert pipeline.discover_backend_url() == 'https://test.modal.run'
    assert 'https://test.modal.run' in (tmp_path / 'services/backend/.env').read_text()
