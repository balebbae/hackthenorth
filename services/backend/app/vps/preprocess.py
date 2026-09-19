"""Image decoding and normalisation shared by mapping and localization."""

from __future__ import annotations

from typing import cast

import cv2
import numpy as np
import torch
from numpy.typing import NDArray

from app.vps.camera import Camera
from app.vps.network import IMAGE_MEAN, IMAGE_STD, OUTPUT_SUBSAMPLE

Gray = NDArray[np.uint8]


def decode_grayscale(data: bytes) -> Gray:
    """JPEG/PNG bytes -> uint8 grayscale (H, W). Raises ValueError on garbage."""
    buf = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(buf, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("could not decode image")
    return np.ascontiguousarray(image, dtype=np.uint8)


def encode_jpeg(gray: Gray, quality: int = 92) -> bytes:
    ok, buf = cv2.imencode(".jpg", gray, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    if not ok:
        raise ValueError("could not encode image")
    return bytes(buf)


def resize_for_network(gray: Gray, camera: Camera, target_height: int) -> tuple[Gray, Camera]:
    """Resize to `target_height` (keeping aspect) and crop to a multiple of the network stride.

    Returns the image the encoder will see and the camera describing it.
    """
    if gray.shape[0] != camera.height or gray.shape[1] != camera.width:
        raise ValueError(
            f"camera {camera.width}x{camera.height} does not describe image {gray.shape[1]}x{gray.shape[0]}"
        )
    scaled = camera.resized_to_height(target_height)
    if (scaled.width, scaled.height) != (camera.width, camera.height):
        interpolation = cv2.INTER_AREA if scaled.height < camera.height else cv2.INTER_LINEAR
        gray = cast(Gray, cv2.resize(gray, (scaled.width, scaled.height), interpolation=interpolation))
    crop_h = (scaled.height // OUTPUT_SUBSAMPLE) * OUTPUT_SUBSAMPLE
    crop_w = (scaled.width // OUTPUT_SUBSAMPLE) * OUTPUT_SUBSAMPLE
    if crop_h < OUTPUT_SUBSAMPLE or crop_w < OUTPUT_SUBSAMPLE:
        raise ValueError("image too small")
    gray = np.ascontiguousarray(gray[:crop_h, :crop_w])
    cropped = Camera(scaled.intrinsics, crop_w, crop_h, scaled.cam_to_world)
    return gray, cropped


def to_network_tensor(gray: Gray, device: torch.device) -> torch.Tensor:
    """uint8 (H, W) -> normalised float tensor (1, 1, H, W)."""
    tensor = torch.from_numpy(gray).to(device=device, dtype=torch.float32) / 255.0
    return ((tensor - IMAGE_MEAN) / IMAGE_STD)[None, None]


def jitter_intensity(gray: Gray, rng: np.random.Generator, brightness: float = 0.1, contrast: float = 0.1) -> Gray:
    """Random brightness/contrast change, in place of colour jitter for grayscale inputs."""
    alpha = 1.0 + rng.uniform(-contrast, contrast)
    beta = rng.uniform(-brightness, brightness) * 255.0
    out = gray.astype(np.float32) * alpha + beta
    return cast(Gray, np.clip(out, 0, 255).astype(np.uint8))
