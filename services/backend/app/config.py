"""Runtime configuration, read from environment variables.

Every knob has a local-development default so `uvicorn app.main:app` works from a
checkout with no Modal account; on Modal the same variables are provided by the
container image / secret (see deployment/modal_app.py).
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _env_flag(name: str, default: bool) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    """Process-wide settings."""

    # Shared secret expected in `X-API-Key`. Empty disables auth (local dev only).
    api_key: str
    # Root of the worlds layout (`worlds/<id>/...`). The Modal Volume mount in production.
    data_root: Path
    # Pretrained scene-agnostic ACE encoder weights. Optional: without it mapping refuses to start.
    encoder_path: Path | None
    # torch device for mapping + localization ("cuda", "cpu", or "auto").
    device: str
    # Where mapping jobs run: "thread" (in-process, local dev) or "modal" (spawn the GPU function).
    job_runner: str
    # Height images are resized to before hitting the encoder (ACE default 480).
    image_height: int

    @classmethod
    def from_env(cls) -> Settings:
        encoder = os.environ.get("WANDER_ACE_ENCODER_PATH", "").strip()
        return cls(
            api_key=os.environ.get("WANDER_API_KEY", ""),
            data_root=Path(os.environ.get("WANDER_DATA_ROOT", "../../maps/assets")).resolve(),
            encoder_path=Path(encoder) if encoder else None,
            device=os.environ.get("WANDER_DEVICE", "auto"),
            job_runner=os.environ.get("WANDER_JOB_RUNNER", "thread"),
            image_height=int(os.environ.get("WANDER_IMAGE_HEIGHT", "480")),
        )

    @property
    def auth_enabled(self) -> bool:
        return bool(self.api_key)

    @property
    def allow_insecure(self) -> bool:
        return _env_flag("WANDER_ALLOW_INSECURE", False)
