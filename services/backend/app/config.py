from pathlib import Path
from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ROOT / 'services/backend/.env', extra='ignore')
    openai_api_key: str = ''
    openai_model: str = ''
    annotation_model: str = 'gpt-5-mini'
    openai_live_model: str = 'gpt-live-1'
    voice_access_token: str = ''
    voice_enabled: bool = False
    wander_api_key: str = ''
    wander_backend_url: str = ''
    wander_data_root: Path = ROOT / 'maps/assets'
    asset_max_bytes: int = 2 * 1024 * 1024 * 1024
    elasticsearch_url: str = ''
    elasticsearch_api_key: str = ''
    elastic_embedding_endpoint: str = ''
    elastic_rerank_endpoint: str = ''
    elastic_embedding_dims: int = 1024
    elastic_embedding_provider: Literal['jinaai', 'openai'] = 'jinaai'
    graph_path: Path = ROOT / 'maps/navigation/demo_building.json'
