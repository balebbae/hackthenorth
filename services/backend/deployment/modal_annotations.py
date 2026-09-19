"""Run with modal run -m services.backend.deployment.modal_annotations --help."""
from pathlib import Path
import uuid
import modal

app = modal.App('htn-semantic-annotations')
volume = modal.Volume.from_name('htn-annotations', create_if_missing=True)
ROOT = Path(__file__).resolve().parents[3]
image = (modal.Image.debian_slim(python_version='3.12').apt_install('ffmpeg')
    .pip_install_from_requirements(str(ROOT / 'services/backend/requirements.txt'))
    .workdir('/workspace')
    .add_local_dir(str(ROOT / 'services/backend'), remote_path='/workspace/services/backend',
        ignore=['.env', '.env.*', '**/.env', '**/.env.*', '**/__pycache__/**', '**/.pytest_cache/**'])
    .add_local_dir(str(ROOT / 'shared/contracts'), remote_path='/workspace/shared/contracts'))


@app.function(image=image, secrets=[modal.Secret.from_name('htn-backend')],
              volumes={'/data': volume}, cpu=2, memory=4096, timeout=3600, max_containers=2)
async def annotate_video(job_id: str, site: str, revision: str, floor: int, limit: int = 120):
    from services.backend.app.config import Settings
    from services.backend.app.services.annotations import extract_frames, annotate
    uuid.UUID(job_id)
    root = Path('/data') / job_id
    if not (root / 'frames').exists():
        extract_frames(root / 'input.video', root / 'frames', limit=limit)
    try:
        batch = await annotate(root / 'frames', root / 'candidates.json', site, revision,
                               floor, Settings(), limit)
        return batch.model_dump()
    finally:
        volume.commit()


@app.local_entrypoint()
def main(video: str, site: str, revision: str, floor: int, output: str = 'artifacts/candidates.json',
         limit: int = 120):
    import json
    source = Path(video)
    if not source.is_file():
        raise ValueError('Video file does not exist')
    job_id = str(uuid.uuid4())
    with volume.batch_upload() as upload:
        upload.put_file(str(source), f'/{job_id}/input.video')
    print(f'Annotation job: {job_id}; evidence persists in volume htn-annotations')
    result = annotate_video.remote(job_id, site, revision, floor, limit)
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(f'Review candidates in {target}; frames are in volume /{job_id}/frames')
