from __future__ import annotations

import numpy as np

from app.vps.localize import LocalizationOptions, solve_pnp_ransac
from app.vps.network import OUTPUT_SUBSAMPLE, feature_cell_pixels
from app.vps.pose import rotation_angle_deg
from tests.synthetic import random_wall_camera, wall_points_for_pixels


def test_pnp_ransac_recovers_pose_with_outliers(rng: np.random.Generator) -> None:
    cam = random_wall_camera(rng, 640, 480)
    import torch

    pixels = feature_cell_pixels(480 // OUTPUT_SUBSAMPLE, 640 // OUTPUT_SUBSAMPLE, torch.device("cpu"))
    pixels = pixels.reshape(2, -1).T.numpy().astype(np.float64)
    points = wall_points_for_pixels(cam, pixels)
    points += rng.normal(scale=0.01, size=points.shape)  # 1 cm noise
    outliers = rng.random(points.shape[0]) < 0.6  # 60 % garbage predictions, like an early ACE head
    points[outliers] = rng.uniform(-3, 3, (int(outliers.sum()), 3))

    pose, inliers, iterations = solve_pnp_ransac(pixels, points, cam.with_pose(None), LocalizationOptions())
    assert pose is not None
    assert inliers > 0.3 * points.shape[0]
    assert iterations >= LocalizationOptions().min_iterations
    assert cam.cam_to_world is not None
    assert np.linalg.norm(pose[:3, 3] - cam.cam_to_world[:3, 3]) < 0.05
    assert rotation_angle_deg(pose[:3, :3], cam.cam_to_world[:3, :3]) < 1.0


def test_pnp_ransac_rejects_pure_noise(rng: np.random.Generator) -> None:
    cam = random_wall_camera(rng, 640, 480)
    pixels = rng.uniform([0, 0], [640, 480], (600, 2))
    points = rng.uniform(-3, 3, (600, 3))
    pose, inliers, _ = solve_pnp_ransac(pixels, points, cam.with_pose(None), LocalizationOptions())
    assert pose is None or inliers < LocalizationOptions().min_inlier_count
