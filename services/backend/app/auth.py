"""Shared-secret authentication: `X-API-Key` (shared/contracts/README.md) or, for the iOS
localization transport which speaks the Niantic wire format, `Authorization: Bearer <key>`."""

from __future__ import annotations

import hmac

from fastapi import Header, HTTPException, Request, status

from app.config import Settings


def get_settings(request: Request) -> Settings:
    settings: Settings = request.app.state.settings
    return settings


async def require_api_key(
    request: Request,
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
    authorization: str | None = Header(default=None),
) -> None:
    settings = get_settings(request)
    if not settings.auth_enabled:
        if settings.allow_insecure:
            return
        raise HTTPException(
            status.HTTP_503_SERVICE_UNAVAILABLE,
            "WANDER_API_KEY is not configured (set WANDER_ALLOW_INSECURE=1 for local development)",
        )
    presented = x_api_key
    if presented is None and authorization is not None:
        scheme, _, token = authorization.partition(" ")
        if scheme.lower() == "bearer":
            presented = token.strip()
    if presented is None or not hmac.compare_digest(presented, settings.api_key):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "invalid or missing X-API-Key")
