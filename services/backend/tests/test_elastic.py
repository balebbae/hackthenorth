from types import SimpleNamespace
from unittest.mock import AsyncMock
import pytest
from ..app.models import Document
from ..app.integrations.elastic.client import ElasticClient
from ..app.integrations.elastic.mappings import mappings
from ..app.integrations.elastic.search import ElasticSearch
from ..app.integrations.elastic.ingestion import Ingestion, extract_text
from ..app.integrations.elastic.events import EventService, parse_rows


@pytest.fixture
def elastic(settings):
    client = SimpleNamespace(
        inference=SimpleNamespace(inference=AsyncMock(return_value={'text_embedding': [{'embedding': [1, 0, 0]}]})),
        index=AsyncMock(), delete_by_query=AsyncMock(), search=AsyncMock(return_value={'hits': {'hits': [{'_source': {'id': 'real'}, '_score': .9}]}}),
        esql=SimpleNamespace(query=AsyncMock(return_value={'columns': [{'name': 'id'}], 'values': [['event-1']]})),
        indices=SimpleNamespace(exists=AsyncMock(return_value=False), create=AsyncMock()))
    return ElasticClient(settings, client)


@pytest.mark.asyncio
async def test_mappings_and_setup(elastic):
    await elastic.setup()
    assert elastic.client.indices.create.await_count == 3
    assert mappings(3)['building_knowledge']['properties']['embedding']['dims'] == 3
    assert mappings(3)['live_events']['properties']['timestamp']['type'] == 'date'


@pytest.mark.asyncio
async def test_hybrid_filters_rrf_rerank(elastic):
    elastic.settings.elastic_rerank_endpoint = 'jina-rerank'
    result = await ElasticSearch(elastic).search('map_entities', 'site-a', 'bathroom')
    request = elastic.client.search.call_args.kwargs
    rerank = request['retriever']['text_similarity_reranker']
    assert rerank['inference_id'] == 'jina-rerank'
    retrievers = rerank['retriever']['rrf']['retrievers']
    assert retrievers[0]['standard']['query']['bool']['filter'] == [{'term': {'site_id': 'site-a'}}]
    assert retrievers[1]['knn']['filter'] == [{'term': {'site_id': 'site-a'}}]
    assert result == [{'id': 'real', 'score': .9}]
    assert elastic.client.inference.inference.call_args.kwargs['input_type'] == 'search'


@pytest.mark.asyncio
async def test_ingestion_and_dimension_validation(elastic):
    doc = Document(site_id='demo_building', id='guide', title='Guide', text='Use East Elevator.')
    ids = await Ingestion(elastic).document(doc)
    assert len(ids) == 1
    source = elastic.client.index.call_args.kwargs['document']
    assert source['text'] == doc.text and source['embedding'] == [1, 0, 0]
    assert elastic.client.inference.inference.call_args.kwargs['input_type'] == 'ingest'
    elastic.settings.elastic_embedding_dims = 4
    with pytest.raises(RuntimeError, match='dimensions'):
        await elastic.embed(['test'], 'search')


@pytest.mark.asyncio
async def test_events_parameterized_and_parsed(elastic):
    events = EventService(elastic)
    rows = await events.recent('site', 'quoted"session', 'obstacle', 5)
    kwargs = elastic.client.esql.query.call_args.kwargs
    assert 'quoted"session' not in kwargs['query']
    assert {'session': 'quoted"session'} in kwargs['params']
    assert {'kind': 'obstacle'} in kwargs['params']
    assert rows == [{'id': 'event-1'}]
    assert parse_rows({'columns': [{'name': 'a'}, {'name': 'b'}], 'values': [[1, 2]]}) == [{'a': 1, 'b': 2}]


def test_text_extraction():
    assert extract_text('guide.md', b'# Elevator') == '# Elevator'
    with pytest.raises(ValueError):
        extract_text('binary.exe', b'bad')


@pytest.mark.asyncio
async def test_openai_embeddings_omit_jina_input_type(elastic):
    elastic.settings.elastic_embedding_provider = 'openai'
    assert await elastic.embed(['text'], 'search') == [[1, 0, 0]]
    assert 'input_type' not in elastic.client.inference.inference.call_args.kwargs
