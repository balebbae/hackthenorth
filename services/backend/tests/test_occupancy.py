import gzip
import struct

import numpy as np

from services.backend.app.services.occupancy import build_occupancy, decode_cells, ray_distance, read_spz_positions


def make_spz(points, alphas=None, fractional_bits=12):
    points = np.asarray(points, dtype=np.float64)
    n = len(points)
    alphas = np.full(n, 255, dtype=np.uint8) if alphas is None else np.asarray(alphas, dtype=np.uint8)
    fixed = np.round(points * (1 << fractional_bits)).astype(np.int64) & 0xFFFFFF
    packed = np.stack([fixed & 0xFF, (fixed >> 8) & 0xFF, (fixed >> 16) & 0xFF], axis=-1).astype(np.uint8)
    header = struct.pack('<IIIBBBB', 0x5053474E, 3, n, 0, fractional_bits, 0, 0)
    tail = bytes(n * 3 + n * 3 + n * 4)  # colours, scales, rotations: unread
    return gzip.compress(header + packed.tobytes() + alphas.tobytes() + tail)


def wall(x0, x1, y0, y1, z, per_cell=10, cell=0.15):
    xs = np.arange(x0, x1, cell / 3)
    ys = np.arange(y0, y1, cell / 3)
    grid = np.array([(x, y, z) for x in xs for y in ys])
    return np.repeat(grid, max(1, per_cell // 9), axis=0)


def test_spz_round_trip():
    pts = [[1.5, -0.25, -3.0], [-2.0, 0.5, 0.75]]
    positions, alphas = read_spz_positions(make_spz(pts, [255, 10]))
    assert np.allclose(positions, pts, atol=1e-3)
    assert list(alphas) == [255, 10]


def test_wall_ahead_is_hit_and_transparent_and_sparse_points_are_ignored():
    world = {'id': 'w', 'version': 'v1', 'alignment': None}
    points = np.vstack([
        wall(-2, 2, -1.2, 1.2, z=-2.0),                    # wall two metres ahead of the origin
        [[0, 0, -0.9]] * 3,                                 # a few stray points: below min_points
        [[0, 0, -1.2]] * 50,                                # a blob, but transparent
    ])
    alphas = np.concatenate([np.full(len(points) - 50, 255), np.full(50, 5)])
    grid = build_occupancy(make_spz(points, alphas), world)
    assert grid['count'] > 0
    assert ray_distance(grid, [0, 0, 0], [0, 0, -1], 4.0) == pytest_approx(2.0, 0.16)
    assert ray_distance(grid, [0, 0, 0], [0, 0, 1], 4.0) is None
    assert ray_distance(grid, [0, 0, 0], [1, 0, 0], 4.0) is None


def test_alignment_moves_the_splat_into_the_world_frame():
    # Splat wall at z=-2; alignment shifts everything +1 in z, so the wall sits at z=-1 in the world.
    world = {'id': 'w', 'version': 'v1',
             'alignment': {'frame': 'niantic-vps', 'position': [0, 0, 1], 'rotation': [0, 0, 0, 1], 'scale': 1}}
    grid = build_occupancy(make_spz(wall(-2, 2, -1.2, 1.2, z=-2.0)), world)
    assert grid['frame'] == 'niantic-vps'
    assert ray_distance(grid, [0, 0, 0], [0, 0, -1], 4.0) == pytest_approx(1.0, 0.16)


def test_cells_decode_to_int32():
    grid = build_occupancy(make_spz(wall(-1, 1, -1, 1, z=-1.0)), {'id': 'w', 'version': 'v1'})
    cells = decode_cells(grid)
    assert cells.dtype == np.int32 and len(cells) == grid['count']


def pytest_approx(value, tolerance):
    import pytest
    return pytest.approx(value, abs=tolerance)
