from elasticsearch import AsyncElasticsearch
from .mappings import mappings


class IntegrationUnavailable(RuntimeError):
    pass


class ElasticClient:
    def __init__(self, settings, client=None):
        self.settings = settings
        self.client = client or (AsyncElasticsearch(settings.elasticsearch_url,
            api_key=settings.elasticsearch_api_key or None, request_timeout=20, max_retries=0)
            if settings.elasticsearch_url else None)

    def require(self):
        if self.client is None:
            raise IntegrationUnavailable('Elasticsearch is not configured')
        return self.client

    async def setup(self):
        client = self.require()
        for name, mapping in mappings(self.settings.elastic_embedding_dims).items():
            if not await client.indices.exists(index=name):
                await client.indices.create(index=name, mappings=mapping)

    async def embed(self, texts, input_type):
        if not self.settings.elastic_embedding_endpoint:
            raise IntegrationUnavailable('ELASTIC_EMBEDDING_ENDPOINT is required for hybrid retrieval')
        options = {} if self.settings.elastic_embedding_provider == 'openai' else {'input_type': input_type}
        result = await self.require().inference.inference(
            inference_id=self.settings.elastic_embedding_endpoint, task_type='text_embedding',
            input=texts, **options)
        vectors = [item['embedding'] for item in result['text_embedding']]
        if len(vectors) != len(texts) or any(len(v) != self.settings.elastic_embedding_dims for v in vectors):
            raise IntegrationUnavailable('Embedding dimensions/count do not match the configured index')
        return vectors

    async def close(self):
        if self.client is not None:
            await self.client.close()
