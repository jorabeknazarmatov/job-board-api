from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
from typing import Optional
from app.core.config import settings
from app.core.logger import logger
from fastapi import HTTPException, status


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#  Hashin password
def get_password_hash(password: str) -> str:
    hash = pwd_context.hash(password)
    logger.debug("password hashing completed")
    return hash

def verify_password(password: str, password_hash: str) -> bool:
    try:
        hash = pwd_context.verify(password, password_hash)
        return hash
    except Exception as e:
        logger.error(f"Password verification failed: {e}")
        raise e

# Create JWT (access and refresh)
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

# Verify JWT (access and refresh)
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        
        user_email: str = payload.get("sub")
        
        if user_email is None:
            logger.error("Token missing 'sub' claim")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No information found in token")
        
        return payload
    
    except JWTError as e:
        logger.error(f"JWT validation error: {str(e)}")        
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token error or expired", headers={"WWW-Authenticate": "Bearer"})

