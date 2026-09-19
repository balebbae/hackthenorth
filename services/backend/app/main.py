from contextlib import asynccontextmanager, AsyncExitStack
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from elasticsearch import ApiError, TransportError
from .config import Settings
from .routing.graph import Graph
from .services.sessions import MemorySessionStore, NavigationService
from .services.agent_tools import AgentTools
from .services.building_agent import BuildingAgentService
from .integrations.elastic.client import ElasticClient, IntegrationUnavailable
from .integrations.elastic.search import ElasticSearch
from .integrations.elastic.events import EventService
from .integrations.elastic.ingestion import Ingestion
from .integrations.openai.agent import OpenAIAgentModel
from .api import http, navigation_ws, assistant_ws


def create_app(settings=None, model=None, elastic=None, search=None, events=None):
    settings = settings or Settings()
    elastic = elastic or ElasticClient(settings)
    events = events or EventService(elastic)
    model = model or OpenAIAgentModel(settings)

    @asynccontextmanager
    async def lifespan(app):
        async with AsyncExitStack() as cleanup:
            cleanup.push_async_callback(model.close)
            cleanup.push_async_callback(elastic.close)
            cleanup.push_async_callback(events.close)
            yield

    app = FastAPI(title='Indoor Navigation Backend', version='0.1.0', lifespan=lifespan)
    app.state.store = MemorySessionStore()
    app.state.navigation = NavigationService(Graph.load(settings.graph_path), app.state.store)
    app.state.elastic, app.state.events = elastic, events
    app.state.ingestion = Ingestion(elastic)
    app.state.agent = BuildingAgentService(app.state.store, model,
        AgentTools(app.state.navigation, search or ElasticSearch(elastic), events))

    @app.exception_handler(KeyError)
    async def missing(request: Request, error):
        return JSONResponse(status_code=404, content={'detail': 'Session not found'})

    @app.exception_handler(ValueError)
    async def invalid(request: Request, error):
        return JSONResponse(status_code=422, content={'detail': str(error)})

    async def unavailable(request: Request, error):
        return JSONResponse(status_code=503, content={'detail': 'External service unavailable; check backend configuration'})

    for error_type in (IntegrationUnavailable, ApiError, TransportError):
        app.add_exception_handler(error_type, unavailable)
    app.include_router(http.router)
    app.include_router(navigation_ws.router)
    app.include_router(assistant_ws.router)
    return app


app = create_app()
