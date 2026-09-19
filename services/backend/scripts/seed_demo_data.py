import asyncio
from ..app.config import ROOT, Settings
from ..app.models import Document
from ..app.routing.graph import Graph
from ..app.integrations.elastic.client import ElasticClient
from ..app.integrations.elastic.ingestion import Ingestion


async def main():
    settings = Settings()
    elastic = ElasticClient(settings)
    try:
        await elastic.setup()
        ingestion = Ingestion(elastic)
        graph = Graph.load(settings.graph_path)
        await ingestion.entities(graph)
        for path in (ROOT / 'services/backend/demo_data').glob('*.md'):
            ids = await ingestion.document(Document(site_id=graph.site_id, id=path.stem,
                title=path.stem, text=path.read_text(encoding='utf-8')))
            print(path.name, ids)
        print('Seeded all three index mappings, mapped entities and building documents.')
    finally:
        await elastic.close()


if __name__ == '__main__':
    asyncio.run(main())
