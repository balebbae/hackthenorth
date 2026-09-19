# Wander backend (FastAPI on Modal)

The service that fronts the `wander-worlds` Modal Volume (`shared/contracts/worlds-api.openapi.yaml`) and hosts
Wander's self-hosted **visual positioning system**: build a map of a space from posed phone frames, then
localize a single photo to a 6DoF camera pose in that map — the same shape of capability as Niantic's VPS,
but running on our own Modal GPU.

```text
app/
  main.py            create_app(): FastAPI factory, mounts routers, /healthz
  config.py          Settings (WANDER_* env vars)
  auth.py            X-API-Key (or Authorization: Bearer) check
  storage.py         WorldStore: worlds/<id>/... layout on the Volume, atomic JSON writes
  api/worlds.py      GET /worlds, GET /worlds/{id}, GET /worlds/{id}/{version}/{file}
  api/vps.py         /worlds/{id}/vps/* (captures, maps, jobs, localize)
  vps/
    camera.py        ARKit (OpenGL, column-major) <-> OpenCV cameras, portrait rotation, intrinsics rescale
    pose.py          4x4 <-> {position, rotation[x,y,z,w]} (navigation.schema.json pose)
    network.py       ACE feature encoder (frozen, pretrained) + per-scene SceneHead
    preprocess.py    JPEG -> grayscale -> normalised tensor
    mapping.py       train_scene_head(): feature buffer + reprojection-loss training
    localize.py      Localizer: dense scene coordinates -> PoseLib PnP-RANSAC
    service.py       VpsService: captures, mapping jobs, active map, localize, session anchoring
deployment/modal_app.py   Modal app: `web` (ASGI) + `train_map` (GPU) sharing the Volume
tests/                    synthetic textured-wall scene; end-to-end mapping + localization on CPU
```

## Method

Mapping and localization follow **ACE – Accelerated Coordinate Encoding** (Brachmann, Cavallari, Prisacariu,
*Learning to Relocalize in Minutes using RGB and Poses*, CVPR 2023; <https://nianticlabs.github.io/ace/>),
the scene-coordinate-regression approach Niantic published for its own relocalization research:

1. **Mapping.** Every posed frame is run through a frozen, scene-agnostic convolutional encoder
   (512-d features at 1/8 resolution). Features from all frames — with rotation/scale/intensity augmentation —
   are shuffled into one training buffer and a small per-scene MLP head is trained for a few minutes to regress
   the 3D **map coordinate** of every feature cell, supervised only by the frame poses through a robust
   reprojection loss (no depth, no SfM point cloud). The head (`head.pt`, a few MB) *is* the map.
2. **Localization.** A query image goes through the same encoder and head, giving a dense set of
   2D→3D correspondences; PnP-RANSAC (PoseLib, LO-RANSAC) returns the 6DoF camera pose plus inlier
   statistics used to accept or reject the fix.

The **map frame is the ARKit world frame of the capture** that produced the map. A localization response
therefore contains the camera pose in that frame (`pose`, `cameraToMap`) and, when the query also carried the
phone's *current* `ARCamera.transform`, `mapFromSession` — the rigid transform from the phone's current ARKit
session into the map, so tracking continues locally between fixes exactly like a Lightship VPS anchor.

Camera conventions are handled in `vps/camera.py`: ARKit poses are OpenGL-style (+Y up, −Z forward) and
column-major; internally everything is OpenCV (+Y down, +Z forward). The iOS `FrameEncoder` rotates the
landscape sensor image 90° CW and downsizes it before upload, so the server folds that rotation and resize
into the intrinsics/pose it trains and localizes with (`tests/test_camera.py`, `tests/test_api.py` round-trip
the exact wire format of `LocalizationTransport.swift`).

### Pretrained encoder

The scene-agnostic encoder weights are **not** in this repository. The Modal image downloads
`ace_encoder_pretrained.pt` (~22 MB) at build time from `WANDER_ACE_ENCODER_URL` (defaults to the checkpoint in
the public ACE repo). That checkpoint is released by Niantic under a **non-commercial licence** — fine for the
hackathon, but point the variable at your own weights (or ones with a suitable licence) before any commercial
use. Locally, set `WANDER_ACE_ENCODER_PATH`; the tests download to `~/.cache/wander/` if it is unset.

## API

All routes need `X-API-Key: $WANDER_API_KEY` (the iOS app's `Authorization: Bearer <key>` is accepted too).
Schemas: `shared/contracts/vps.schema.json`.

| Route | Purpose |
| --- | --- |
| `POST /worlds/{id}/vps/captures` | start a mapping walk-through (optional `sensorWidth/Height`, `rotation`) |
| `POST /worlds/{id}/vps/captures/{captureId}/frames` | append a posed frame — same JSON the phone already sends for localization |
| `POST /worlds/{id}/vps/maps` | train a map from one or more captures (async GPU job) → `202 {map, job}` |
| `GET /worlds/{id}/vps/jobs/{jobId}` | job status / progress / loss curve |
| `GET /worlds/{id}/vps/maps`, `POST …/maps/{mapId}/activate` | list maps; choose the one queries use (first success auto-activates) |
| `POST /worlds/{id}/vps/localize` | image query → `{localized, pose, cameraToMap, mapFromSession, inlierCount, …}` |

A typical mapping session from the phone: `POST …/captures`, stream 1–2 posed frames/s while walking the space
(a few hundred frames), `POST …/maps`, poll the job (≈2–5 min on an A10G with the defaults), then switch the
localization loop to `POST …/vps/localize`.

## Run locally

```bash
cd services/backend
python -m venv .venv && . .venv/bin/activate
pip install -e ".[dev,modal]"          # CPU torch is fine for tests and small maps
export WANDER_API_KEY=dev WANDER_DATA_ROOT=/tmp/wander WANDER_ACE_ENCODER_PATH=~/.cache/wander/ace_encoder_pretrained.pt
uvicorn app.main:app --reload
```

Quality gates: `ruff check . && ruff format --check . && mypy && pytest` (the mapping/API tests need the pretrained
encoder and take ~2 minutes on CPU; they skip if the checkpoint cannot be found or downloaded).

## Deploy to Modal

```bash
modal secret create wander-api WANDER_API_KEY=<shared secret>
modal deploy deployment/modal_app.py
```

* `web` — CPU container (set `WANDER_WEB_GPU=T4` for lower localization latency) serving the FastAPI app.
* `train_map` — GPU container (`WANDER_TRAIN_GPU`, default `A10G`) spawned per mapping job; progress is
  exchanged through the job record on the Volume.
* Volume: `wander-worlds` mounted at `/data`, layout in `shared/contracts/README.md`.

## Caveats

* Accuracy has only been verified on the synthetic scene in `tests/` (novel views localize to ~0.1 m / 1–3°
  at very low resolution). Real indoor captures still need an evaluation pass before trusting the poses for
  guidance.
* Scene-coordinate regression always produces *some* correspondences; only trust `localized: true`, and tune
  `min_inlier_count` / `min_inlier_ratio` per map (`localization` overrides on `POST …/maps`).
* Maps are tied to the ARKit frame of one capture. Merging several captures into one map assumes they were
  taken in the same ARKit session (or pre-aligned).
