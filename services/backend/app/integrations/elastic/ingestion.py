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
            source = {**destination.model_dump(), 'site_id': graph.site_id, 'title': destination.name,
                      'text': text, 'x': point.x, 'y': point.y, 'z': point.z, 'embedding': vector}
            await self.elastic.require().index(index='map_entities', id=f'{graph.site_id}:{destination.id}',
                                               document=source, refresh='wait_for')
