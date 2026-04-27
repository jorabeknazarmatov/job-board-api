from app.db.session import SessionLocal
from app.core.logger import logger


def get_db():
    db = SessionLocal()
    logger.debug("Database session created")
    
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {e}")
        raise
    finally:
        logger.debug("Database session closed")        
        db.close()