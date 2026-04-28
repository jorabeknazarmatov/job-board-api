from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.logger import logger
from app.models.user import User
from jose import jwt, JWTError
from app.core.config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

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

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={"WWW-Authenticate": "Bearer"}, detail="User not found")
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        
        if email is None:
            logger.error("JWT payload missing 'sub' claim")
            raise credentials_exception
        
    except JWTError as e:
        logger.error(f"JWT decode error: {str(e)}")
        raise credentials_exception
    
    user = db.query(User).filter(User.email == email).first()
    
    if user is None:
        logger.warning(f"User with email {email} not found in database")
        raise credentials_exception
    
    return user