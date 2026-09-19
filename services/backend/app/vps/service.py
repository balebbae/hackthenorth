"""Orchestration between the HTTP layer, the Volume layout and the ACE pipeline.

Records (all JSON on the Volume, see storage.py for paths):

* capture  - one phone recording session; frames share the same ARKit world.
* frame    - one uploaded JPEG + its camera (OpenCV convention, map frame).
* map      - a trained scene head for one or more captures.
* job      - progress/status of a mapping run (thread locally, GPU function on Modal).

The *map frame* of a world is the ARKit world frame of the capture(s) a map was
trained from. Query results are expressed in that frame; the phone turns the
returned `mapFromSession` transform into an anchor for its own ARKit session.
"""

from __future__ import annotations

import base64
import binascii
import logging
import threading
import traceback
from collections.abc import Callable
from dataclasses import dataclass, replace
from typing import Any, Protocol

import numpy as np
import torch

from app.config import Settings
from app.storage import WorldStore, new_id, now_iso
from app.vps.camera import Camera, Rotation, cv_to_arkit_pose, infer_sensor_size, matrix_to_column_major
from app.vps.localize import LocalizationOptions, LocalizationResult, Localizer
from app.vps.mapping import MappingFrame, MappingOptions, train_scene_head
from app.vps.network import FeatureEncoder, SceneHead, load_encoder, resolve_device
from app.vps.pose import matrix_to_pose
from app.vps.preprocess import decode_grayscale

log = logging.getLogger(__name__)


class VpsError(Exception):
    def __init__(self, status: int, detail: str) -> None:
        super().__init__(detail)
        self.status = status
        self.detail = detail


@dataclass(frozen=True)
class FrameUpload:
    """Decoded request for one frame (mapping upload or query); mirrors the iOS `LocalizationQuery` JSON."""

    sequence: int
    captured_at: float
    image: bytes
    image_width: int
    image_height: int
    intrinsics: list[float]  # 3x3 column-major, ARKit sensor image
    camera_transform: list[float] | None  # 4x4 column-major, ARKit camera-to-world
    sensor_width: int | None = None
    sensor_height: int | None = None
    rotation: Rotation = "cw90"

    @staticmethod
    def decode_image(image_base64: str) -> bytes:
        try:
            return base64.b64decode(image_base64, validate=True)
        except (binascii.Error, ValueError) as exc:
            raise VpsError(400, "imageBase64 is not valid base64") from exc

    def camera(self) -> Camera:
        intrinsics = np.asarray(self.intrinsics, dtype=np.float64).reshape(3, 3, order="F")
        if self.sensor_width and self.sensor_height:
            sensor = (self.sensor_width, self.sensor_height)
        else:
            sensor = infer_sensor_size(intrinsics, self.image_width, self.image_height, self.rotation)
        return Camera.from_arkit(
            self.intrinsics,
            sensor[0],
            sensor[1],
            self.image_width,
            self.image_height,
            self.rotation,
            self.camera_transform,
        )


class JobRunner(Protocol):
    def submit(self, world_id: str, map_id: str, job_id: str) -> None: ...


class ThreadJobRunner:
    """Runs mapping in a daemon thread of the API process (local development)."""

    def __init__(self, run: Callable[[str, str, str], None]) -> None:
        self._run = run

    def submit(self, world_id: str, map_id: str, job_id: str) -> None:
        threading.Thread(target=self._run, args=(world_id, map_id, job_id), daemon=True).start()


