"""Camera models and frame conventions.

Internally every camera is an OpenCV pinhole: +X right, +Y down, +Z forward,
pixel `(u, v)` with `u` along the image width. Poses are camera-to-world 4x4
matrices. "World" is the *map frame*: the ARKit world of the capture session
that produced the map (gravity aligned, +Y up, metres).

ARKit hands out camera-to-world transforms in the OpenGL convention (+X right,
+Y up, -Z forward) with intrinsics expressed in the landscape sensor image, while
the iOS client uploads a portrait, downscaled JPEG. `Camera.from_arkit` folds the
axis flip, the 90 degree rotation and the rescale into a single consistent model.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, replace
from typing import Literal

import numpy as np
from numpy.typing import NDArray

Mat = NDArray[np.float64]
Rotation = Literal["none", "cw90", "ccw90", "180"]

# ARKit/OpenGL camera axes -> OpenCV camera axes (flip Y and Z). Involutory.
ARKIT_TO_CV: Mat = np.diag([1.0, -1.0, -1.0, 1.0])


def column_major_to_matrix(values: list[float] | tuple[float, ...], n: int) -> Mat:
    """simd_floatNxN flattened column by column (what `SIMD` / `Swift` emit) -> row-major ndarray."""
    arr = np.asarray(values, dtype=np.float64)
    if arr.size != n * n:
        raise ValueError(f"expected {n * n} values, got {arr.size}")
    return np.array(arr.reshape((n, n), order="F"))


def matrix_to_column_major(matrix: Mat) -> list[float]:
    return [float(v) for v in np.asarray(matrix, dtype=np.float64).flatten(order="F")]


def rot_z(angle_rad: float) -> Mat:
    c, s = math.cos(angle_rad), math.sin(angle_rad)
    return np.array([[c, -s, 0.0, 0.0], [s, c, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])


def arkit_to_cv_pose(cam_to_world_arkit: Mat) -> Mat:
    """ARKit camera-to-world (OpenGL axes) -> OpenCV camera-to-world in the same world."""
    return np.asarray(cam_to_world_arkit, dtype=np.float64) @ ARKIT_TO_CV


def cv_to_arkit_pose(cam_to_world_cv: Mat) -> Mat:
    return np.asarray(cam_to_world_cv, dtype=np.float64) @ ARKIT_TO_CV


def infer_sensor_size(intrinsics: Mat, image_width: int, image_height: int, rotation: Rotation) -> tuple[int, int]:
    """Best-effort sensor size when the client did not send one.

    ARKit's principal point sits within a few pixels of the sensor centre, so
    `2 * (cx, cy)` recovers the calibration image size closely enough for a
    <0.5 % focal-length error. The aspect ratio of the uploaded image is used to
    keep the pair self-consistent.
    """
    cx, cy = float(intrinsics[0, 2]), float(intrinsics[1, 2])
    if rotation in ("cw90", "ccw90"):
        target_w, target_h = image_height, image_width  # undo the rotation
    else:
        target_w, target_h = image_width, image_height
    scale = (target_w / (2.0 * cx) + target_h / (2.0 * cy)) / 2.0
    return int(round(target_w / scale)), int(round(target_h / scale))


@dataclass(frozen=True)
class Camera:
    """Pinhole camera (OpenCV convention) with an optional camera-to-world pose."""

    intrinsics: Mat
    width: int
    height: int
    cam_to_world: Mat | None = None

    # -- Construction ---------------------------------------------------------

    @classmethod
    def from_arkit(
        cls,
        intrinsics_col_major: list[float],
        sensor_width: int,
        sensor_height: int,
        image_width: int,
        image_height: int,
        rotation: Rotation = "cw90",
        camera_transform_col_major: list[float] | None = None,
    ) -> Camera:
        """Build the camera of an uploaded frame.

        `intrinsics_col_major` and `camera_transform_col_major` are ARKit's
        `intrinsics` / `transform` for the landscape sensor image of size
        `sensor_width x sensor_height`. The uploaded image was rotated by
        `rotation` and then resized to `image_width x image_height`.
        """
        pose = None
        if camera_transform_col_major is not None:
            pose = arkit_to_cv_pose(column_major_to_matrix(camera_transform_col_major, 4))
        cam = cls(column_major_to_matrix(intrinsics_col_major, 3), sensor_width, sensor_height, pose)
        cam = cam.rotated(rotation)
        return cam.resized(image_width, image_height)

    # -- Derived cameras ------------------------------------------------------

    def with_pose(self, cam_to_world: Mat | None) -> Camera:
        return replace(self, cam_to_world=None if cam_to_world is None else np.asarray(cam_to_world, dtype=np.float64))

    def resized(self, width: int, height: int) -> Camera:
        sx, sy = width / self.width, height / self.height
        scale = np.array([[sx, 0.0, 0.0], [0.0, sy, 0.0], [0.0, 0.0, 1.0]])
        return replace(self, intrinsics=scale @ self.intrinsics, width=width, height=height)

    def resized_to_height(self, height: int) -> Camera:
        width = int(round(self.width * height / self.height))
        return self.resized(width, height)

    def rotated(self, rotation: Rotation) -> Camera:
        """Camera of the image rotated by a multiple of 90 degrees (image content rotates, scene does not)."""
        if rotation == "none":
            return self
        fx, fy = self.intrinsics[0, 0], self.intrinsics[1, 1]
        cx, cy = self.intrinsics[0, 2], self.intrinsics[1, 2]
        w, h = self.width, self.height
        if rotation == "cw90":  # (u, v) -> (h - v, u); new camera axes: x' = -y, y' = x
            k = np.array([[fy, 0.0, h - cy], [0.0, fx, cx], [0.0, 0.0, 1.0]])
            new_w, new_h, angle = h, w, math.pi / 2
        elif rotation == "ccw90":  # (u, v) -> (v, w - u); x' = y, y' = -x
            k = np.array([[fy, 0.0, cy], [0.0, fx, w - cx], [0.0, 0.0, 1.0]])
            new_w, new_h, angle = h, w, -math.pi / 2
        elif rotation == "180":  # (u, v) -> (w - u, h - v); x' = -x, y' = -y
            k = np.array([[fx, 0.0, w - cx], [0.0, fy, h - cy], [0.0, 0.0, 1.0]])
            new_w, new_h, angle = w, h, math.pi
        else:
            raise ValueError(f"unknown rotation {rotation!r}")
        # New camera coordinates are X' = Rz(angle) X, so cam'->world = cam->world @ Rz(-angle).
        pose = None if self.cam_to_world is None else self.cam_to_world @ rot_z(-angle)
        return Camera(k, new_w, new_h, pose)

    def rotated_about_center(self, angle_deg: float) -> Camera:
        """Camera of the image rotated by `angle_deg` counter-clockwise about its centre (cv2 convention).

        Used for mapping-time augmentation. Assumes fx ~ fy, which holds for phone cameras.
        """
        theta = math.radians(angle_deg)
        c, s = math.cos(theta), math.sin(theta)
        centre = np.array([self.width / 2.0, self.height / 2.0])
        principal = np.array([self.intrinsics[0, 2], self.intrinsics[1, 2]])
        rot2 = np.array([[c, s], [-s, c]])
        new_principal = rot2 @ (principal - centre) + centre
        k = self.intrinsics.copy()
        k[0, 2], k[1, 2] = new_principal
        pose = None if self.cam_to_world is None else self.cam_to_world @ rot_z(theta)
        return Camera(k, self.width, self.height, pose)

    def cv2_rotation_matrix(self, angle_deg: float) -> Mat:
        """Affine matrix that `cv2.warpAffine` needs to realise `rotated_about_center(angle_deg)`."""
        theta = math.radians(angle_deg)
        c, s = math.cos(theta), math.sin(theta)
        cx, cy = self.width / 2.0, self.height / 2.0
        return np.array([[c, s, (1 - c) * cx - s * cy], [-s, c, s * cx + (1 - c) * cy]])

    # -- Geometry -----------------------------------------------------------

    @property
    def world_to_cam(self) -> Mat:
        if self.cam_to_world is None:
            raise ValueError("camera has no pose")
        return np.linalg.inv(self.cam_to_world)

    @property
    def focal_length(self) -> float:
        return float((self.intrinsics[0, 0] + self.intrinsics[1, 1]) / 2.0)

    def project(self, points_world: Mat) -> tuple[Mat, Mat]:
        """World points (N,3) -> pixels (N,2) and depths (N,)."""
        pts = np.asarray(points_world, dtype=np.float64)
        cam = (self.world_to_cam[:3, :3] @ pts.T).T + self.world_to_cam[:3, 3]
        depth = cam[:, 2]
        px = (self.intrinsics @ cam.T).T
        return px[:, :2] / px[:, 2:3], depth

    def unproject(self, pixels: Mat, depths: Mat) -> Mat:
        """Pixels (N,2) at depths (N,) -> world points (N,3)."""
        px = np.asarray(pixels, dtype=np.float64)
        homogeneous = np.concatenate([px, np.ones((px.shape[0], 1))], axis=1)
        rays = (np.linalg.inv(self.intrinsics) @ homogeneous.T).T
        cam = rays * np.asarray(depths, dtype=np.float64)[:, None]
        pose = self.cam_to_world
        if pose is None:
            raise ValueError("camera has no pose")
        return np.asarray((pose[:3, :3] @ cam.T).T + pose[:3, 3], dtype=np.float64)

    def poselib_dict(self) -> dict[str, object]:
        fx, fy = float(self.intrinsics[0, 0]), float(self.intrinsics[1, 1])
        cx, cy = float(self.intrinsics[0, 2]), float(self.intrinsics[1, 2])
        return {"model": "PINHOLE", "width": self.width, "height": self.height, "params": [fx, fy, cx, cy]}
