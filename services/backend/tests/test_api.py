"""End-to-end through HTTP: upload posed frames the way apps/ios does, map, localize a novel view."""

from __future__ import annotations

import base64
import json
from pathlib import Path

import numpy as np
import pytest
from fastapi.testclient import TestClient

from app.config import Settings
from app.main import create_app
from app.storage import WorldStore
from app.vps.camera import Camera, cv_to_arkit_pose, matrix_to_column_major
from app.vps.network import FeatureEncoder
from app.vps.pose import pose_to_matrix, rotation_angle_deg
from app.vps.preprocess import encode_jpeg
from app.vps.service import FrameUpload, VpsService
from tests.conftest import encoder_path
from tests.synthetic import make_texture, random_wall_camera, render_wall

API_KEY = "test-key"
# "Sensor" is landscape 384x288; the phone rotates it to portrait and downsizes to 144x192 before upload.
SENSOR_W, SENSOR_H = 384, 288
UPLOAD_W, UPLOAD_H = 144, 192
NET_HEIGHT = 192


class InlineRunner:
    """Runs the mapping job synchronously inside the request (deterministic tests)."""

    def __init__(self) -> None:
        self.service: VpsService | None = None

    def submit(self, world_id: str, map_id: str, job_id: str) -> None:
        assert self.service is not None
        self.service.run_mapping_job(world_id, map_id, job_id)


@pytest.fixture
def client(tmp_path: Path, encoder: FeatureEncoder) -> TestClient:
    path = encoder_path()
    assert path is not None
    world_dir = tmp_path / "worlds" / "demo-hall"
    world_dir.mkdir(parents=True)
    (world_dir / "world.json").write_text(
        json.dumps({"id": "demo-hall", "name": "Demo", "version": "v1", "status": "ready", "assets": {}})
    )
    settings = Settings(
        api_key=API_KEY,
        data_root=tmp_path,
        encoder_path=path,
        device="cpu",
        job_runner="thread",
        image_height=NET_HEIGHT,
    )
    runner = InlineRunner()
    app = create_app(settings, store=WorldStore(tmp_path), job_runner=runner)
    runner.service = app.state.vps
    return TestClient(app, headers={"X-API-Key": API_KEY})


def ios_payload(cam_cv: Camera, image: np.ndarray, sequence: int, with_pose: bool = True) -> dict[str, object]:
    """Serialise a (portrait, OpenCV-convention) camera + render into the iOS wire format.

    The phone reports *landscape sensor* intrinsics and an ARKit (OpenGL-axes) transform, then
    uploads a `.oriented(.right)` + downscaled JPEG. Undo those steps to fake the sensor camera.
    """
    assert cam_cv.cam_to_world is not None
    sensor_cam = cam_cv.resized(SENSOR_H, SENSOR_W).rotated("ccw90")  # portrait upload -> landscape sensor
    assert (sensor_cam.width, sensor_cam.height) == (SENSOR_W, SENSOR_H)
    assert sensor_cam.cam_to_world is not None
    payload: dict[str, object] = {
        "sequence": sequence,
        "capturedAt": 1000.0 + sequence,
        "imageBase64": base64.b64encode(encode_jpeg(image)).decode(),
        "imageWidth": UPLOAD_W,
        "imageHeight": UPLOAD_H,
        "intrinsics": matrix_to_column_major(sensor_cam.intrinsics),
        "sensorWidth": SENSOR_W,
        "sensorHeight": SENSOR_H,
        "rotation": "cw90",
    }
    if with_pose:
        payload["cameraTransform"] = matrix_to_column_major(cv_to_arkit_pose(sensor_cam.cam_to_world))
    return payload


def test_auth_required(client: TestClient) -> None:
    assert client.get("/worlds", headers={"X-API-Key": "nope"}).status_code == 401
    assert client.get("/worlds", headers={"X-API-Key": ""}).status_code == 401
    assert client.get("/worlds", headers={"Authorization": f"Bearer {API_KEY}"}).status_code == 200
    assert client.get("/worlds").json() == {
        "worlds": [{"id": "demo-hall", "name": "Demo", "version": "v1", "status": "ready", "assets": {}}]
    }
    assert client.get("/worlds/../etc").status_code in (400, 404)
    assert client.get("/worlds/missing/vps/captures").status_code == 404


def test_ios_payload_roundtrip(rng: np.random.Generator) -> None:
    cam = random_wall_camera(rng, UPLOAD_W, UPLOAD_H)
    payload = ios_payload(cam, np.zeros((UPLOAD_H, UPLOAD_W), np.uint8), 0)
    upload = FrameUpload(
        0, 0.0, b"", UPLOAD_W, UPLOAD_H, payload["intrinsics"], payload["cameraTransform"], SENSOR_W, SENSOR_H, "cw90"
    )  # type: ignore[arg-type]
    back = upload.camera()
    assert (back.width, back.height) == (UPLOAD_W, UPLOAD_H)
    assert np.allclose(back.intrinsics, cam.intrinsics)
    assert back.cam_to_world is not None and cam.cam_to_world is not None
    assert np.allclose(back.cam_to_world, cam.cam_to_world)
    # Without sensor hints the sensor size is inferred from the principal point; the synthetic camera
    # has its principal point up to 3 px off-centre, so expect an error of that order (not a wrong axis).
    inferred = FrameUpload(
        0, 0.0, b"", UPLOAD_W, UPLOAD_H, payload["intrinsics"], payload["cameraTransform"], None, None, "cw90"
    ).camera()  # type: ignore[arg-type]
    assert np.abs(inferred.intrinsics - cam.intrinsics).max() < 6.0
    assert np.allclose(inferred.cam_to_world, cam.cam_to_world)


