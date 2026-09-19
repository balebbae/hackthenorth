import time
import pytest
from ..app.config import Settings
from ..app.models import Pose
from ..app.routing.graph import Graph
from ..app.services.sessions import MemorySessionStore, NavigationService


@pytest.fixture
def settings(tmp_path):
    return Settings(_env_file=None, wander_api_key='test-key', wander_data_root=tmp_path, openai_api_key='', openai_model='', elasticsearch_url='',
                    elasticsearch_api_key='', elastic_embedding_endpoint='test-jina', elastic_embedding_dims=3)


@pytest.fixture
def graph(settings):
    return Graph.load(settings.graph_path)


@pytest.fixture
def navigation(graph):
    return NavigationService(graph, MemorySessionStore())


@pytest.fixture
def pose():
    return Pose(x=0, y=0, z=0, heading=0, localized=True, timestamp=time.time())
