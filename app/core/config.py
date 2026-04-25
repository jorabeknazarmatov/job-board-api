from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


current_file_dir = Path(__file__).resolve().parent
BASE_DIR = current_file_dir.parent.parent
ENV_PATH = BASE_DIR / ".env"

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_IP: str
    DB_PORT: int
    DB_NAME: str
    
    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        extra="ignore"
    )
    
    @property
    def db_url(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_IP}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()
