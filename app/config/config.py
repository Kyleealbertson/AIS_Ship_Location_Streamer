# filepath: /Users/kyle_albertson/AIS_Ship_Location_Streamer/app/Config/config.py
from pydantic_settings import BaseSettings  # Correct import
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/kyle_albertson/AIS_Ship_Location_Streamer/app/Config/.env")

import os
print(os.environ.get("AIS_API_KEY"))
print(os.environ.get("AIS_API_URL"))

class Settings(BaseSettings):
    ais_api_key: str
    nats_url: str = "nats://127.0.0.1:4222"
    nats_subject_raw: str = "ais.raw"
    duckdb_path: str = "./data/shipstream.duckdb"

    class Config:
        env_file = ".env"