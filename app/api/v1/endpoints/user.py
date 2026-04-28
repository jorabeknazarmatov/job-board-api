from fastapi import APIRouter, Depends
from app.api.deps import get_current_user
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.user import User
from app.schemas.user import UserRead


router = APIRouter()

@router.get("/users", response_model=list[UserRead])
async def read_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    users = db.query(User).all()
    return users