from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.user import User
from app.schemas.user import UserRead


router = APIRouter()

@router.get("/users", response_model=list[UserRead])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users