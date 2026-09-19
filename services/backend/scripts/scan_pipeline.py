"""One-command scan import; rerun with --publish after reviewing placements."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone

import httpx

from ..app.config import Settings, ROOT
from .backend_http import check_redirect
from ..app.services.annotations import AnnotationBatch, batch_digest, world_digest, write_json


def discover_backend_url():
    from dotenv import set_key
    print('Looking up the deployed Modal backend...', flush=True)
    # Isolate SDK retries so even a stuck network lookup can be terminated.
    code = (
        "import modal; "
        "url = modal.Function.from_name('htn-navigation-backend', 'fastapi_app').get_web_url(); "
        "print('WANDER_ENDPOINT=' + (url or ''), flush=True)"
    )
    process = subprocess.Popen([sys.executable, '-c', code], cwd=ROOT,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        for elapsed in range(5, 46, 5):
            try:
                output, _ = process.communicate(timeout=5)
                break
            except subprocess.TimeoutExpired:
                print(f'Modal lookup still waiting ({elapsed}/45 seconds); no scan upload has started.', flush=True)
        else:
            raise TimeoutError('Modal endpoint lookup timed out after 45 seconds. Check your network and Modal authentication, or run the deployment script to save the URL.')
        matches = re.findall(r'^WANDER_ENDPOINT=(https://\S+)$', output, re.MULTILINE)
        if process.returncode != 0 or len(matches) != 1:
            raise ValueError('Modal could not resolve htn-navigation-backend / fastapi_app. Check that it is deployed in your current Modal profile, or run python -m services.backend.scripts.deploy.')
        url = matches[0]
    finally:
        if process.poll() is None:
            process.kill()
            process.communicate()
    set_key(str(ROOT / 'services/backend/.env'), 'WANDER_BACKEND_URL', url)
    print(f'Found backend: {url}', flush=True)
    return url.rstrip('/')


def command(*args):
    subprocess.run([sys.executable, '-X', 'utf8', *map(str, args)], cwd=ROOT, check=True)


def digest(path):
    with path.open('rb') as source:
        return hashlib.file_digest(source, 'sha256').hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--world', default='test-building')
    parser.add_argument('--splat', type=Path, help='Defaults to artifacts/<world>/<version>/scene.spz')
    parser.add_argument('--video', type=Path, help='Defaults to artifacts/<world>/<version>/walkthrough.mp4')
    parser.add_argument('--version', default='v1')
    parser.add_argument('--floor', type=int, default=0)
    parser.add_argument('--limit', type=int, default=20)
    parser.add_argument('--base-url')
    parser.add_argument('--publish', action='store_true')
    parser.add_argument('--reannotate', action='store_true', help='Archive prior annotation/review outputs and analyze the video again')
    parser.add_argument('--question', default='Search this building for bathrooms and drinking fountains. What do the indexed annotations say?')
    args = parser.parse_args()
    if args.publish and args.reannotate:
        parser.error('Use --reannotate separately from --publish.')
    settings = Settings()
    url = (args.base_url or settings.wander_backend_url).rstrip('/')
    if not settings.wander_api_key:
        parser.error(f'WANDER_API_KEY is missing from {ROOT / "services/backend/.env"}. Run python -m services.backend.scripts.deploy first.')
    for value in (args.world, args.version):
        if not re.fullmatch(r'[a-z0-9][a-z0-9._-]{0,63}', value) or '..' in value:
            parser.error('World/version must be lowercase slugs without spaces or ..')
    folder = ROOT / 'artifacts' / args.world / args.version
    args.splat = args.splat or folder / 'scene.spz'
    args.video = args.video or folder / 'walkthrough.mp4'
    # Explicit relative overrides also resolve against the script's repository.
    args.splat = ROOT / args.splat
    args.video = ROOT / args.video
    if not args.publish:
        missing = [str(path) for path in (args.splat, args.video) if not path.is_file()]
        if missing:
            parser.error('Missing scan files: ' + ', '.join(missing))
    if not url:
        try:
            url = discover_backend_url()
        except (TimeoutError, ValueError, OSError) as error:
            parser.error(str(error))
    folder.mkdir(parents=True, exist_ok=True)
    batch_path, review_path = folder / 'candidates.json', folder / 'review.json'
    world_path = folder / 'world.json'
    with httpx.Client(base_url=url, headers={'X-API-Key': settings.wander_api_key}, timeout=300,
                      follow_redirects=True, max_redirects=10,
                      event_hooks={'response': [check_redirect]}) as client:
        def request(method, path, **kwargs):
            response = client.request(method, path, **kwargs)
            response.raise_for_status()
            return response

        print('Checking backend health (up to 60 seconds for a cold start)...', flush=True)
        request('GET', '/health', timeout=60)
        print('Backend is reachable and API key accepted.', flush=True)
        endpoint = f'/worlds/{args.world}'
        if args.publish:
            if not all(p.exists() for p in (batch_path, review_path, world_path)):
                parser.error('Run import and prepare the review before --publish.')
            command('-m', 'services.backend.scripts.annotate_scan', 'publish',
                    '--batch', batch_path, '--reviews', review_path, '--graph', world_path,
                    '--revision', args.version, '--output', folder / 'published.world.json',
                    '--api-url', url, '--index')
            session = request('POST', '/sessions', json={'worldId': args.world, 'deviceId': 'scan-pipeline'}).json()
            answer = request('POST', '/assistant/query', json={
                'session_id': session['sessionId'], 'text': args.question}).json()
            write_json(folder / 'answer.json', answer)
            print(json.dumps(answer, indent=2))
            return

        if args.splat.suffix.lower() not in ('.spz', '.ply', '.splat', '.ksplat', '.sog'):
            parser.error('Unsupported splat extension.')
        if not 1 <= args.limit <= 300:
            parser.error('--limit must be 1..300.')
        print('Calculating file checksums...', flush=True)
        identity = {'splat': digest(args.splat), 'video': digest(args.video),
                    'floor': args.floor, 'limit': args.limit, 'backend': url}
        state_path = folder / 'import.json'
        if state_path.exists() and json.loads(state_path.read_text()) != identity:
            parser.error('This output folder belongs to different inputs/settings. Use a new version.')
        write_json(state_path, identity)
        print('Checking world and existing scan asset...', flush=True)
        response = client.get(endpoint)
        if response.status_code == 404:
            request('POST', '/worlds', json={'id': args.world, 'name': args.world.replace('-', ' ').title()})
        else:
            response.raise_for_status()
        asset = f'{endpoint}/{args.version}/scene{args.splat.suffix.lower()}'
        with client.stream('GET', asset) as existing:
            if existing.status_code == 200:
                checksum = hashlib.sha256()
                for chunk in existing.iter_bytes():
                    checksum.update(chunk)
                if checksum.hexdigest() != identity['splat']:
                    parser.error('Existing asset differs; use a new version.')
                upload = False
            elif existing.status_code == 404:
                upload = True
            else:
                existing.raise_for_status()
        if upload:
            print('Uploading splat...', flush=True)
            with args.splat.open('rb') as source:
                request('PUT', asset, content=source, headers={'Content-Type': 'application/octet-stream'})
        current = request('GET', endpoint).json()
        if current['version'] != args.version or current['assets']['splat'] != asset.lstrip('/'):
            request('PATCH', endpoint, json={'version': args.version})

        if args.reannotate:
            archive = folder / ('previous-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
            archive.mkdir()
            for name in ('candidates.json', 'review.json', 'world.json', 'frames'):
                previous = folder / name
                if previous.exists():
                    previous.rename(archive / name)
            print(f'Previous evidence and review preserved in {archive}', flush=True)
        if not batch_path.exists():
            print('Starting Modal video upload and annotation job; Modal will report job progress below.', flush=True)
            command('-m', 'modal', 'run', '-m', 'services.backend.deployment.modal_annotations',
                    '--video', args.video.resolve(), '--site', args.world,
                    '--revision', args.version, '--floor', args.floor, '--limit', args.limit,
                    '--output', batch_path, '--download-frames')
        if not review_path.exists():
            world = request('GET', endpoint).json()
            write_json(world_path, world)
            batch = AnnotationBatch.model_validate_json(batch_path.read_text(encoding='utf-8'))
            write_json(review_path, {'site_id': batch.site_id, 'map_revision': batch.map_revision,
                'batch_sha256': batch_digest(batch), 'graph_sha256': world_digest(world),
                'reviews': [{'candidate_id': c.id, 'decision': 'reject', 'waypoint_id': None,
                    'duplicate_of': None, 'verified_by': '', 'verified_at': '',
                    'corrected': None, 'notes': ''} for c in batch.candidates]})
        print(f'Candidates, frames and review: {folder}')
        print('Review detections and assign existing map waypoints in review.json. Then run:')
        print(f'python -m services.backend.scripts.scan_pipeline --world {args.world} --version {args.version} --publish')
        print('If the world has no navigation graph, add measured waypoints first, then regenerate the review with annotate_scan prepare-review against a fresh world.json.')


if __name__ == '__main__':
    main()
