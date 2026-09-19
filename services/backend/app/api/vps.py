"""`/worlds/{id}/vps/*` - visual positioning: capture upload, mapping jobs, image-query localization."""

from __future__ import annotations

from typing import Any, Literal

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel, ConfigDict, Field

from app.auth import require_api_key
from app.vps.localize import LocalizationOptions
from app.vps.mapping import MappingOptions
from app.vps.service import FrameUpload, VpsError, VpsService

router = APIRouter(prefix="/worlds/{world_id}/vps", tags=["vps"], dependencies=[Depends(require_api_key)])

RotationName = Literal["none", "cw90", "ccw90", "180"]


def get_service(request: Request) -> VpsService:
    service: VpsService = request.app.state.vps
    return service


class FrameBody(BaseModel):
    """Exactly what `NianticRESTTransport` (apps/ios) posts, plus optional sensor hints."""

    model_config = ConfigDict(extra="ignore")

    sequence: int = 0
    capturedAt: float = 0.0  # noqa: N815 - wire format
    imageBase64: str  # noqa: N815
    imageWidth: int = Field(gt=0)  # noqa: N815
    imageHeight: int = Field(gt=0)  # noqa: N815
    intrinsics: list[float] = Field(min_length=9, max_length=9, description="3x3 column-major (simd_float3x3)")
    cameraTransform: list[float] | None = Field(  # noqa: N815
        default=None, min_length=16, max_length=16, description="4x4 column-major ARKit camera transform"
    )
    sensorWidth: int | None = Field(default=None, gt=0)  # noqa: N815
    sensorHeight: int | None = Field(default=None, gt=0)  # noqa: N815
    rotation: RotationName = Field(default="cw90", description="How the client rotated the sensor image before upload")

    def to_upload(self) -> FrameUpload:
        return FrameUpload(
            sequence=self.sequence,
            captured_at=self.capturedAt,
            image=FrameUpload.decode_image(self.imageBase64),
            image_width=self.imageWidth,
            image_height=self.imageHeight,
            intrinsics=self.intrinsics,
            camera_transform=self.cameraTransform,
            sensor_width=self.sensorWidth,
            sensor_height=self.sensorHeight,
            rotation=self.rotation,
        )


class CreateCaptureBody(BaseModel):
    model_config = ConfigDict(extra="ignore")

    deviceId: str | None = None  # noqa: N815
    sensorWidth: int | None = Field(default=None, gt=0)  # noqa: N815
    sensorHeight: int | None = Field(default=None, gt=0)  # noqa: N815
    rotation: RotationName = "cw90"


class CreateMapBody(BaseModel):
    model_config = ConfigDict(extra="ignore")

    captureIds: list[str] = Field(min_length=1)  # noqa: N815
    name: str | None = None
    mapping: dict[str, Any] = Field(default_factory=dict, description="Overrides for MappingOptions")
    localization: dict[str, Any] = Field(default_factory=dict, description="Overrides for LocalizationOptions")


class LocalizeBody(FrameBody):
    mapId: str | None = None  # noqa: N815


def _raise(exc: VpsError) -> HTTPException:
    return HTTPException(exc.status, exc.detail)


@router.post("/captures", status_code=201)
def create_capture(
    world_id: str, body: CreateCaptureBody, service: VpsService = Depends(get_service)
) -> dict[str, Any]:
    sensor = (body.sensorWidth, body.sensorHeight) if body.sensorWidth and body.sensorHeight else None
    try:
        return service.create_capture(world_id, body.deviceId, sensor, body.rotation)
    except VpsError as exc:
        raise _raise(exc) from exc


@router.get("/captures")
def list_captures(world_id: str, service: VpsService = Depends(get_service)) -> dict[str, Any]:
    try:
        return {"captures": service.list_captures(world_id)}
    except VpsError as exc:
        raise _raise(exc) from exc


@router.get("/captures/{capture_id}")
def get_capture(world_id: str, capture_id: str, service: VpsService = Depends(get_service)) -> dict[str, Any]:
    try:
        return service.get_capture(world_id, capture_id)
    except VpsError as exc:
        raise _raise(exc) from exc


@router.post("/captures/{capture_id}/frames", status_code=201)
def add_frame(
    world_id: str, capture_id: str, body: FrameBody, service: VpsService = Depends(get_service)
) -> dict[str, Any]:
    try:
        return service.add_frame(world_id, capture_id, body.to_upload())
    except VpsError as exc:
        raise _raise(exc) from exc


@router.post("/maps", status_code=202)
def create_map(world_id: str, body: CreateMapBody, service: VpsService = Depends(get_service)) -> dict[str, Any]:
    try:
        mapping = MappingOptions.from_dict({"image_height": service.settings.image_height, **body.mapping})
        localization = LocalizationOptions.from_dict(
            {"image_height": service.settings.image_height, **body.localization}
        )
    except TypeError as exc:
        raise HTTPException(400, f"invalid options: {exc}") from exc
    try:
        map_record, job = service.start_mapping(world_id, body.captureIds, mapping, localization, body.name)
    except VpsError as exc:
        raise _raise(exc) from exc
    return {"map": map_record, "job": job}


@router.get("/maps")
def list_maps(world_id: str, service: VpsService = Depends(get_service)) -> dict[str, Any]:
    try:
        service.store.refresh()
        return {"maps": service.list_maps(world_id), "activeMapId": service.active_map_id(world_id)}
    except VpsError as exc:
        raise _raise(exc) from exc


@router.get("/maps/{map_id}")
def get_map(world_id: str, map_id: str, service: VpsService = Depends(get_service)) -> dict[str, Any]:
    try:
        service.store.refresh()
        return service.get_map(world_id, map_id)
    except VpsError as exc:
        raise _raise(exc) from exc


@router.post("/maps/{map_id}/activate")
def activate_map(world_id: str, map_id: str, service: VpsService = Depends(get_service)) -> dict[str, Any]:
    try:
        service.store.refresh()
        return service.activate_map(world_id, map_id)
    except VpsError as exc:
        raise _raise(exc) from exc


@router.get("/jobs/{job_id}")
def get_job(world_id: str, job_id: str, service: VpsService = Depends(get_service)) -> dict[str, Any]:
    try:
        service.store.refresh()
        return service.get_job(world_id, job_id)
    except VpsError as exc:
        raise _raise(exc) from exc


@router.post("/localize")
def localize(world_id: str, body: LocalizeBody, service: VpsService = Depends(get_service)) -> dict[str, Any]:
    try:
        return service.localize(world_id, body.to_upload(), body.mapId)
    except VpsError as exc:
        raise _raise(exc) from exc
