import logging
from starlette.exceptions import HTTPException as StarletteHTTPException
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
from .api import http, navigation_ws, assistant_ws, voice_ws, worlds, haptics
from .api.auth import APIKeyMiddleware
from .services.worlds import WorldStore, WorldNavigation
from .services.world_agent import WorldAgentTools


def create_app(settings=None, model=None, elastic=None, search=None, events=None, volume_commit=None,
               annotation_client=None):
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
    app.state.settings = settings
    # Vision client for POST /worlds/{id}/annotations/propose; None means build one from settings per call.
    app.state.annotation_client = annotation_client
    app.add_middleware(APIKeyMiddleware, key=settings.wander_api_key)
    app.state.worlds = WorldStore(settings.wander_data_root, volume_commit)
    app.state.world_navigation = WorldNavigation(app.state.worlds)
    app.state.store = MemorySessionStore()
    app.state.navigation = NavigationService(Graph.load(settings.graph_path), app.state.store)
    app.state.elastic, app.state.events = elastic, events
    app.state.ingestion = Ingestion(elastic)
    agent_tools = WorldAgentTools(
        AgentTools(app.state.navigation, search or ElasticSearch(elastic), events),
        app.state.worlds, app.state.world_navigation, app.state.store)
    app.state.store.refresh = agent_tools.refresh
    app.state.agent = BuildingAgentService(app.state.store, model, agent_tools)

    @app.exception_handler(StarletteHTTPException)
    async def rejected(request: Request, error: StarletteHTTPException):
        # Client errors are logged so a phone's rejected upload can be diagnosed from the server side.
        if 400 <= error.status_code < 500:
            logging.getLogger(__name__).warning('%s %s -> %s %s', request.method, request.url.path,
                                                error.status_code, error.detail)
        return JSONResponse(status_code=error.status_code, content={'detail': error.detail}, headers=error.headers)

    @app.exception_handler(KeyError)
    async def missing(request: Request, error):
        return JSONResponse(status_code=404, content={'detail': 'Session not found'})

    @app.exception_handler(ValueError)
    async def invalid(request: Request, error):
        return JSONResponse(status_code=422, content={'detail': str(error)})

    async def unavailable(request: Request, error):
        logging.getLogger(__name__).warning('%s %s -> Elasticsearch unavailable: %s', request.method, request.url.path, error)
        return JSONResponse(status_code=503, content={'detail': 'External service unavailable; check backend configuration'})

    for error_type in (IntegrationUnavailable, ApiError, TransportError):
        app.add_exception_handler(error_type, unavailable)
    app.include_router(http.router)
    app.include_router(worlds.router)
    app.include_router(haptics.router)
    app.include_router(navigation_ws.router)
    app.include_router(assistant_ws.router)
    app.include_router(voice_ws.router)
    return app


app = create_app()
