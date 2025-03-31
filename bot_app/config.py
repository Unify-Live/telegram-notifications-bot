from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    # Version
    VERSION: str = "dev"

    # Backend api connection
    BACKEND_API_HOST: str = "http://localhost:5000/public"

    # aiogram settings
    WEBHOOK_HOST: str = ""
    TELEGRAM_API_SECRET: str = ""
    TELEGRAM_BOT_TOKEN: str = ""

    # FastAPI settings
    BASE_URL: str = ""
    SERVER_PORT: str = "2000"
    SERVER_ADDRESS: str = "0.0.0.0"

    # Database settings
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "root"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "main_unify_telegram_tg_notifications_db"

    FASTAPI_BASE_PATH: str = ""

    @property
    def DATABASE_URL(self) -> str:
        """Construct database URL."""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"


settings = Settings()

__version__ = settings.VERSION
