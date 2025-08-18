# shipstream/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ais_api_key: str
    nats_url: str = "nats://127.0.0.1:4222"
    nats_subject_raw: str = "ais.raw"
    duckdb_path: str = "./data/shipstream.duckdb"

    class Config:
        env_file = ".env"

S = Settings()
