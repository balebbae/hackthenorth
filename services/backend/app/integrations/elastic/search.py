class ElasticSearch:
    def __init__(self, elastic):
        self.elastic = elastic

    def _retriever(self, query, vector, filters):
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
        return retriever

    def _proximity_rescore(self, near):
        # Real Euclidean proximity on our local per-building x/y/z coordinates.
        # There is no real-world lat/long anywhere in this app, so this deliberately
        # does not use geo_point/geo_distance, which would misrepresent the data.
        script = ("double dx = doc['x'].size()==0 ? 1000000 : doc['x'].value - params.x;"
                  "double dy = doc['y'].size()==0 ? 0 : doc['y'].value - params.y;"
                  "double dz = doc['z'].size()==0 ? 0 : doc['z'].value - params.z;"
                  "return 1.0 / (1.0 + Math.sqrt(dx * dx + dy * dy + dz * dz));")
        return {'window_size': 40, 'query': {
            'rescore_query': {'script_score': {'query': {'match_all': {}},
                'script': {'source': script, 'params': {'x': near['x'], 'y': near['y'], 'z': near['z']}}}},
            'query_weight': 1, 'rescore_query_weight': 4}}

    async def search(self, index: str, site_id: str, query: str, near: dict | None = None):
        if index not in ('building_knowledge', 'map_entities'):
            raise ValueError('Unknown search index')
        vector = (await self.elastic.embed([query], 'search'))[0]
        filters = [{'term': {'site_id': site_id}}]
        retriever = self._retriever(query, vector, filters)
        request = {'index': index, 'size': 8, 'retriever': retriever, 'source_excludes': ['embedding']}
        if near is not None:
            request['rescore'] = self._proximity_rescore(near)
        response = await self.elastic.require().search(**request)
        return [dict(hit['_source'], score=hit.get('_score')) for hit in response['hits']['hits']]

    async def context(self, site_id: str, query: str, floor: int | None = None):
        """Non-navigable context/hazard evidence: hybrid retrieval plus aggregations
        so an agent can both cite specific findings and summarize what's around."""
        vector = (await self.elastic.embed([query], 'search'))[0]
        filters = [{'term': {'site_id': site_id}}, {'term': {'is_destination': False}}]
        if floor is not None:
            filters.append({'term': {'floor': floor}})
        retriever = self._retriever(query, vector, filters)
        response = await self.elastic.require().search(index='map_entities', size=8, retriever=retriever,
            source_excludes=['embedding'],
            aggs={'by_category': {'terms': {'field': 'category', 'size': 10}},
                  'by_role': {'terms': {'field': 'navigation_role', 'size': 5}}})
        results = [dict(hit['_source'], score=hit.get('_score')) for hit in response['hits']['hits']]
        aggregations = response.get('aggregations', {})
        counts_by_category = {bucket['key']: bucket['doc_count']
                               for bucket in aggregations.get('by_category', {}).get('buckets', [])}
        counts_by_role = {bucket['key']: bucket['doc_count']
                          for bucket in aggregations.get('by_role', {}).get('buckets', [])}
        return {'results': results, 'counts_by_category': counts_by_category, 'counts_by_role': counts_by_role}
