from __future__ import annotations

import math

import cv2
import numpy as np
import pytest

from app.vps.camera import (
    Camera,
    arkit_to_cv_pose,
    column_major_to_matrix,
    cv_to_arkit_pose,
    infer_sensor_size,
    matrix_to_column_major,
    rot_z,
)
from app.vps.pose import matrix_to_pose, pose_to_matrix, quaternion_to_rotation, rotation_to_quaternion
from tests.synthetic import random_wall_camera, wall_points_for_pixels


def test_column_major_roundtrip() -> None:
    m = np.arange(16, dtype=np.float64).reshape(4, 4)
    flat = matrix_to_column_major(m)
    assert flat[:4] == [0.0, 4.0, 8.0, 12.0]  # first column
    assert np.allclose(column_major_to_matrix(flat, 4), m)


def test_arkit_identity_camera_looks_down_negative_z() -> None:
    cam = Camera(np.array([[500.0, 0, 320], [0, 500.0, 240], [0, 0, 1]]), 640, 480, arkit_to_cv_pose(np.eye(4)))
    px, depth = cam.project(np.array([[0.0, 0.0, -5.0], [0.5, 0.5, -5.0]]))
    assert depth[0] > 0
    assert np.allclose(px[0], [320, 240])
    assert px[1, 0] > 320 and px[1, 1] < 240  # +X right, +Y up in ARKit world
    assert np.allclose(cv_to_arkit_pose(cam.cam_to_world), np.eye(4))


@pytest.mark.parametrize("rotation", ["cw90", "ccw90", "180"])
def test_rotated_camera_matches_pixel_remap(rng: np.random.Generator, rotation: str) -> None:
    cam = random_wall_camera(rng, 640, 480)
    pixels = rng.uniform([0, 0], [640, 480], (50, 2))
    points = wall_points_for_pixels(cam, pixels)
    rotated = cam.rotated(rotation)  # type: ignore[arg-type]
    projected, depth = rotated.project(points)
    u, v = pixels[:, 0], pixels[:, 1]
    if rotation == "cw90":
        expected = np.stack([480 - v, u], axis=1)
        assert (rotated.width, rotated.height) == (480, 640)
    elif rotation == "ccw90":
        expected = np.stack([v, 640 - u], axis=1)
        assert (rotated.width, rotated.height) == (480, 640)
    else:
        expected = np.stack([640 - u, 480 - v], axis=1)
        assert (rotated.width, rotated.height) == (640, 480)
    assert np.all(depth > 0)
    assert np.allclose(projected, expected, atol=1e-6)


def test_rotated_about_center_matches_cv2_affine(rng: np.random.Generator) -> None:
    cam = random_wall_camera(rng, 640, 480)
    pixels = rng.uniform([0, 0], [640, 480], (50, 2))
    points = wall_points_for_pixels(cam, pixels)
    angle = 12.5
    affine = cam.cv2_rotation_matrix(angle)
    assert np.allclose(affine, cv2.getRotationMatrix2D((320.0, 240.0), angle, 1.0))
    expected = (affine[:, :2] @ pixels.T).T + affine[:, 2]
    projected, _ = cam.rotated_about_center(angle).project(points)
    assert np.allclose(projected, expected, atol=1e-6)


def test_resize_scales_intrinsics(rng: np.random.Generator) -> None:
    cam = random_wall_camera(rng, 640, 480)
    pixels = rng.uniform([0, 0], [640, 480], (20, 2))
    points = wall_points_for_pixels(cam, pixels)
    small = cam.resized_to_height(240)
    assert (small.width, small.height) == (320, 240)
    projected, _ = small.project(points)
    assert np.allclose(projected, pixels / 2.0, atol=1e-6)


def test_from_arkit_full_ios_pipeline(rng: np.random.Generator) -> None:
    """Landscape sensor intrinsics + portrait downscaled upload (what apps/ios sends)."""
    sensor_w, sensor_h = 1920, 1440
    fx, fy, cx, cy = 1500.0, 1500.0, 958.0, 722.0
    intrinsics_col_major = [fx, 0.0, 0.0, 0.0, fy, 0.0, cx, cy, 1.0]
    arkit_pose = np.eye(4)
    arkit_pose[:3, :3] = quaternion_to_rotation([0.1, 0.7, -0.2, 0.68])
    arkit_pose[:3, 3] = [0.3, 1.4, -0.2]
    cam = Camera.from_arkit(
        intrinsics_col_major, sensor_w, sensor_h, 480, 640, "cw90", matrix_to_column_major(arkit_pose)
    )
    assert (cam.width, cam.height) == (480, 640)

    # A point 2 m in front of the ARKit camera (its -Z axis) must land near the image centre with positive depth.
    ahead = arkit_pose @ np.array([0.0, 0.0, -2.0, 1.0])
    px, depth = cam.project(ahead[None, :3])
    assert depth[0] > 0
    scale = 640 / sensor_w
    assert np.allclose(px[0], [(sensor_h - cy) * scale, cx * scale], atol=1e-6)

    # A point to the ARKit camera's +X ends up further down the portrait image (sensor top is on the right).
    right = arkit_pose @ np.array([0.5, 0.0, -2.0, 1.0])
    px_right, _ = cam.project(right[None, :3])
    assert px_right[0, 1] > px[0, 1]
    assert np.isclose(px_right[0, 0], px[0, 0])


def test_infer_sensor_size() -> None:
    intrinsics = np.array([[1500.0, 0, 961.0], [0, 1500.0, 719.0], [0, 0, 1]])
    assert infer_sensor_size(intrinsics, 480, 640, "cw90") == (1920, 1440)
    assert infer_sensor_size(intrinsics, 640, 480, "none") == (1920, 1440)


def test_quaternion_roundtrip(rng: np.random.Generator) -> None:
    for _ in range(50):
        axis = rng.normal(size=3)
        axis /= np.linalg.norm(axis)
        angle = rng.uniform(-math.pi, math.pi)
        rot = rot_z(0.0)[:3, :3]
        k = np.array([[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]])
        rot = np.eye(3) + math.sin(angle) * k + (1 - math.cos(angle)) * k @ k
        q = rotation_to_quaternion(rot)
        assert q[3] >= 0
        assert np.allclose(quaternion_to_rotation(q), rot, atol=1e-9)
        m = np.eye(4)
        m[:3, :3] = rot
        m[:3, 3] = rng.normal(size=3)
        assert np.allclose(pose_to_matrix(matrix_to_pose(m)), m, atol=1e-9)
