"""Scene coordinate regression network (ACE, Brachmann et al. CVPR 2023).

Two parts:

* `FeatureEncoder` - a fully convolutional, scene-agnostic backbone that maps a
  normalised grayscale image to a 512-channel feature map at 1/8 resolution.
  We do not train it; weights are loaded from a pretrained checkpoint (see
  `load_encoder`). Parameter names follow the public checkpoint so it can be
  loaded verbatim.
* `SceneHead` - a scene-specific MLP (1x1 convolutions) that regresses, for
  every feature cell, a 3D point in the map frame. It predicts a homogeneous
  4-vector and de-homogenises with a bounded scale, which stabilises the early
  phase of mapping. This is the only thing a map stores (`head.pt`).

`SceneRegressor` composes both. Predictions are anchored at the feature-cell
centres: cell `(i, j)` corresponds to pixel `(8 * j + 4, 8 * i + 4)` of the
network input image.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any, cast

import torch
import torch.nn.functional as fn
from torch import Tensor, nn

OUTPUT_SUBSAMPLE = 8
FEATURE_DIM = 512
IMAGE_MEAN = 0.4
IMAGE_STD = 0.25


class FeatureEncoder(nn.Module):
    def __init__(self, out_channels: int = FEATURE_DIM) -> None:
        super().__init__()
        self.out_channels = out_channels
        self.conv1 = nn.Conv2d(1, 32, 3, 1, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 2, 1)
        self.conv3 = nn.Conv2d(64, 128, 3, 2, 1)
        self.conv4 = nn.Conv2d(128, 256, 3, 2, 1)
        self.res1_conv1 = nn.Conv2d(256, 256, 3, 1, 1)
        self.res1_conv2 = nn.Conv2d(256, 256, 1, 1, 0)
        self.res1_conv3 = nn.Conv2d(256, 256, 3, 1, 1)
        self.res2_conv1 = nn.Conv2d(256, 512, 3, 1, 1)
        self.res2_conv2 = nn.Conv2d(512, 512, 1, 1, 0)
        self.res2_conv3 = nn.Conv2d(512, out_channels, 3, 1, 1)
        self.res2_skip = nn.Conv2d(256, out_channels, 1, 1, 0)

    def forward(self, image: Tensor) -> Tensor:
        x = fn.relu(self.conv1(image))
        x = fn.relu(self.conv2(x))
        x = fn.relu(self.conv3(x))
        res = fn.relu(self.conv4(x))
        x = fn.relu(self.res1_conv1(res))
        x = fn.relu(self.res1_conv2(x))
        x = fn.relu(self.res1_conv3(x))
        res = res + x
        x = fn.relu(self.res2_conv1(res))
        x = fn.relu(self.res2_conv2(x))
        x = fn.relu(self.res2_conv3(x))
        out: Tensor = self.res2_skip(res) + x
        return out


class SceneHead(nn.Module):
    """Per-cell MLP: 512-d feature -> 3D scene coordinate (map frame, metres)."""

    def __init__(
        self,
        scene_center: Tensor,
        num_blocks: int = 1,
        in_channels: int = FEATURE_DIM,
        hidden: int = 512,
        min_scale: float = 0.01,
        max_scale: float = 4.0,
    ) -> None:
        super().__init__()
        self.num_blocks = num_blocks
        self.in_channels = in_channels
        self.hidden = hidden
        self.skip = nn.Identity() if in_channels == hidden else nn.Conv2d(in_channels, hidden, 1)
        self.stem = nn.ModuleList(
            [nn.Conv2d(in_channels, hidden, 1), nn.Conv2d(hidden, hidden, 1), nn.Conv2d(hidden, hidden, 1)]
        )
        self.blocks = nn.ModuleList(
            [nn.ModuleList([nn.Conv2d(hidden, hidden, 1) for _ in range(3)]) for _ in range(num_blocks)]
        )
        self.out1 = nn.Conv2d(hidden, hidden, 1)
        self.out2 = nn.Conv2d(hidden, hidden, 1)
        self.out3 = nn.Conv2d(hidden, 4, 1)
        self.scene_center: Tensor
        self.max_inv_scale: Tensor
        self.min_inv_scale: Tensor
        self.softplus_beta: Tensor
        self.register_buffer("scene_center", scene_center.detach().clone().float().view(1, 3, 1, 1))
        self.register_buffer("max_inv_scale", torch.tensor([1.0 / max_scale]))
        self.register_buffer("min_inv_scale", torch.tensor([1.0 / min_scale]))
        self.register_buffer("softplus_beta", torch.tensor([math.log(2.0) / (1.0 - 1.0 / max_scale)]))

    def forward(self, features: Tensor) -> Tensor:
        x = features
        for layer in self.stem:
            x = fn.relu(layer(x))
        res = self.skip(features) + x
        for block in self.blocks:
            x = res
            for layer in cast(nn.ModuleList, block):
                x = fn.relu(layer(x))
            res = res + x
        x = fn.relu(self.out1(res))
        x = fn.relu(self.out2(x))
        raw = self.out3(x)
        # Bounded homogeneous scale: h in [1/max_scale, 1/min_scale], i.e. |scene coord| within [min, max] * |raw|.
        h = fn.softplus(raw[:, 3:4], beta=float(self.softplus_beta.item())) + self.max_inv_scale
        h = h.clamp(max=float(self.min_inv_scale.item()))
        out: Tensor = raw[:, :3] / h + self.scene_center
        return out

    def export(self) -> dict[str, Any]:
        return {
            "arch": {"num_blocks": self.num_blocks, "in_channels": self.in_channels, "hidden": self.hidden},
            "state_dict": {k: v.detach().cpu() for k, v in self.state_dict().items()},
        }

    @classmethod
    def from_export(cls, payload: dict[str, Any]) -> SceneHead:
        arch = payload["arch"]
        head = cls(torch.zeros(3), arch["num_blocks"], arch["in_channels"], arch["hidden"])
        head.load_state_dict(payload["state_dict"])
        return head


class SceneRegressor(nn.Module):
    def __init__(self, encoder: FeatureEncoder, head: SceneHead) -> None:
        super().__init__()
        self.encoder = encoder
        self.head = head

    def forward(self, image: Tensor) -> Tensor:
        out: Tensor = self.head(self.encoder(image))
        return out


def load_encoder(path: Path, device: torch.device) -> FeatureEncoder:
    state = torch.load(path, map_location="cpu", weights_only=True)
    if "state_dict" in state:
        state = state["state_dict"]
    encoder = FeatureEncoder(out_channels=state["res2_conv3.weight"].shape[0])
    encoder.load_state_dict(state)
    encoder.eval().requires_grad_(False)
    return encoder.to(device)


def feature_cell_pixels(height: int, width: int, device: torch.device) -> Tensor:
    """(2, H, W) pixel coordinates (u, v) of the cell centres for a feature map of size HxW."""
    ys = (torch.arange(height, device=device, dtype=torch.float32) + 0.5) * OUTPUT_SUBSAMPLE
    xs = (torch.arange(width, device=device, dtype=torch.float32) + 0.5) * OUTPUT_SUBSAMPLE
    vv, uu = torch.meshgrid(ys, xs, indexing="ij")
    return torch.stack([uu, vv])


def resolve_device(preference: str) -> torch.device:
    if preference == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    return torch.device(preference)
