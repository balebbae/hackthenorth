class ElasticSearch:
    def __init__(self, elastic):
        self.elastic = elastic

    async def search(self, index: str, site_id: str, query: str):
        if index not in ('building_knowledge', 'map_entities'):
            raise ValueError('Unknown search index')
        vector = (await self.elastic.embed([query], 'search'))[0]
        filters = [{'term': {'site_id': site_id}}]
        retriever = {'rrf': {'retrievers': [
            {'standard': {'query': {'bool': {'filter': filters, 'must': [
                {'multi_match': {'query': query, 'fields': ['title^2', 'text', 'name^3', 'aliases^2']}}]}}}},
            {'knn': {'field': 'embedding', 'query_vector': vector, 'k': 40,
                     'num_candidates': 100, 'filter': filters}},
        ], 'rank_window_size': 40, 'rank_constant': 60}}
        if self.elastic.settings.elastic_rerank_endpoint:
            retriever = {'text_similarity_reranker': {
                'retriever': retriever, 'field': 'text', 'inference_text': query,
                'inference_id': self.elastic.settings.elastic_rerank_endpoint, 'rank_window_size': 40}}
        response = await self.elastic.require().search(index=index, size=8, retriever=retriever,
                                                       source_excludes=['embedding'])
        return [dict(hit['_source'], score=hit.get('_score')) for hit in response['hits']['hits']]
