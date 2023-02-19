import os

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    APP_ENV: str
    ROOT_PATH: str
    DEBUG: bool
    VERSION: str
    POSTGRES_DSN: PostgresDsn
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


class DebugConfig(Settings):
    pass


def resolve_settings() -> Settings:
    environment = os.environ.get("APP_ENV")

    if environment == "test":
        settings = DebugConfig(db_name="pytest")
    elif environment == "DEV":
        settings = DebugConfig()
    else:
        settings = Settings()

    return settings
