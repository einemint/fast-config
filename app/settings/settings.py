from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from urllib.parse import quote_plus

_ENV_FILE = Path(__file__).resolve().parent.parent.parent / ".env"


class DBSettings(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    @property
    def db_url_asyncpg(self) -> str:
        password = quote_plus(self.db_password)
        return f"postgresql+asyncpg://{self.db_user}:{password}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def db_url_psycopg(self) -> str:
        password = quote_plus(self.db_password)
        return f"postgresql+psycopg://{self.db_user}:{password}@{self.db_host}:{self.db_port}/{self.db_name}"

    model_config = SettingsConfigDict(env_file=_ENV_FILE, env_file_encoding="utf-8", extra="ignore")


class RedisSettings(BaseSettings):
    redis_host: str
    redis_port: int
    redis_password: str
    redis_db_app: str
    redis_db_celery: str

    @property
    def redis_url_app(self) -> str:
        if self.redis_password:
            password = quote_plus(self.redis_password)
            return f"redis://:{password}@{self.redis_host}:{self.redis_port}/{self.redis_db_app}"
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db_app}"

    @property
    def redis_url_celery(self) -> str:
        if self.redis_password:
            password = quote_plus(self.redis_password)
            return f"redis://:{password}@{self.redis_host}:{self.redis_port}/{self.redis_db_celery}"
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db_celery}"

    model_config = SettingsConfigDict(env_file=_ENV_FILE, env_file_encoding="utf-8", extra="ignore")

class AdminSettings(BaseSettings):
    enable_admin_panel: bool = True

    model_config = SettingsConfigDict(env_file=_ENV_FILE, env_file_encoding="utf-8", extra="ignore")

class Settings(BaseSettings):
    db_settings: DBSettings = DBSettings()
    redis_settings: RedisSettings = RedisSettings()
    admin_settings: AdminSettings = AdminSettings()


settings = Settings()