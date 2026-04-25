from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings


engine = create_engine(settings.db_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)