def test_frame_validation(client: TestClient, rng: np.random.Generator) -> None:
    capture = client.post("/worlds/demo-hall/vps/captures", json={"deviceId": "sim"}).json()
    url = f"/worlds/demo-hall/vps/captures/{capture['captureId']}/frames"
    cam = random_wall_camera(rng, UPLOAD_W, UPLOAD_H)
    image = render_wall(cam, make_texture(rng, 128))
    good = ios_payload(cam, image, 0)
    assert client.post(url, json={**good, "imageBase64": "@@"}).status_code == 400
    assert client.post(url, json={**good, "imageWidth": 50}).status_code == 400
    assert client.post(url, json={**good, "intrinsics": [1.0, 2.0]}).status_code == 422
    assert client.post(url, json=ios_payload(cam, image, 0, with_pose=False)).status_code == 400
    assert client.post(url, json=good).status_code == 201
    assert client.get(f"/worlds/demo-hall/vps/captures/{capture['captureId']}").json()["frameCount"] == 1


def test_map_and_localize_end_to_end(client: TestClient) -> None:
    rng = np.random.default_rng(3)
    texture = make_texture(rng)
    world = "/worlds/demo-hall"

    # No map yet -> 409.
    query_cam = random_wall_camera(rng, UPLOAD_W, UPLOAD_H)
    query = ios_payload(query_cam, render_wall(query_cam, texture), 999)
    assert client.post(f"{world}/vps/localize", json=query).status_code == 409

    capture = client.post(
        f"{world}/vps/captures", json={"deviceId": "sim", "sensorWidth": SENSOR_W, "sensorHeight": SENSOR_H}
    ).json()
    for seq in range(30):
        cam = random_wall_camera(rng, UPLOAD_W, UPLOAD_H)
        r = client.post(
            f"{world}/vps/captures/{capture['captureId']}/frames", json=ios_payload(cam, render_wall(cam, texture), seq)
        )
        assert r.status_code == 201, r.text
    assert client.get(f"{world}/vps/captures").json()["captures"][0]["frameCount"] == 30

    assert client.post(f"{world}/vps/maps", json={"captureIds": ["nope"]}).status_code == 404
    r = client.post(
        f"{world}/vps/maps",
        json={
            "captureIds": [capture["captureId"]],
            "name": "hall-v1",
            "mapping": {
                "buffer_size": 40_000,
                "samples_per_image": 800,
                "batch_size": 2048,
                "epochs": 40,
                "use_half": False,
                "aug_rotation_deg": 10,
                "aug_scale": 1.25,
            },
            "localization": {"min_inlier_count": 100},
        },
    )
    assert r.status_code == 202, r.text
    map_id, job_id = r.json()["map"]["mapId"], r.json()["job"]["jobId"]

    job = client.get(f"{world}/vps/jobs/{job_id}").json()
    assert job["status"] == "succeeded", job
    assert job["progress"] == 1.0
    map_record = client.get(f"{world}/vps/maps/{map_id}").json()
    assert map_record["status"] == "ready"
    assert map_record["stats"]["frames"] == 30
    assert map_record["options"]["image_height"] == NET_HEIGHT
    assert client.get(f"{world}/vps/maps").json()["activeMapId"] == map_id
    manifest = client.get(world).json()
    assert manifest["assets"]["vpsMap"] == f"worlds/demo-hall/vps/maps/{map_id}/head.pt"
    assert client.get(f"{world}/vps/maps/{map_id}/head.pt").status_code == 404  # vps tree is not served as an asset

    # Localize a novel view; the response must be in the (ARKit) map frame. This is a plumbing test on a
    # tiny CPU budget (144x192 px, 4 m wall), so tolerances are loose; accuracy is covered by test_mapping.
    r = client.post(f"{world}/vps/localize", json=query)
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["localized"] is True, body
    assert body["mapId"] == map_id and body["sequence"] == 999
    assert body["inlierCount"] >= 100 and body["correspondences"] == (UPLOAD_W // 8) * (NET_HEIGHT // 8)
    assert query_cam.cam_to_world is not None
    truth = cv_to_arkit_pose(query_cam.cam_to_world)
    estimate = pose_to_matrix(body["pose"])
    assert np.linalg.norm(estimate[:3, 3] - truth[:3, 3]) < 0.6, (estimate[:3, 3], truth[:3, 3])
    assert rotation_angle_deg(estimate[:3, :3], truth[:3, :3]) < 10.0
    assert np.allclose(np.array(body["cameraToMap"]).reshape(4, 4, order="F"), estimate)
    # Query was posed in the same frame as the map, so session->map must be ~identity.
    map_from_session = np.array(body["mapFromSession"]).reshape(4, 4, order="F")
    assert np.linalg.norm(map_from_session[:3, 3]) < 0.6
    assert rotation_angle_deg(map_from_session[:3, :3], np.eye(3)) < 10.0

    # Unposed query (pure image query) still returns a 6DoF pose, just no session anchor.
    r = client.post(
        f"{world}/vps/localize", json=ios_payload(query_cam, render_wall(query_cam, texture), 1000, with_pose=False)
    )
    assert r.status_code == 200 and r.json()["localized"] is True
    assert r.json()["mapFromSession"] is None and r.json()["pose"] is not None

    # An image of something else must not localize.
    other = render_wall(query_cam, make_texture(np.random.default_rng(77)))
    r = client.post(f"{world}/vps/localize", json=ios_payload(query_cam, other, 1001))
    assert r.status_code == 200
    assert r.json()["localized"] is False and r.json()["pose"] is None, r.json()
