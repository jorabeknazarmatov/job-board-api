from sqlalchemy.orm import Session
from app.models.token import Token
from datetime import datetime
from app.core.logger import logger


def create_refresh_token_db(db: Session, token: str, user_id: int, expires_at: datetime):
    db_obj = Token(
        token=token,
        user_id=user_id,
        expires_at=expires_at
    )
    
    try:
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        logger.debug(f"User created successfully: {db_obj.email}")
        return db_obj
    
    except Exception as e:
        db.rollback()
        logger.error(f"Database error during user creation: {e}")
        raise e

def delete_refresh_token(db: Session, token: str):
    db_token = db.query(Token).filter(Token.token == token).first()
    
    try:
        if db_token:
            db.delete(db_token)
            db.commit()
        return db_token
    except Exception as e:
        logger.error(f"Database error during user creation: {e}")
        raise e