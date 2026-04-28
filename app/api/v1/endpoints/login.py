from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.user import User
from app.schemas.user import UserLoginSchema
from app.core.security import create_access_token, create_refresh_token, verify_password
from app.crud.token import create_refresh_token_db
from app.core.config import settings
from datetime import datetime, timezone, timedelta


router = APIRouter()

@router.post("/login")
def login(login_data: UserLoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.email).first()
    
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or password incorrect"
        )
        
    token_data = {"sub": user.email}
    
    access_token = create_access_token(data=token_data)
    refresh_token = create_refresh_token(data=token_data)
    
    expire_date = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN)
    
    create_refresh_token_db(
        db=db, 
        token=refresh_token, 
        user_id=user.id, 
        expires_at=expire_date
    )
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }