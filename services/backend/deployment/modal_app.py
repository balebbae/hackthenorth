"""Modal deployment of the Wander worlds backend + VPS pipeline.

    cd services/backend
    modal secret create wander-api WANDER_API_KEY=<shared secret>
    modal deploy deployment/modal_app.py

Two functions share one image and one Volume (`wander-worlds`, mounted at /data):

* `web`       - CPU container serving the FastAPI app (`/worlds/*`, `/worlds/{id}/vps/*`).
                Localization runs here (encoder + head forward pass + PnP-RANSAC).
* `train_map` - GPU container that fits a scene head for one mapping job. The web
                container spawns it and polls the job record on the Volume.

The pretrained scene-agnostic encoder is downloaded into the image at build time
from `WANDER_ACE_ENCODER_URL` (defaults to the checkpoint published with the ACE
paper). Check the licence of whatever checkpoint you point this at before
deploying: the Niantic release is for non-commercial use.
"""

from __future__ import annotations

import os
from pathlib import Path

import modal

APP_NAME = "wander-backend"
VOLUME_NAME = "wander-worlds"
DATA_ROOT = "/data"
ENCODER_PATH = "/models/ace_encoder_pretrained.pt"
ENCODER_URL = os.environ.get(
    "WANDER_ACE_ENCODER_URL",
    "https://github.com/nianticlabs/ace/raw/e9e90f2d02ee92c348bf411a5a60e230af6c315e/ace_encoder_pretrained.pt",
)
TRAIN_GPU = os.environ.get("WANDER_TRAIN_GPU", "A10G")
WEB_GPU = os.environ.get("WANDER_WEB_GPU") or None  # e.g. "T4" for faster localization

BACKEND_DIR = Path(__file__).resolve().parent.parent

app = modal.App(APP_NAME)
volume = modal.Volume.from_name(VOLUME_NAME, create_if_missing=True)
api_secret = modal.Secret.from_name("wander-api")

image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("libgl1", "libglib2.0-0", "curl")
    .pip_install(
        "fastapi[standard]>=0.115",
        "pydantic>=2.7",
        "numpy>=1.26",
        "opencv-python-headless>=4.9",
        "poselib>=2.0",
    )
    .pip_install("torch>=2.2", index_url="https://download.pytorch.org/whl/cu124")
    .run_commands(f"mkdir -p /models && curl -fsSL -o {ENCODER_PATH} {ENCODER_URL}")
    .env(
        {
            "WANDER_DATA_ROOT": DATA_ROOT,
            "WANDER_ACE_ENCODER_PATH": ENCODER_PATH,
            "WANDER_JOB_RUNNER": "modal",
        }
    )
    .add_local_dir(str(BACKEND_DIR / "app"), remote_path="/root/app")
)


class ModalJobRunner:
    """Spawns the GPU mapping function; job progress is exchanged through the Volume."""

    def submit(self, world_id: str, map_id: str, job_id: str) -> None:
        train_map.spawn(world_id, map_id, job_id)


@app.function(
    image=image,
    volumes={DATA_ROOT: volume},
    secrets=[api_secret],
    gpu=TRAIN_GPU,
    timeout=60 * 60,
    memory=32768,
)
def train_map(world_id: str, map_id: str, job_id: str) -> None:
    from app.config import Settings
    from app.storage import WorldStore
    from app.vps.service import VpsService

    settings = Settings.from_env()
    store = WorldStore(settings.data_root, refresh=volume.reload, commit=volume.commit)
    VpsService(store, settings, runner=ModalJobRunner()).run_mapping_job(world_id, map_id, job_id)


@app.function(
    image=image,
    volumes={DATA_ROOT: volume},
    secrets=[api_secret],
    gpu=WEB_GPU,
    cpu=4.0,
    memory=8192,
    scaledown_window=600,
)
@modal.concurrent(max_inputs=8)
@modal.asgi_app()
def web():  # type: ignore[no-untyped-def]
    from app.main import create_app

    return create_app(job_runner=ModalJobRunner(), volume_refresh=volume.reload, volume_commit=volume.commit)
