"""Filesystem layout of the worlds Volume (shared/contracts/README.md).

Everything lives under `<data_root>/worlds/<worldId>/`::

    world.json                          manifest (world.schema.json)
    <version>/scene.spz                 splat + other versioned assets
    vps/captures/<captureId>/capture.json
    vps/captures/<captureId>/frames.jsonl   one FrameRecord per line
    vps/captures/<captureId>/frames/<seq>.jpg
    vps/maps/<mapId>/map.json           MapRecord (status, stats, training options)
    vps/maps/<mapId>/head.pt            scene-specific ACE head weights
    vps/jobs/<jobId>.json               JobRecord
    vps/active.json                     {"mapId": ...} - map used by /vps/localize

Modal is the only writer, so plain files + atomic renames are enough. Volume
consistency across containers is handled by `refresh()`/`commit()` hooks that
the Modal deployment wires to `Volume.reload()`/`Volume.commit()`.
"""

from __future__ import annotations

import json
import os
import re
import uuid
from collections.abc import Callable, Iterator
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

SEGMENT_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def is_safe_segment(segment: str) -> bool:
    return bool(SEGMENT_RE.match(segment)) and segment not in {".", ".."}


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def new_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:12]}"


def _atomic_write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)


def _write_json(path: Path, payload: Any) -> None:
    _atomic_write_bytes(path, (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode())


def _read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        return None


class WorldStore:
    """Path helpers + small JSON records for one data root."""

    def __init__(
        self,
        root: Path,
        refresh: Callable[[], None] | None = None,
        commit: Callable[[], None] | None = None,
    ) -> None:
        self.root = root
        self._refresh = refresh
        self._commit = commit

    # -- Volume hooks -------------------------------------------------------

    def refresh(self) -> None:
        """Pick up writes made by other containers (no-op on a plain filesystem)."""
        if self._refresh:
            self._refresh()

    def commit(self) -> None:
        """Make local writes visible to other containers (no-op on a plain filesystem)."""
        if self._commit:
            self._commit()

    # -- Paths --------------------------------------------------------------

    def worlds_dir(self) -> Path:
        return self.root / "worlds"

    def world_dir(self, world_id: str) -> Path:
        self._check(world_id)
        return self.worlds_dir() / world_id

    def manifest_path(self, world_id: str) -> Path:
        return self.world_dir(world_id) / "world.json"

    def asset_path(self, world_id: str, segments: list[str]) -> Path:
        for s in segments:
            self._check(s)
        return self.world_dir(world_id).joinpath(*segments)

    def vps_dir(self, world_id: str) -> Path:
        return self.world_dir(world_id) / "vps"

    def capture_dir(self, world_id: str, capture_id: str) -> Path:
        self._check(capture_id)
        return self.vps_dir(world_id) / "captures" / capture_id

    def frames_index_path(self, world_id: str, capture_id: str) -> Path:
        return self.capture_dir(world_id, capture_id) / "frames.jsonl"

    def frame_image_path(self, world_id: str, capture_id: str, sequence: int) -> Path:
        return self.capture_dir(world_id, capture_id) / "frames" / f"{sequence:06d}.jpg"

    def map_dir(self, world_id: str, map_id: str) -> Path:
        self._check(map_id)
        return self.vps_dir(world_id) / "maps" / map_id

    def head_path(self, world_id: str, map_id: str) -> Path:
        return self.map_dir(world_id, map_id) / "head.pt"

    def job_path(self, world_id: str, job_id: str) -> Path:
        self._check(job_id)
        return self.vps_dir(world_id) / "jobs" / f"{job_id}.json"

    def active_map_path(self, world_id: str) -> Path:
        return self.vps_dir(world_id) / "active.json"

    # -- Manifests ----------------------------------------------------------

    def list_worlds(self) -> list[dict[str, Any]]:
        root = self.worlds_dir()
        if not root.is_dir():
            return []
        manifests: list[dict[str, Any]] = []
        for child in sorted(root.iterdir()):
            if child.is_dir() and is_safe_segment(child.name):
                manifest = _read_json(child / "world.json")
                if isinstance(manifest, dict):
                    manifests.append(manifest)
        manifests.sort(key=lambda m: (str(m.get("updatedAt", "")), str(m.get("name", ""))), reverse=True)
        return manifests

    def read_manifest(self, world_id: str) -> dict[str, Any] | None:
        manifest = _read_json(self.manifest_path(world_id))
        return manifest if isinstance(manifest, dict) else None

    def write_manifest(self, world_id: str, manifest: dict[str, Any]) -> None:
        _write_json(self.manifest_path(world_id), manifest)

    def world_exists(self, world_id: str) -> bool:
        return self.world_dir(world_id).is_dir()

    # -- Generic JSON records -------------------------------------------------

    def read_record(self, path: Path) -> dict[str, Any] | None:
        record = _read_json(path)
        return record if isinstance(record, dict) else None

    def write_record(self, path: Path, record: dict[str, Any]) -> None:
        _write_json(path, record)

    def write_bytes(self, path: Path, data: bytes) -> None:
        _atomic_write_bytes(path, data)

    def append_jsonl(self, path: Path, record: dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, separators=(",", ":")) + "\n")

    def iter_jsonl(self, path: Path) -> Iterator[dict[str, Any]]:
        try:
            with path.open(encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        record = json.loads(line)
                        if isinstance(record, dict):
                            yield record
        except FileNotFoundError:
            return

    def list_record_ids(self, directory: Path) -> list[str]:
        if not directory.is_dir():
            return []
        return sorted(p.name.removesuffix(".json") for p in directory.iterdir() if is_safe_segment(p.name))

    # -- Internal -------------------------------------------------------------

    @staticmethod
    def _check(segment: str) -> None:
        if not is_safe_segment(segment):
            raise ValueError(f"unsafe path segment: {segment!r}")