class VpsService:
    def __init__(self, store: WorldStore, settings: Settings, runner: JobRunner | None = None) -> None:
        self.store = store
        self.settings = settings
        self.device = resolve_device(settings.device)
        self.runner: JobRunner = runner or ThreadJobRunner(self.run_mapping_job)
        self._encoder: FeatureEncoder | None = None
        self._localizers: dict[tuple[str, str], tuple[float, Localizer]] = {}
        self._lock = threading.Lock()

    # ------------------------------------------------------------------ models

    def encoder(self) -> FeatureEncoder:
        with self._lock:
            if self._encoder is None:
                path = self.settings.encoder_path
                if path is None or not path.is_file():
                    raise VpsError(503, "pretrained encoder not available (set WANDER_ACE_ENCODER_PATH)")
                self._encoder = load_encoder(path, self.device)
            return self._encoder

    def localizer(self, world_id: str, map_id: str) -> Localizer:
        record = self.get_map(world_id, map_id)
        if record["status"] != "ready":
            raise VpsError(409, f"map {map_id} is {record['status']}")
        head_path = self.store.head_path(world_id, map_id)
        mtime = head_path.stat().st_mtime
        key = (world_id, map_id)
        with self._lock:
            cached = self._localizers.get(key)
            if cached and cached[0] == mtime:
                return cached[1]
        head = SceneHead.from_export(torch.load(head_path, map_location="cpu", weights_only=True))
        options = LocalizationOptions.from_dict(record.get("localization", {}))
        localizer = Localizer(self.encoder(), head, self.device, options)
        with self._lock:
            self._localizers[key] = (mtime, localizer)
        return localizer

    # ---------------------------------------------------------------- captures

    def require_world(self, world_id: str) -> None:
        if not self.store.world_exists(world_id):
            raise VpsError(404, f"world {world_id} not found")

    def create_capture(
        self, world_id: str, device_id: str | None, sensor: tuple[int, int] | None, rotation: Rotation
    ) -> dict[str, Any]:
        self.require_world(world_id)
        capture_id = new_id("cap")
        record = {
            "captureId": capture_id,
            "worldId": world_id,
            "deviceId": device_id,
            "sensorWidth": sensor[0] if sensor else None,
            "sensorHeight": sensor[1] if sensor else None,
            "rotation": rotation,
            "frameCount": 0,
            "lastSequence": None,
            "createdAt": now_iso(),
            "updatedAt": now_iso(),
        }
        self.store.write_record(self.store.capture_dir(world_id, capture_id) / "capture.json", record)
        self.store.commit()
        return record

    def get_capture(self, world_id: str, capture_id: str) -> dict[str, Any]:
        record = self.store.read_record(self.store.capture_dir(world_id, capture_id) / "capture.json")
        if record is None:
            raise VpsError(404, f"capture {capture_id} not found")
        return record

    def list_captures(self, world_id: str) -> list[dict[str, Any]]:
        self.require_world(world_id)
        root = self.store.vps_dir(world_id) / "captures"
        return [self.get_capture(world_id, cid) for cid in self.store.list_record_ids(root)]

    def add_frame(self, world_id: str, capture_id: str, upload: FrameUpload) -> dict[str, Any]:
        capture = self.get_capture(world_id, capture_id)
        if upload.camera_transform is None:
            raise VpsError(400, "mapping frames need cameraTransform")
        if not upload.sensor_width and capture.get("sensorWidth") and capture.get("sensorHeight"):
            upload = replace(upload, sensor_width=capture["sensorWidth"], sensor_height=capture["sensorHeight"])
        gray = self._decode_checked(upload)
        camera = upload.camera()
        assert camera.cam_to_world is not None
        self.store.write_bytes(self.store.frame_image_path(world_id, capture_id, upload.sequence), upload.image)
        frame = {
            "sequence": upload.sequence,
            "capturedAt": upload.captured_at,
            "width": gray.shape[1],
            "height": gray.shape[0],
            "intrinsics": camera.intrinsics.tolist(),
            "camToWorld": camera.cam_to_world.tolist(),
        }
        self.store.append_jsonl(self.store.frames_index_path(world_id, capture_id), frame)
        capture["frameCount"] = int(capture.get("frameCount", 0)) + 1
        capture["lastSequence"] = upload.sequence
        capture["updatedAt"] = now_iso()
        self.store.write_record(self.store.capture_dir(world_id, capture_id) / "capture.json", capture)
        self.store.commit()
        return {"captureId": capture_id, "sequence": upload.sequence, "frameCount": capture["frameCount"]}

    def _decode_checked(self, upload: FrameUpload) -> np.ndarray:
        try:
            gray = decode_grayscale(upload.image)
        except ValueError as exc:
            raise VpsError(400, str(exc)) from exc
        if gray.shape[1] != upload.image_width or gray.shape[0] != upload.image_height:
            raise VpsError(
                400,
                f"image is {gray.shape[1]}x{gray.shape[0]} but imageWidth/imageHeight say "
                f"{upload.image_width}x{upload.image_height}",
            )
        return gray

    def mapping_frames(self, world_id: str, capture_ids: list[str]) -> list[MappingFrame]:
        frames: list[MappingFrame] = []
        for capture_id in capture_ids:
            self.get_capture(world_id, capture_id)
            for record in self.store.iter_jsonl(self.store.frames_index_path(world_id, capture_id)):
                camera = Camera(
                    np.asarray(record["intrinsics"], dtype=np.float64),
                    int(record["width"]),
                    int(record["height"]),
                    np.asarray(record["camToWorld"], dtype=np.float64),
                )
                frames.append(
                    MappingFrame(self.store.frame_image_path(world_id, capture_id, int(record["sequence"])), camera)
                )
        return frames

    # -------------------------------------------------------------------- maps

    def get_map(self, world_id: str, map_id: str) -> dict[str, Any]:
        record = self.store.read_record(self.store.map_dir(world_id, map_id) / "map.json")
        if record is None:
            raise VpsError(404, f"map {map_id} not found")
        return record

    def list_maps(self, world_id: str) -> list[dict[str, Any]]:
        self.require_world(world_id)
        root = self.store.vps_dir(world_id) / "maps"
        return [self.get_map(world_id, mid) for mid in self.store.list_record_ids(root)]

    def get_job(self, world_id: str, job_id: str) -> dict[str, Any]:
        record = self.store.read_record(self.store.job_path(world_id, job_id))
        if record is None:
            raise VpsError(404, f"job {job_id} not found")
        return record

    def active_map_id(self, world_id: str) -> str | None:
        record = self.store.read_record(self.store.active_map_path(world_id))
        return None if record is None else str(record.get("mapId"))

    def activate_map(self, world_id: str, map_id: str) -> dict[str, Any]:
        record = self.get_map(world_id, map_id)
        if record["status"] != "ready":
            raise VpsError(409, f"map {map_id} is {record['status']}")
        self.store.write_record(self.store.active_map_path(world_id), {"mapId": map_id, "activatedAt": now_iso()})
        manifest = self.store.read_manifest(world_id)
        if manifest is not None:
            assets = dict(manifest.get("assets") or {})
            assets["vpsMap"] = str(self.store.head_path(world_id, map_id).relative_to(self.store.root))
            manifest["assets"] = assets
            manifest["updatedAt"] = now_iso()
            self.store.write_manifest(world_id, manifest)
        self.store.commit()
        return record

    def start_mapping(
        self,
        world_id: str,
        capture_ids: list[str],
        options: MappingOptions,
        localization: LocalizationOptions,
        name: str | None = None,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        self.require_world(world_id)
        if self.settings.encoder_path is None or not self.settings.encoder_path.is_file():
            raise VpsError(503, "pretrained encoder not available (set WANDER_ACE_ENCODER_PATH)")
        total = 0
        for capture_id in capture_ids:
            total += int(self.get_capture(world_id, capture_id).get("frameCount", 0))
        if total == 0:
            raise VpsError(409, "captures contain no frames")
        map_id = new_id("map")
        job_id = new_id("job")
        map_record = {
            "mapId": map_id,
            "worldId": world_id,
            "name": name,
            "captureIds": capture_ids,
            "frameCount": total,
            "status": "pending",
            "jobId": job_id,
            "options": options.to_dict(),
            "localization": localization.to_dict(),
            "stats": None,
            "error": None,
            "createdAt": now_iso(),
            "updatedAt": now_iso(),
        }
        job_record = {
            "jobId": job_id,
            "worldId": world_id,
            "mapId": map_id,
            "status": "pending",
            "phase": "queued",
            "progress": 0.0,
            "detail": {},
            "error": None,
            "createdAt": now_iso(),
            "updatedAt": now_iso(),
            "finishedAt": None,
        }
        self.store.write_record(self.store.map_dir(world_id, map_id) / "map.json", map_record)
        self.store.write_record(self.store.job_path(world_id, job_id), job_record)
        self.store.commit()
        self.runner.submit(world_id, map_id, job_id)
        return map_record, job_record

    def run_mapping_job(self, world_id: str, map_id: str, job_id: str) -> None:
        """Entry point for the worker (thread or Modal function). Never raises."""
        self.store.refresh()
        job = self.get_job(world_id, job_id)
        map_record = self.get_map(world_id, map_id)

        def update_job(
            status: str, phase: str, progress: float, detail: dict[str, Any], error: str | None = None
        ) -> None:
            job.update(
                status=status, phase=phase, progress=round(progress, 4), detail=detail, error=error, updatedAt=now_iso()
            )
            if status in ("succeeded", "failed"):
                job["finishedAt"] = now_iso()
            self.store.write_record(self.store.job_path(world_id, job_id), job)

        last_flush = {"value": -1.0}

        def progress(phase: str, fraction: float, detail: dict[str, Any]) -> None:
            if fraction - last_flush["value"] >= 0.01 or fraction >= 1.0:
                last_flush["value"] = fraction
                update_job("running", phase, fraction, detail)
                self.store.commit()

        try:
            map_record.update(status="running", updatedAt=now_iso())
            self.store.write_record(self.store.map_dir(world_id, map_id) / "map.json", map_record)
            update_job("running", "loading", 0.0, {})
            self.store.commit()

            options = MappingOptions.from_dict(map_record["options"])
            frames = self.mapping_frames(world_id, map_record["captureIds"])
            head, stats = train_scene_head(frames, self.encoder(), options, self.device, progress)

            torch.save(head.export(), self.store.head_path(world_id, map_id))
            map_record.update(status="ready", stats=stats.to_dict(), updatedAt=now_iso())
            self.store.write_record(self.store.map_dir(world_id, map_id) / "map.json", map_record)
            update_job("succeeded", "done", 1.0, {"stats": stats.to_dict()})
            if self.active_map_id(world_id) is None:
                self.activate_map(world_id, map_id)
        except Exception as exc:  # noqa: BLE001 - job status must always be written
            log.exception("mapping job %s failed", job_id)
            message = f"{type(exc).__name__}: {exc}"
            map_record.update(status="failed", error=message, updatedAt=now_iso())
            self.store.write_record(self.store.map_dir(world_id, map_id) / "map.json", map_record)
            update_job(
                "failed", "error", job.get("progress", 0.0), {"traceback": traceback.format_exc()[-4000:]}, message
            )
        finally:
            self.store.commit()

    # ---------------------------------------------------------------- queries

    def localize(self, world_id: str, upload: FrameUpload, map_id: str | None) -> dict[str, Any]:
        self.require_world(world_id)
        self.store.refresh()
        map_id = map_id or self.active_map_id(world_id)
        if map_id is None:
            raise VpsError(409, "world has no active VPS map")
        localizer = self.localizer(world_id, map_id)
        gray = self._decode_checked(upload)
        camera = upload.camera()
        result = localizer.localize(gray, camera)
        return self._response(result, map_id, camera, upload.sequence)

    @staticmethod
    def _response(result: LocalizationResult, map_id: str, query_camera: Camera, sequence: int) -> dict[str, Any]:
        response: dict[str, Any] = {"mapId": map_id, "sequence": sequence, **result.to_dict()}
        if result.cam_to_world is None:
            response.update(pose=None, cameraToMap=None, mapFromSession=None)
            return response
        cam_to_map_arkit = cv_to_arkit_pose(result.cam_to_world)
        response["pose"] = matrix_to_pose(cam_to_map_arkit)
        response["cameraToMap"] = matrix_to_column_major(cam_to_map_arkit)
        # T_map<-session = T_map<-cam * (T_session<-cam)^-1 : anchors the phone's live ARKit session in the map.
        if query_camera.cam_to_world is not None:
            session_cam_arkit = cv_to_arkit_pose(query_camera.cam_to_world)
            response["mapFromSession"] = matrix_to_column_major(cam_to_map_arkit @ np.linalg.inv(session_cam_arkit))
        else:
            response["mapFromSession"] = None
        return response
