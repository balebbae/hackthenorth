"""Synthetic planar scene used by the tests: a textured wall rendered from known cameras."""

from __future__ import annotations

import math

import cv2
import numpy as np

from app.vps.camera import Camera, Mat, rot_z

WALL_HALF_SIZE = 3.0  # metres; the wall is the z=0 plane, x,y in [-3, 3]


def make_texture(rng: np.random.Generator, size: int = 512) -> np.ndarray:
    """High-frequency but smooth texture so that both encoders and PnP have something to grab."""
    noise = rng.integers(0, 256, (size // 8, size // 8), dtype=np.uint8)
    coarse = cv2.resize(noise, (size, size), interpolation=cv2.INTER_CUBIC)
    fine = rng.integers(0, 256, (size // 2, size // 2), dtype=np.uint8)
    fine = cv2.resize(fine, (size, size), interpolation=cv2.INTER_LINEAR)
    return cv2.addWeighted(coarse, 0.7, fine, 0.3, 0)


def look_at(position: Mat, target: Mat, up: Mat | None = None) -> Mat:
    """OpenCV camera-to-world looking from `position` at `target` (+Y down in the image)."""
    up = np.array([0.0, -1.0, 0.0]) if up is None else up
    forward = target - position
    forward /= np.linalg.norm(forward)
    right = np.cross(forward, up)
    right /= np.linalg.norm(right)
    down = np.cross(forward, right)
    pose = np.eye(4)
    pose[:3, 0], pose[:3, 1], pose[:3, 2], pose[:3, 3] = right, down, forward, position
    return pose


def random_wall_camera(rng: np.random.Generator, width: int, height: int, focal: float | None = None) -> Camera:
    focal = focal or 0.9 * max(width, height)
    intrinsics = np.array(
        [[focal, 0.0, width / 2.0 + rng.uniform(-3, 3)], [0.0, focal, height / 2.0 + rng.uniform(-3, 3)], [0, 0, 1.0]]
    )
    position = np.array([rng.uniform(-1.0, 1.0), rng.uniform(-1.0, 1.0), rng.uniform(-4.5, -3.0)])
    target = np.array([rng.uniform(-0.5, 0.5), rng.uniform(-0.5, 0.5), 0.0])
    pose = look_at(position, target) @ rot_z(math.radians(rng.uniform(-10, 10)))
    return Camera(intrinsics, width, height, pose)


def render_wall(camera: Camera, texture: np.ndarray) -> np.ndarray:
    """Render the textured z=0 wall as seen by `camera` (grayscale uint8)."""
    size = texture.shape[0]
    # Texture pixel (s, t) -> world (x, y, 0).
    scale = 2 * WALL_HALF_SIZE / size
    tex_to_world = np.array([[scale, 0.0, -WALL_HALF_SIZE], [0.0, scale, -WALL_HALF_SIZE], [0.0, 0.0, 1.0]])
    w2c = camera.world_to_cam
    # World (x, y, 0, 1) -> camera: columns 0, 1 and 3 of [R|t].
    plane_to_cam = np.stack([w2c[:3, 0], w2c[:3, 1], w2c[:3, 3]], axis=1)
    homography = camera.intrinsics @ plane_to_cam @ tex_to_world
    return cv2.warpPerspective(
        texture, homography, (camera.width, camera.height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT
    )


def wall_points_for_pixels(camera: Camera, pixels: Mat) -> Mat:
    """Ground-truth 3D points on the wall for query pixels (ray/plane intersection)."""
    pose = camera.cam_to_world
    assert pose is not None
    px = np.concatenate([pixels, np.ones((pixels.shape[0], 1))], axis=1)
    rays_cam = (np.linalg.inv(camera.intrinsics) @ px.T).T
    rays_world = (pose[:3, :3] @ rays_cam.T).T
    origin = pose[:3, 3]
    depth = -origin[2] / rays_world[:, 2]
    return origin + rays_world * depth[:, None]
