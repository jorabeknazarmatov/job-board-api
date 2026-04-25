from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.user import User


router = APIRouter()

@router.get("/users")
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users