from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    app_name: str = "LanguageCouch API"
    app_version: str = "0.1.0"
    debug: bool = True

    gemini_api_key: str = ""
    text_model: str = "gemini-3.5-flash"
    
    tts_model: str = "gemini-2.5-flash-preview-tts"

    sample_rate: int = 24000
    channels: int = 1
    sample_width: int = 2

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()