"""FastAPI application factory.

Local development::

    cd services/backend
    WANDER_ALLOW_INSECURE=1 WANDER_DATA_ROOT=../../maps/assets \
    WANDER_ACE_ENCODER_PATH=/path/to/ace_encoder_pretrained.pt uvicorn app.main:app --reload

On Modal the same app is served by `deployment/modal_app.py`, which swaps in the
Volume-aware store and the GPU job runner.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from typing import Any

from fastapi import FastAPI

from app.api import vps, worlds
from app.config import Settings
from app.storage import WorldStore
from app.vps.service import JobRunner, VpsService


def create_app(
    settings: Settings | None = None,
    *,
    store: WorldStore | None = None,
    job_runner: JobRunner | None = None,
    volume_refresh: Callable[[], None] | None = None,
    volume_commit: Callable[[], None] | None = None,
) -> FastAPI:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    settings = settings or Settings.from_env()
    store = store or WorldStore(settings.data_root, refresh=volume_refresh, commit=volume_commit)

    app = FastAPI(title="Wander worlds backend", version="0.1.0")
    app.state.settings = settings
    app.state.store = store
    app.state.vps = VpsService(store, settings, runner=job_runner)

    @app.get("/healthz", tags=["meta"])
    def healthz() -> dict[str, Any]:
        return {
            "ok": True,
            "device": str(app.state.vps.device),
            "encoder": settings.encoder_path is not None and settings.encoder_path.is_file(),
            "jobRunner": settings.job_runner,
        }

    app.include_router(vps.router)
    app.include_router(worlds.router)
    return app


app = create_app()
