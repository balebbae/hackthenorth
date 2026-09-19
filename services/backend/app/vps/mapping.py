"""Mapping: fit a scene-specific `SceneHead` to a set of posed images.

Follows the ACE recipe (Brachmann et al., "Accelerated Coordinate Encoding:
Learning to Relocalize in Minutes using RGB and Poses", CVPR 2023):

1. Run every (augmented) mapping image through the frozen encoder once and keep
   a large shuffled buffer of `(feature, target pixel, view)` samples.
2. Train the head on random mini-batches from that buffer with a reprojection
   loss: predicted scene coordinate -> camera of the source view -> pixel, error
   against the pixel the feature came from. A robust (dynamic tanh) loss is used
   for plausible predictions, and an L1 pull towards a fixed-depth proxy point
   for predictions that are behind the camera / too far / wildly off.

No depth, no 3D reconstruction and no feature matching are required - only the
ARKit camera poses and intrinsics that come with every uploaded frame. The
output is a few MB of head weights; localization is a single forward pass plus
PnP-RANSAC (see localize.py).
"""

from __future__ import annotations

import math
import time
from collections.abc import Callable, Sequence
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, cast

import cv2
import numpy as np
import torch
from torch import Tensor

from app.vps.camera import Camera
from app.vps.network import FeatureEncoder, SceneHead, feature_cell_pixels
from app.vps.preprocess import Gray, decode_grayscale, jitter_intensity, resize_for_network, to_network_tensor

ProgressCallback = Callable[[str, float, dict[str, Any]], None]


@dataclass(frozen=True)
class MappingOptions:
    image_height: int = 480
    buffer_size: int = 8_000_000
    samples_per_image: int = 1024
    batch_size: int = 5120
    epochs: int = 16
    learning_rate_min: float = 5e-4
    learning_rate_max: float = 5e-3
    head_blocks: int = 1
    repro_soft_clamp: float = 50.0
    repro_soft_clamp_min: float = 1.0
    repro_hard_clamp: float = 1000.0
    depth_min: float = 0.1
    depth_target: float = 10.0
    depth_max: float = 1000.0
    augment: bool = True
    aug_rotation_deg: float = 15.0
    aug_scale: float = 1.5
    use_half: bool | None = None  # None = on CUDA only
    seed: int = 2089

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> MappingOptions:
        known = {f for f in cls.__dataclass_fields__}
        return cls(**{k: v for k, v in raw.items() if k in known})

    @property
    def iterations(self) -> int:
        return max(1, math.ceil(self.epochs * self.buffer_size / self.batch_size))


@dataclass(frozen=True)
class MappingFrame:
    """One posed mapping image: bytes on disk + the camera describing that exact image."""

    image_path: Path
    camera: Camera  # OpenCV convention, `cam_to_world` in the map frame, sized like the stored image


@dataclass
class MappingStats:
    frames: int
    buffer_samples: int
    iterations: int
    buffer_seconds: float
    train_seconds: float
    final_loss: float
    final_valid_fraction: float
    loss_curve: list[float] = field(default_factory=list)
    scene_center: list[float] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class _RobustReprojectionLoss:
    """tanh-clamped L1 whose clamp shrinks from `soft_clamp` to `soft_clamp_min` on a circular schedule."""

    def __init__(self, total_iterations: int, soft_clamp: float, soft_clamp_min: float) -> None:
        self.total = total_iterations
        self.soft_clamp = soft_clamp
        self.soft_clamp_min = soft_clamp_min

    def __call__(self, errors: Tensor, iteration: int) -> Tensor:
        if errors.numel() == 0:
            return errors.sum()
        progress = min(1.0, iteration / self.total)
        progress = 1.0 - math.sqrt(max(0.0, 1.0 - progress**2))
        weight = (1.0 - progress) * self.soft_clamp + self.soft_clamp_min
        return weight * torch.tanh(errors / weight).sum()


