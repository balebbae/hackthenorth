"""CLI: extract, annotate, prepare-review, publish. No automatic map placement."""
import argparse
import asyncio
import hashlib
import json
import httpx
from pathlib import Path

from ..app.config import Settings
from ..app.routing.graph import Graph
from ..app.services.annotations import (AnnotationBatch, ReviewFile, annotate, batch_digest,
                                        extract_frames, publish, publish_world, world_digest, write_json)
from ..app.integrations.elastic.client import ElasticClient
from ..app.integrations.elastic.ingestion import Ingestion


async def run(args):
    if args.command == 'extract':
        extract_frames(args.video, args.output, args.interval, args.limit)
    elif args.command == 'annotate':
        await annotate(args.frames, args.output, args.site, args.revision, args.floor,
                       Settings(), args.limit)
    elif args.command == 'prepare-review':
        batch = AnnotationBatch.model_validate_json(args.batch.read_text(encoding='utf-8'))
        raw = json.loads(args.graph.read_text(encoding='utf-8'))
        digest = world_digest(raw) if raw.get('schema') == 'wander.world/v1' else hashlib.sha256(Graph.model_validate(raw).model_dump_json().encode()).hexdigest()
        if args.output.exists():
            raise ValueError('Review file already exists; refusing to overwrite human work')
        write_json(args.output, {'site_id': batch.site_id, 'map_revision': batch.map_revision,
            'batch_sha256': batch_digest(batch),
            'graph_sha256': digest,
            'reviews': [{'candidate_id': c.id, 'decision': 'reject', 'waypoint_id': None,
                         'duplicate_of': None, 'verified_by': '', 'verified_at': '',
                         'corrected': None, 'notes': ''} for c in batch.candidates]})
    else:
        batch = AnnotationBatch.model_validate_json(args.batch.read_text(encoding='utf-8'))
        reviews = ReviewFile.model_validate_json(args.reviews.read_text(encoding='utf-8'))
        if args.output.resolve() == args.graph.resolve():
            raise ValueError('Export to a new graph file; do not overwrite the reviewed input graph')
        raw = json.loads(args.graph.read_text(encoding='utf-8'))
        if raw.get('schema') == 'wander.world/v1':
            if args.revision != raw['version']:
                raise ValueError('Revision must equal the active world version')
            manifest, records = publish_world(batch, reviews, raw)
            write_json(args.output, manifest)
            write_json(args.output.with_suffix('.annotations.json'), records)
            if args.api_url:
                settings = Settings()
                async with httpx.AsyncClient(base_url=args.api_url.rstrip('/'), timeout=120,
                    headers={'X-API-Key': settings.wander_api_key}) as client:
                    result = await client.put(f"/worlds/{raw['id']}/annotations", json={
                        'batch': batch.model_dump(), 'review': reviews.model_dump()})
                    result.raise_for_status()
                    write_json(args.output, result.json())
                    if args.index:
                        result = await client.post(f"/worlds/{raw['id']}/index")
                        result.raise_for_status()
            elif args.index:
                raise ValueError('World indexing requires --api-url so the active manifest and evidence are indexed together')
            print('World exported' + (' and published to backend.' if args.api_url else '; use --api-url to publish.'))
            return
        if args.api_url:
            raise ValueError('--api-url publication requires a world.json manifest')
        graph = publish(batch, reviews, Graph.model_validate(raw), args.revision)
        # Save the local artifact before indexing. Retry indexing safely if the provider fails.
        write_json(args.output, graph.model_dump())
        if args.index:
            elastic = ElasticClient(Settings())
            try:
                await elastic.setup()
                await Ingestion(elastic).entities(graph)
            finally:
                await elastic.close()
        print('Graph exported. Set GRAPH_PATH to this file and restart the backend to activate it.')
    print(args.output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    extract = sub.add_parser('extract')
    extract.add_argument('--video', type=Path, required=True)
    extract.add_argument('--interval', type=float, default=3)
    extract.add_argument('--limit', type=int, default=120)
    annotation = sub.add_parser('annotate')
    annotation.add_argument('--frames', type=Path, required=True)
    annotation.add_argument('--site', required=True)
    annotation.add_argument('--revision', required=True)
    annotation.add_argument('--floor', type=int, required=True)
    annotation.add_argument('--limit', type=int, default=120)
    review = sub.add_parser('prepare-review')
    publication = sub.add_parser('publish')
    for command in (review, publication):
        command.add_argument('--batch', type=Path, required=True)
        command.add_argument('--graph', type=Path, required=True)
    publication.add_argument('--reviews', type=Path, required=True)
    publication.add_argument('--revision', required=True)
    publication.add_argument('--index', action='store_true', help='Calls Elastic/OpenAI; incurs usage')
    publication.add_argument('--api-url', help='Publish reviewed world annotations to the running backend')
    for command in (extract, annotation, review, publication):
        command.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        asyncio.run(run(args))
    except ValueError as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
