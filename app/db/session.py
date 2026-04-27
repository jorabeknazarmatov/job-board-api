from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings
from app.core.logger import logger

try:
    engine = create_engine(settings.db_url)
    with engine.connect() as connection:
        logger.info("Database connection established successfully")
except Exception as e:
    logger.critical(f"Could not connect to database: {e}")
    raise e


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
logger.debug("Created Sessionmaker")