"""POST /worlds/{id}/localize/query + GET /worlds/{id}/localizations (phone image-query mirror)."""
import base64
from datetime import datetime, timezone

import pytest

from ..app.services.worlds import check
from .test_worlds import client as bare_client, world  # noqa: F401  (fixtures)

# Smallest valid-looking JPEG: SOI marker + a few bytes + EOI.
JPEG = b'\xff\xd8\xff\xe0' + b'\x00' * 16 + b'\xff\xd9'
SITE = 'site-123'


@pytest.fixture
def client(bare_client, world):
    """The example world is unpublished; give it a site so localization is accepted."""
    assert bare_client.patch(f"/worlds/{world['id']}", json={'nianticSiteId': SITE}).status_code == 200
    return bare_client


def upload(world, **overrides):
    now = datetime.now(timezone.utc).isoformat()
    body = {
        'deviceId': 'dev-1', 'role': 'chest', 'nianticSiteId': SITE, 'capturedAt': now,
        'imageBase64': base64.b64encode(JPEG).decode(),
        'image': {'width': 480, 'height': 640, 'orientation': 'portrait', 'fovDeg': {'horizontal': 50, 'vertical': 65}},
        'request': {'identifier': 'a' * 32, 'frameId': 12, 'type': 'vpsLocalize', 'status': 'completed',
                    'error': 'none', 'startedAt': now, 'endedAt': now, 'latencyMs': 310, 'frameMatch': 'exact'},
        'result': {'trackingState': 'localized', 'anchorState': 'tracked', 'confidence': 0.91,
                   'pose': {'position': [1.0, 1.5, -2.0], 'rotation': [0, 0, 0, 1]}},
    }
    body.update(overrides)
    return body


def test_query_roundtrip(client, world, settings):
    wid = world['id']
    result = client.post(f'/worlds/{wid}/localize/query', json=upload(world))
    assert result.status_code == 201, result.text
    record = result.json()
    check(record, 'navigation.schema.json', '#/$defs/localizationQuery')
    assert record['image']['path'] == f"worlds/{wid}/localizations/{record['id']}.jpg"
    assert record['nearestNode']['id'] and record['offGraphMetres'] >= 0
    assert (settings.wander_data_root / record['image']['path']).read_bytes() == JPEG

    listing = client.get(f'/worlds/{wid}/localizations')
    assert listing.status_code == 200
    check(listing.json(), 'navigation.schema.json', '#/$defs/localizationQueries')
    assert [q['id'] for q in listing.json()['queries']] == [record['id']]

    # The JPEG is served through the versioned-asset route, immutable.
    image = client.get(f"/worlds/{wid}/localizations/{record['id']}.jpg")
    assert image.status_code == 200 and image.content == JPEG
    assert 'immutable' in image.headers['cache-control']

    # A successful query stamps the site status like /localize does.
    assert client.get(f'/worlds/{wid}/vps').json()['lastLocalizedAt'] == record['capturedAt']


def test_failed_query_without_pose_is_stored(client, world):
    body = upload(world, result={'trackingState': 'lost'},
                  request={'identifier': 'b' * 32, 'type': 'vpsLocalize', 'status': 'failed',
                           'error': 'localizationFailed', 'startedAt': datetime.now(timezone.utc).isoformat()})
    result = client.post(f"/worlds/{world['id']}/localize/query", json=body)
    assert result.status_code == 201, result.text
    assert 'nearestNode' not in result.json()


def test_query_validation(client, world):
    wid = world['id']
    assert client.post(f'/worlds/{wid}/localize/query', json=upload(world, nianticSiteId='other')).status_code == 409
    assert client.post(f'/worlds/{wid}/localize/query', json=upload(world, imageBase64='not base64!')).status_code == 400
    png = base64.b64encode(b'\x89PNG\r\n\x1a\n' + b'\x00' * 8).decode()
    assert client.post(f'/worlds/{wid}/localize/query', json=upload(world, imageBase64=png)).status_code == 400
    bad = upload(world)
    bad['result']['trackingState'] = 'confused'
    assert client.post(f'/worlds/{wid}/localize/query', json=bad).status_code == 400


def test_index_is_capped_and_old_images_deleted(client, world, settings, monkeypatch):
    from ..app.api import worlds as api
    monkeypatch.setattr(api, 'LOCALIZATIONS_KEPT', 3)
    wid = world['id']
    ids = [client.post(f'/worlds/{wid}/localize/query', json=upload(world)).json()['id'] for _ in range(5)]
    listing = client.get(f'/worlds/{wid}/localizations?limit=50').json()['queries']
    assert [q['id'] for q in listing] == ids[::-1][:3]
    directory = settings.wander_data_root / 'worlds' / wid / 'localizations'
    assert not (directory / f'{ids[0]}.jpg').exists()
    assert (directory / f'{ids[-1]}.jpg').exists()
    assert len(client.get(f'/worlds/{wid}/localizations?limit=1').json()['queries']) == 1