class _TrainingBuffer:
    def __init__(self, size: int, channels: int, device: torch.device, half: bool) -> None:
        dtype = torch.float16 if half else torch.float32
        self.features = torch.empty((size, channels), dtype=dtype, device=device)
        self.target_px = torch.empty((size, 2), dtype=torch.float32, device=device)
        self.view = torch.empty((size,), dtype=torch.int64, device=device)
        self.world_to_cam: list[Tensor] = []
        self.intrinsics: list[Tensor] = []
        self.fill = 0

    def add_view(self, camera: Camera) -> int:
        self.world_to_cam.append(torch.from_numpy(camera.world_to_cam[:3]).float())
        self.intrinsics.append(torch.from_numpy(camera.intrinsics).float())
        return len(self.world_to_cam) - 1

    def finalize(self, device: torch.device) -> tuple[Tensor, Tensor, Tensor]:
        world_to_cam = torch.stack(self.world_to_cam).to(device)
        intrinsics = torch.stack(self.intrinsics).to(device)
        return world_to_cam, intrinsics, torch.linalg.inv(intrinsics)


def _augmented_view(
    gray: np.ndarray, camera: Camera, options: MappingOptions, rng: np.random.Generator
) -> tuple[np.ndarray, np.ndarray, Camera]:
    """Scale / rotate / intensity-jitter a mapping image; returns (image, validity mask, camera)."""
    if options.augment:
        scale = rng.uniform(1.0 / options.aug_scale, options.aug_scale)
        gray = jitter_intensity(gray, rng)
    else:
        scale = 1.0
    target_height = max(8, int(round(options.image_height * scale)))
    gray, camera = resize_for_network(gray, camera, target_height)
    mask: np.ndarray = np.ones_like(gray)
    if options.augment and options.aug_rotation_deg > 0:
        angle = rng.uniform(-options.aug_rotation_deg, options.aug_rotation_deg)
        affine = camera.cv2_rotation_matrix(angle)
        size = (camera.width, camera.height)
        gray = cast(Gray, cv2.warpAffine(gray, affine, size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT))
        mask = cv2.warpAffine(
            mask, affine, size, flags=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=0
        )
        camera = camera.rotated_about_center(angle)
    return gray, mask, camera


def scene_center_of(frames: Sequence[MappingFrame]) -> Tensor:
    centers = np.stack([f.camera.cam_to_world[:3, 3] for f in frames if f.camera.cam_to_world is not None])
    return torch.from_numpy(centers.mean(axis=0)).float()


