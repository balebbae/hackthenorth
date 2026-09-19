"""Static obstacle map from a world's Gaussian splat.

The splat (Niantic .spz) is a dense point set of the scanned space. Voxelising
it gives an occupancy grid in the world frame that a localised phone can ray-cast
against to find walls and furniture in any direction, including where no sensor
is looking. Only the positions and alphas are read from the file.
"""
import base64
import gzip
import math
import struct

import numpy as np

SPZ_MAGIC = 0x5053474E
SCHEMA = 'wander.occupancy/v1'


def read_spz_positions(data: bytes):
    """Return (positions[N,3] float32, alphas[N] uint8) from an .spz file."""
    raw = gzip.decompress(data)
    magic, version, count, _sh, fractional_bits, _flags, _ = struct.unpack_from('<IIIBBBB', raw, 0)
    if magic != SPZ_MAGIC:
        raise ValueError('Not an SPZ file')
    if version not in (2, 3):
        raise ValueError(f'Unsupported SPZ version {version}')
    offset = 16
    packed = np.frombuffer(raw, dtype=np.uint8, count=count * 9, offset=offset).reshape(count, 3, 3).astype(np.int32)
    fixed = packed[:, :, 0] | (packed[:, :, 1] << 8) | (packed[:, :, 2] << 16)
    fixed = np.where(fixed & 0x800000, fixed - 0x1000000, fixed)
    positions = (fixed / float(1 << fractional_bits)).astype(np.float32)
    offset += count * 9
    alphas = np.frombuffer(raw, dtype=np.uint8, count=count, offset=offset)
    return positions, alphas


def quaternion_rotate(points, q):
    """Rotate points[N,3] by quaternion q = [x, y, z, w]."""
    x, y, z, w = q
    r = np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
        [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
        [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)],
    ], dtype=np.float32)
    return points @ r.T


def build_occupancy(spz: bytes, world: dict, cell_size: float = 0.15, min_alpha: int = 64, min_points: int = 6,
                    trim_percentile: float = 0.5) -> dict:
    """Voxelise the splat into the world frame (alignment applied). Cells with
    fewer than `min_points` opaque-enough points are treated as empty, which
    drops the floating gaussians every scan has."""
    positions, alphas = read_spz_positions(spz)
    positions = positions[alphas >= min_alpha]
    alignment = world.get('alignment')
    if alignment:
        positions = quaternion_rotate(positions * np.float32(alignment['scale']), alignment['rotation'])
        positions = positions + np.asarray(alignment['position'], dtype=np.float32)
    if len(positions) == 0:
        raise ValueError('Splat has no opaque points')
    low = np.percentile(positions, trim_percentile, axis=0) - 0.5
    high = np.percentile(positions, 100 - trim_percentile, axis=0) + 0.5
    inside = np.all((positions >= low) & (positions <= high), axis=1)
    positions = positions[inside]
    origin = np.floor(low / cell_size) * cell_size
    size = np.maximum(1, np.ceil((high - origin) / cell_size).astype(np.int64))
    index = np.floor((positions - origin) / cell_size).astype(np.int64)
    index = np.clip(index, 0, size - 1)
    flat = (index[:, 0] * size[1] + index[:, 1]) * size[2] + index[:, 2]
    cells, counts = np.unique(flat, return_counts=True)
    occupied = cells[counts >= min_points].astype(np.int32)
    return {
        'schema': SCHEMA,
        'worldId': world['id'],
        'version': world['version'],
        'frame': (alignment or {}).get('frame', 'splat'),
        'cellSize': cell_size,
        'origin': [float(v) for v in origin],
        'size': [int(v) for v in size],
        'count': int(len(occupied)),
        'minPoints': min_points,
        'encoding': 'int32le-base64',
        'cells': base64.b64encode(occupied.tobytes()).decode('ascii'),
    }


def decode_cells(grid: dict) -> np.ndarray:
    return np.frombuffer(base64.b64decode(grid['cells']), dtype=np.int32)


def ray_distance(grid: dict, origin, direction, max_range: float, cells=None) -> float | None:
    """Reference ray march used by tests: distance to the first occupied cell."""
    cells = set(decode_cells(grid).tolist()) if cells is None else cells
    cell = grid['cellSize']
    o = np.asarray(grid['origin'])
    size = grid['size']
    d = np.asarray(direction, dtype=np.float64)
    d = d / np.linalg.norm(d)
    step = cell / 2
    t = 0.0
    while t <= max_range:
        p = np.asarray(origin) + d * t
        i = np.floor((p - o) / cell).astype(int)
        if np.all(i >= 0) and np.all(i < size):
            if int((i[0] * size[1] + i[1]) * size[2] + i[2]) in cells:
                return t
        t += step
    return None
