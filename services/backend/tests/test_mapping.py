from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import pytest
import torch

from app.vps.camera import Camera
from app.vps.localize import LocalizationOptions, Localizer
from app.vps.mapping import MappingFrame, MappingOptions, train_scene_head
from app.vps.network import FeatureEncoder, SceneHead
from app.vps.pose import rotation_angle_deg
from app.vps.preprocess import encode_jpeg
from tests.synthetic import make_texture, random_wall_camera, render_wall

WIDTH, HEIGHT = 192, 144
CPU = torch.device("cpu")


def _render_frames(tmp_path: Path, rng: np.random.Generator, texture: np.ndarray, count: int) -> list[MappingFrame]:
    frames = []
    for i in range(count):
        cam = random_wall_camera(rng, WIDTH, HEIGHT)
        path = tmp_path / f"{i:03d}.jpg"
        path.write_bytes(encode_jpeg(render_wall(cam, texture)))
        frames.append(MappingFrame(path, cam))
    return frames


@pytest.fixture(scope="module")
def trained(
    tmp_path_factory: pytest.TempPathFactory, encoder: FeatureEncoder
) -> tuple[SceneHead, FeatureEncoder, np.ndarray, list[MappingFrame]]:
    rng = np.random.default_rng(7)
    texture = make_texture(rng)
    frames = _render_frames(tmp_path_factory.mktemp("frames"), rng, texture, 40)
    options = MappingOptions(
        image_height=HEIGHT,
        buffer_size=40_000,
        samples_per_image=800,
        batch_size=2048,
        epochs=int(os.environ.get("WANDER_TEST_EPOCHS", "40")),
        aug_rotation_deg=10.0,
        aug_scale=1.25,
        use_half=False,
    )
    progress: list[float] = []
    head, stats = train_scene_head(frames, encoder, options, CPU, lambda phase, frac, _d: progress.append(frac))
    assert stats.buffer_samples == options.buffer_size
    assert stats.iterations == options.iterations
    assert progress and progress[-1] == 1.0
    assert stats.loss_curve[-1] < stats.loss_curve[0]
    return head, encoder, texture, frames


def test_head_export_roundtrip(
    trained: tuple[SceneHead, FeatureEncoder, np.ndarray, list[MappingFrame]], tmp_path: Path
) -> None:
    head, *_ = trained
    torch.save(head.export(), tmp_path / "head.pt")
    restored = SceneHead.from_export(torch.load(tmp_path / "head.pt", weights_only=True))
    x = torch.randn(1, 512, 4, 4)
    assert torch.allclose(restored(x), head(x))


def test_localizes_novel_views(trained: tuple[SceneHead, FeatureEncoder, np.ndarray, list[MappingFrame]]) -> None:
    head, encoder, texture, _frames = trained
    rng = np.random.default_rng(99)
    localizer = Localizer(encoder, head, CPU, LocalizationOptions(image_height=HEIGHT, min_inlier_count=40))
    translation_errors, rotation_errors, successes = [], [], 0
    for _ in range(6):
        cam = random_wall_camera(rng, WIDTH, HEIGHT)
        result = localizer.localize(render_wall(cam, texture), cam.with_pose(None))
        assert result.correspondences == (WIDTH // 8) * (HEIGHT // 8)
        if result.localized and result.cam_to_world is not None:
            assert cam.cam_to_world is not None
            successes += 1
            translation_errors.append(float(np.linalg.norm(result.cam_to_world[:3, 3] - cam.cam_to_world[:3, 3])))
            rotation_errors.append(rotation_angle_deg(result.cam_to_world[:3, :3], cam.cam_to_world[:3, :3]))
    assert successes >= 4, (successes, translation_errors, rotation_errors)
    assert np.median(translation_errors) < 0.25, translation_errors
    assert np.median(rotation_errors) < 5.0, rotation_errors


def test_training_rejects_frames_without_pose(tmp_path: Path) -> None:
    cam = Camera(np.eye(3), 8, 8, None)
    with pytest.raises(ValueError):
        train_scene_head([MappingFrame(tmp_path / "x.jpg", cam)], FeatureEncoder(), MappingOptions(), CPU)