def train_scene_head(
    frames: Sequence[MappingFrame],
    encoder: FeatureEncoder,
    options: MappingOptions,
    device: torch.device,
    progress: ProgressCallback | None = None,
) -> tuple[SceneHead, MappingStats]:
    if not frames:
        raise ValueError("no mapping frames")
    for frame in frames:
        if frame.camera.cam_to_world is None:
            raise ValueError(f"frame {frame.image_path} has no pose")

    half = options.use_half if options.use_half is not None else device.type == "cuda"
    torch.manual_seed(options.seed)
    rng = np.random.default_rng(options.seed)
    report = progress or (lambda *_: None)

    # ---- Phase 1: feature buffer -------------------------------------------------
    t0 = time.perf_counter()
    encoder = encoder.to(device).eval()
    buffer = _TrainingBuffer(options.buffer_size, encoder.out_channels, device, half)
    autocast = torch.autocast(device_type=device.type, dtype=torch.float16, enabled=half and device.type == "cuda")
    with torch.no_grad():
        passes = 0
        while buffer.fill < options.buffer_size:
            passes += 1
            for index in rng.permutation(len(frames)):
                if buffer.fill >= options.buffer_size:
                    break
                frame = frames[index]
                gray = decode_grayscale(frame.image_path.read_bytes())
                gray, mask, camera = _augmented_view(gray, frame.camera, options, rng)
                with autocast:
                    features = encoder(to_network_tensor(gray, device))  # (1, C, h, w)
                _, channels, fh, fw = features.shape
                cell_mask = torch.from_numpy(cv2.resize(mask, (fw, fh), interpolation=cv2.INTER_NEAREST)).to(device)
                weights = cell_mask.reshape(-1).float()
                if weights.sum() == 0:
                    continue
                n = min(options.samples_per_image, options.buffer_size - buffer.fill)
                picks = torch.multinomial(weights, n, replacement=True)
                view = buffer.add_view(camera)
                flat_features = features[0].reshape(channels, -1).transpose(0, 1)  # (h*w, C)
                flat_pixels = feature_cell_pixels(fh, fw, device).reshape(2, -1).transpose(0, 1)
                sl = slice(buffer.fill, buffer.fill + n)
                buffer.features[sl] = flat_features[picks].to(buffer.features.dtype)
                buffer.target_px[sl] = flat_pixels[picks]
                buffer.view[sl] = view
                buffer.fill += n
                report("buffer", buffer.fill / options.buffer_size, {"frames": len(frames), "passes": passes})
    world_to_cam, intrinsics, intrinsics_inv = buffer.finalize(device)
    buffer_seconds = time.perf_counter() - t0

    # ---- Phase 2: head optimisation ----------------------------------------------
    t1 = time.perf_counter()
    head = SceneHead(scene_center_of(frames), num_blocks=options.head_blocks, in_channels=encoder.out_channels)
    head = head.to(device).train()
    optimizer = torch.optim.AdamW(head.parameters(), lr=options.learning_rate_min)
    iterations = options.iterations
    scheduler = torch.optim.lr_scheduler.OneCycleLR(
        optimizer, max_lr=options.learning_rate_max, total_steps=iterations, cycle_momentum=False
    )
    scaler = torch.amp.GradScaler(device.type, enabled=half and device.type == "cuda")
    robust_loss = _RobustReprojectionLoss(iterations, options.repro_soft_clamp, options.repro_soft_clamp_min)
    generator = torch.Generator(device=device)
    generator.manual_seed(options.seed)

    loss_curve: list[float] = []
    last_loss = float("nan")
    last_valid = 0.0
    iteration = 0
    while iteration < iterations:
        order = torch.randperm(buffer.fill, generator=generator, device=device)
        for start in range(0, buffer.fill, options.batch_size):
            if iteration >= iterations:
                break
            batch = order[start : start + options.batch_size]
            feats = buffer.features[batch]
            target_px = buffer.target_px[batch]
            views = buffer.view[batch]
            b = feats.shape[0]

            with autocast:
                # 1x1 convs: treat the batch as a single 1 x B "image".
                pred = head(feats.transpose(0, 1).reshape(1, -1, 1, b))
            scene = pred.reshape(3, b).transpose(0, 1).float()  # (B, 3)

            w2c = world_to_cam[views]  # (B, 3, 4)
            cam = torch.einsum("bij,bj->bi", w2c[:, :, :3], scene) + w2c[:, :, 3]  # (B, 3)
            px_h = torch.einsum("bij,bj->bi", intrinsics[views], cam)
            depth = px_h[:, 2].clamp(min=options.depth_min)
            px = px_h[:, :2] / depth[:, None]
            repro_err = (px - target_px).abs().sum(dim=1)  # L1 in pixels

            invalid = (
                (cam[:, 2] < options.depth_min)
                | (cam[:, 2] > options.depth_max)
                | (repro_err > options.repro_hard_clamp)
            )
            valid = ~invalid
            loss_valid = robust_loss(repro_err[valid], iteration)

            target_h = torch.cat([target_px, torch.ones_like(target_px[:, :1])], dim=1)
            proxy = options.depth_target * torch.einsum("bij,bj->bi", intrinsics_inv[views], target_h)
            loss_invalid = (proxy - cam).abs()[invalid].sum()

            loss = (loss_valid + loss_invalid) / b

            optimizer.zero_grad(set_to_none=True)
            scaler.scale(loss).backward()  # type: ignore[no-untyped-call]
            scaler.step(optimizer)
            scaler.update()
            if iteration + 1 < iterations:
                scheduler.step()

            iteration += 1
            last_loss = float(loss.detach())
            last_valid = float(valid.float().mean())
            if iteration % max(1, iterations // 100) == 0 or iteration == iterations:
                loss_curve.append(last_loss)
                report(
                    "train",
                    iteration / iterations,
                    {"iteration": iteration, "iterations": iterations, "loss": last_loss, "valid": last_valid},
                )

    head.eval()
    stats = MappingStats(
        frames=len(frames),
        buffer_samples=buffer.fill,
        iterations=iterations,
        buffer_seconds=round(buffer_seconds, 2),
        train_seconds=round(time.perf_counter() - t1, 2),
        final_loss=last_loss,
        final_valid_fraction=last_valid,
        loss_curve=loss_curve,
        scene_center=[float(v) for v in head.scene_center.flatten().cpu()],
    )
    return head, stats
