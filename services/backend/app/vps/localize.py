"""Localization: single query image -> 6DoF camera pose in the map frame.

The scene regressor gives one 2D-3D correspondence per 8x8 pixel cell of the
query image (its centre pixel and the predicted scene coordinate). Those go
into a robust PnP solver (P3P inside LO-RANSAC with a final non-linear
refinement, via PoseLib) which returns the world-to-camera pose plus an inlier
set. The inlier count against the number of correspondences is the confidence
signal, exactly like the "number of inliers" ACE reports.
"""

from __future__ import annotations

import time
from dataclasses import asdict, dataclass
from typing import Any

import numpy as np
import poselib
import torch

from app.vps.camera import Camera, Mat
from app.vps.network import FeatureEncoder, SceneHead, SceneRegressor, feature_cell_pixels
from app.vps.preprocess import Gray, resize_for_network, to_network_tensor


@dataclass(frozen=True)
class LocalizationOptions:
    image_height: int = 480
    max_reproj_error_px: float = 10.0  # inlier threshold, in pixels of the network input image
    min_iterations: int = 64
    max_iterations: int = 5000
    success_probability: float = 0.9999
    min_inlier_count: int = 100
    min_inlier_ratio: float = 0.05

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> LocalizationOptions:
        known = {f for f in cls.__dataclass_fields__}
        return cls(**{k: v for k, v in raw.items() if k in known})


@dataclass(frozen=True)
class LocalizationResult:
    localized: bool
    cam_to_world: Mat | None  # OpenCV camera, map frame
    inlier_count: int
    correspondences: int
    inlier_ratio: float
    ransac_iterations: int
    latency_ms: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "localized": self.localized,
            "inlierCount": self.inlier_count,
            "correspondences": self.correspondences,
            "inlierRatio": self.inlier_ratio,
            "ransacIterations": self.ransac_iterations,
            "latencyMs": self.latency_ms,
        }


def solve_pnp_ransac(
    pixels: Mat, scene_points: Mat, camera: Camera, options: LocalizationOptions
) -> tuple[Mat | None, int, int]:
    """Robust PnP. Returns (cam_to_world or None, inlier count, RANSAC iterations)."""
    if pixels.shape[0] < 4:
        return None, 0, 0
    ransac = {
        "max_reproj_error": options.max_reproj_error_px,
        "min_iterations": options.min_iterations,
        "max_iterations": options.max_iterations,
        "success_prob": options.success_probability,
    }
    pose, info = poselib.estimate_absolute_pose(
        np.ascontiguousarray(pixels, dtype=np.float64),
        np.ascontiguousarray(scene_points, dtype=np.float64),
        camera.poselib_dict(),
        ransac,
        {},
    )
    inliers = int(info.get("num_inliers", 0))
    if inliers < 4:
        return None, inliers, int(info.get("iterations", 0))
    world_to_cam = np.eye(4)
    world_to_cam[:3, :3] = np.asarray(pose.R)
    world_to_cam[:3, 3] = np.asarray(pose.t)
    return np.linalg.inv(world_to_cam), inliers, int(info.get("iterations", 0))


class Localizer:
    def __init__(
        self, encoder: FeatureEncoder, head: SceneHead, device: torch.device, options: LocalizationOptions
    ) -> None:
        self.device = device
        self.options = options
        self.regressor = SceneRegressor(encoder, head).to(device).eval()

    @torch.no_grad()
    def predict_correspondences(self, gray: Gray, camera: Camera) -> tuple[Mat, Mat, Camera]:
        """Returns (pixels (N,2), scene points (N,3), camera of the network input image)."""
        gray, net_camera = resize_for_network(gray, camera.with_pose(None), self.options.image_height)
        scene = self.regressor(to_network_tensor(gray, self.device))[0]  # (3, h, w)
        _, h, w = scene.shape
        pixels = feature_cell_pixels(h, w, self.device).reshape(2, -1).transpose(0, 1)
        points = scene.reshape(3, -1).transpose(0, 1)
        return pixels.cpu().numpy().astype(np.float64), points.cpu().numpy().astype(np.float64), net_camera

    def localize(self, gray: Gray, camera: Camera) -> LocalizationResult:
        start = time.perf_counter()
        pixels, points, net_camera = self.predict_correspondences(gray, camera)
        pose, inliers, iterations = solve_pnp_ransac(pixels, points, net_camera, self.options)
        n = int(pixels.shape[0])
        ratio = inliers / n if n else 0.0
        ok = pose is not None and inliers >= self.options.min_inlier_count and ratio >= self.options.min_inlier_ratio
        return LocalizationResult(
            localized=ok,
            cam_to_world=pose if ok else None,
            inlier_count=inliers,
            correspondences=n,
            inlier_ratio=round(ratio, 4),
            ransac_iterations=iterations,
            latency_ms=round((time.perf_counter() - start) * 1000.0, 1),
        )
