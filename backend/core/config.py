from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    env: str
    log_level: str
    log_dir: str
    data_dir: str
    api_host: str
    api_port: int
    api_token: str | None


def load_settings() -> Settings:
    load_dotenv()

    def getenv(key: str, default: str | None = None) -> str:
        value = os.getenv(key, default)
        if value is None:
            raise RuntimeError(f"Missing required env var: {key}")
        return value

    return Settings(
        env=os.getenv("LUCY_ENV", "dev"),
        log_level=os.getenv("LUCY_LOG_LEVEL", "INFO"),
        log_dir=os.getenv("LUCY_LOG_DIR", "./data/logs"),
        data_dir=os.getenv("LUCY_DATA_DIR", "./data"),
        api_host=os.getenv("LUCY_API_HOST", "127.0.0.1"),
        api_port=int(os.getenv("LUCY_API_PORT", "8000")),
        api_token=os.getenv("LUCY_API_TOKEN") or None,
    )
