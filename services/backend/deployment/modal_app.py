from pathlib import Path
import modal

ROOT = Path(__file__).resolve().parents[3]
image = (modal.Image.debian_slim(python_version='3.12')
         .pip_install_from_requirements(str(ROOT / 'services/backend/requirements.txt'))
         .workdir('/workspace')
         .add_local_dir(str(ROOT / 'services/backend'), remote_path='/workspace/services/backend',
                        ignore=['.env', '.env.*', '**/.env', '**/.env.*', '**/__pycache__/**', '**/.pytest_cache/**'])
         .add_local_dir(str(ROOT / 'maps/navigation'), remote_path='/workspace/maps/navigation'))
app = modal.App('htn-navigation-backend')


@app.function(image=image, secrets=[modal.Secret.from_name('htn-backend')],
              min_containers=1, max_containers=1, timeout=3600)
@modal.concurrent(max_inputs=100)
@modal.asgi_app()
def fastapi_app():
    from services.backend.app.main import app as web_app
    return web_app
