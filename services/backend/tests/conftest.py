from __future__ import annotations

import os
import sys
import urllib.request
from pathlib import Path

import numpy as np
import pytest
import torch

BACKEND_DIR = Path(__file__).resolve().parent.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.vps.network import FeatureEncoder, load_encoder  # noqa: E402

ENCODER_URL = (
    "https://github.com/nianticlabs/ace/raw/e9e90f2d02ee92c348bf411a5a60e230af6c315e/ace_encoder_pretrained.pt"
)
ENCODER_CACHE = Path.home() / ".cache" / "wander" / "ace_encoder_pretrained.pt"


def encoder_path() -> Path | None:
    """Pretrained ACE encoder: WANDER_ACE_ENCODER_PATH, else a cached download (None if offline)."""
    configured = os.environ.get("WANDER_ACE_ENCODER_PATH")
    if configured and Path(configured).is_file():
        return Path(configured)
    if ENCODER_CACHE.is_file():
        return ENCODER_CACHE
    try:
        ENCODER_CACHE.parent.mkdir(parents=True, exist_ok=True)
        tmp = ENCODER_CACHE.with_suffix(".tmp")
        urllib.request.urlretrieve(ENCODER_URL, tmp)
        tmp.replace(ENCODER_CACHE)
        return ENCODER_CACHE
    except OSError:
        return None


@pytest.fixture
def rng() -> np.random.Generator:
    return np.random.default_rng(1234)


@pytest.fixture(scope="session")
def encoder() -> FeatureEncoder:
    path = encoder_path()
    if path is None:
        pytest.skip("pretrained ACE encoder unavailable (set WANDER_ACE_ENCODER_PATH or allow network)")
    return load_encoder(path, torch.device("cpu"))
