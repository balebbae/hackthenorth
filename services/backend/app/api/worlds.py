"""Read side of `/worlds` that the Next.js proxy needs (list, manifest, versioned assets)."""

from __future__ import annotations

import mimetypes
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import FileResponse

from app.auth import require_api_key
from app.storage import WorldStore, is_safe_segment

router = APIRouter(prefix="/worlds", tags=["worlds"], dependencies=[Depends(require_api_key)])


def get_store(request: Request) -> WorldStore:
    store: WorldStore = request.app.state.store
    return store


@router.get("")
def list_worlds(store: WorldStore = Depends(get_store)) -> dict[str, Any]:
    store.refresh()
    return {"worlds": store.list_worlds()}


@router.get("/{world_id}")
def get_world(world_id: str, store: WorldStore = Depends(get_store)) -> dict[str, Any]:
    if not is_safe_segment(world_id):
        raise HTTPException(400, "invalid world id")
    store.refresh()
    manifest = store.read_manifest(world_id)
    if manifest is None:
        raise HTTPException(404, "world not found")
    return manifest


@router.get("/{world_id}/{version}/{filename}")
def get_asset(world_id: str, version: str, filename: str, store: WorldStore = Depends(get_store)) -> FileResponse:
    if not all(is_safe_segment(s) for s in (world_id, version, filename)) or version == "vps":
        raise HTTPException(404, "asset not found")
    store.refresh()
    path = store.asset_path(world_id, [version, filename])
    if not path.is_file():
        raise HTTPException(404, "asset not found")
    media_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    return FileResponse(path, media_type=media_type)
