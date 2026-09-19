import hashlib
from io import BytesIO
from pypdf import PdfReader


def extract_text(filename: str, data: bytes) -> str:
    if filename.lower().endswith('.pdf'):
        reader = PdfReader(BytesIO(data))
        return '\n'.join(page.extract_text() or '' for page in reader.pages)
    if not filename.lower().endswith(('.md', '.txt')):
        raise ValueError('Only UTF-8 Markdown/text and text-based PDFs are supported')
    return data.decode('utf-8-sig')


class Ingestion:
    def __init__(self, elastic):
        self.elastic = elastic

    async def document(self, document):
        # Content-addressed chunks make identical uploads idempotent.
        chunks = [document.text[i:i + 1600] for i in range(0, len(document.text), 1400)]
        vectors = await self.elastic.embed(chunks, 'ingest')
        ids = []
        for i, (chunk, vector) in enumerate(zip(chunks, vectors)):
            chunk_id = f'{document.id}:{i}:{hashlib.sha256(chunk.encode()).hexdigest()[:12]}'
            source = {'id': chunk_id, 'document_id': document.id, 'site_id': document.site_id,
                      'title': document.title, 'text': chunk, 'embedding': vector}
            await self.elastic.require().index(index='building_knowledge',
                id=f'{document.site_id}:{chunk_id}', document=source, refresh='wait_for')
            ids.append(chunk_id)
        # Remove obsolete revisions only after every new chunk was indexed successfully.
        await self.elastic.require().delete_by_query(index='building_knowledge', query={'bool': {
            'filter': [{'term': {'site_id': document.site_id}}, {'term': {'document_id': document.id}}],
            'must_not': [{'terms': {'id': ids}}]}}, refresh=True)
        return ids

    async def entities(self, graph):
        for destination in graph.destinations:
            point = graph.point(destination.waypoint_id)
            text = ' '.join([destination.name, destination.entity_type, destination.description, *destination.aliases, *destination.tags])
            vector = (await self.elastic.embed([text], 'ingest'))[0]
            evidence = destination.annotation
            source = {**destination.model_dump(), 'site_id': graph.site_id, 'title': destination.name,
                      'text': text, 'x': point.x, 'y': point.y, 'z': point.z, 'embedding': vector,
                      'category': evidence.category if evidence else None,
                      'permanence': evidence.permanence if evidence else None,
                      'navigation_role': evidence.navigation_role if evidence else None,
                      'visual_location': evidence.visual_location if evidence else None,
                      'uncertainty': evidence.uncertainty if evidence else None,
                      'is_destination': True}
            await self.elastic.require().index(index='map_entities', id=f'{graph.site_id}:{destination.id}',
                                               document=source, refresh='wait_for')

    async def world(self, manifest, annotations=()):
        from ...services.worlds import world_graph
        metadata = {a['id']: a for a in annotations}
        for node in world_graph(manifest)['nodes']:
            record = metadata.get(node['id'], {})
            evidence = record.get('annotation') or {}
            name = node.get('name', node['id'])
            text = ' '.join([name, record.get('description', ''), *record.get('tags', [])])
            vector = (await self.elastic.embed([text], 'ingest'))[0]
            point = node['position']
            source = {'id': node['id'], 'site_id': manifest['id'], 'name': name, 'title': name,
                      'text': text, 'description': record.get('description', ''),
                      'entity_type': record.get('entity_type', node.get('kind', 'waypoint')),
                      'tags': record.get('tags', []), 'x': point[0], 'y': point[1], 'z': point[2],
                      'embedding': vector, 'annotation': record.get('annotation'),
                      'category': evidence.get('category'), 'permanence': evidence.get('permanence'),
                      'navigation_role': evidence.get('navigation_role'),
                      'visual_location': evidence.get('visual_location'),
                      'uncertainty': evidence.get('uncertainty'),
                      'is_destination': node.get('kind') == 'destination'}
            await self.elastic.require().index(index='map_entities', id=f"{manifest['id']}:{node['id']}",
                                               document=source, refresh='wait_for')

    async def context_notes(self, site_id, notes):
        """Index non-navigable evidence (hazards/context) alongside destinations so
        search_places' hybrid retriever finds them naturally; is_destination=False
        keeps them out of navigable results and lets search_context filter to them."""
        for note in notes:
            text = ' '.join([note['name'], note.get('description', ''), note.get('category', ''),
                             note.get('visual_location', ''), note.get('uncertainty', '')])
            vector = (await self.elastic.embed([text], 'ingest'))[0]
            source = {'id': note['id'], 'site_id': site_id, 'name': note['name'], 'title': note['name'],
                      'text': text, 'description': note.get('description', ''),
                      'entity_type': 'context_note', 'waypoint_id': note.get('waypoint_id'),
                      'tags': [], 'floor': note.get('floor'),
                      'x': note.get('x'), 'y': note.get('y'), 'z': note.get('z'), 'embedding': vector,
                      'category': note.get('category'), 'permanence': note.get('permanence'),
                      'navigation_role': note.get('navigation_role'),
                      'visual_location': note.get('visual_location'), 'uncertainty': note.get('uncertainty'),
                      'is_destination': False}
            await self.elastic.require().index(index='map_entities', id=f'{site_id}:{note["id"]}',
                                               document=source, refresh='wait_for')
