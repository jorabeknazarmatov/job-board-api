from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from app.core.logger import logger


current_file_dir = Path(__file__).resolve().parent
BASE_DIR = current_file_dir.parent.parent
ENV_PATH = BASE_DIR / ".env"

logger.debug(f"Searching for .env file at: {ENV_PATH}")

if not ENV_PATH.exists():
    logger.warning(f".env file NOT found at {ENV_PATH}. Using default environment variables or OS env.")
else:
    logger.info(".env file found and being loaded.")

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_IP: str
    DB_PORT: int
    DB_NAME: str
    ACCESS_TOKEN: int
    REFRESH_TOKEN: int
    ALGORITHM: str
    SECRET_KEY: str
    
    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        extra="ignore"
    )
    
    @property
    def db_url(self):
        logger.debug(f"Database URL generated: postgresql+psycopg2://{self.DB_USER}:***@{self.DB_IP}...")
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_IP}:{self.DB_PORT}/{self.DB_NAME}"

try:
    settings = Settings()
    logger.info("Settings loaded successfully.")
except Exception as e:
    logger.critical(f"Failed to load settings: {e}")
    raise e
