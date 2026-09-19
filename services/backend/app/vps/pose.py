"""Rigid transform helpers in the shared contract representation (position + `[x, y, z, w]` quaternion)."""

from __future__ import annotations

import math

import numpy as np

from app.vps.camera import Mat


def rotation_to_quaternion(rotation: Mat) -> list[float]:
    """3x3 rotation matrix -> unit quaternion `[x, y, z, w]` (navigation.schema.json order)."""
    r = np.asarray(rotation, dtype=np.float64)
    trace = float(np.trace(r))
    if trace > 0.0:
        s = math.sqrt(trace + 1.0) * 2.0
        w, x, y, z = 0.25 * s, (r[2, 1] - r[1, 2]) / s, (r[0, 2] - r[2, 0]) / s, (r[1, 0] - r[0, 1]) / s
    elif r[0, 0] > r[1, 1] and r[0, 0] > r[2, 2]:
        s = math.sqrt(1.0 + r[0, 0] - r[1, 1] - r[2, 2]) * 2.0
        w, x, y, z = (r[2, 1] - r[1, 2]) / s, 0.25 * s, (r[0, 1] + r[1, 0]) / s, (r[0, 2] + r[2, 0]) / s
    elif r[1, 1] > r[2, 2]:
        s = math.sqrt(1.0 + r[1, 1] - r[0, 0] - r[2, 2]) * 2.0
        w, x, y, z = (r[0, 2] - r[2, 0]) / s, (r[0, 1] + r[1, 0]) / s, 0.25 * s, (r[1, 2] + r[2, 1]) / s
    else:
        s = math.sqrt(1.0 + r[2, 2] - r[0, 0] - r[1, 1]) * 2.0
        w, x, y, z = (r[1, 0] - r[0, 1]) / s, (r[0, 2] + r[2, 0]) / s, (r[1, 2] + r[2, 1]) / s, 0.25 * s
    q = np.array([x, y, z, w])
    q /= np.linalg.norm(q)
    if q[3] < 0:
        q = -q
    return [float(v) for v in q]


def quaternion_to_rotation(quaternion: list[float]) -> Mat:
    x, y, z, w = (float(v) for v in quaternion)
    n = math.sqrt(x * x + y * y + z * z + w * w)
    x, y, z, w = x / n, y / n, z / n, w / n
    return np.array(
        [
            [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
            [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
            [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)],
        ]
    )


def matrix_to_pose(matrix: Mat) -> dict[str, list[float]]:
    m = np.asarray(matrix, dtype=np.float64)
    return {"position": [float(v) for v in m[:3, 3]], "rotation": rotation_to_quaternion(m[:3, :3])}


def pose_to_matrix(pose: dict[str, list[float]]) -> Mat:
    m = np.eye(4)
    m[:3, :3] = quaternion_to_rotation(pose["rotation"])
    m[:3, 3] = np.asarray(pose["position"], dtype=np.float64)
    return m


def rotation_angle_deg(rotation_a: Mat, rotation_b: Mat) -> float:
    """Geodesic angle between two rotations."""
    rel = np.asarray(rotation_a).T @ np.asarray(rotation_b)
    cos = (np.trace(rel) - 1.0) / 2.0
    return math.degrees(math.acos(max(-1.0, min(1.0, cos))))
