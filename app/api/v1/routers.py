from fastapi import APIRouter, Depends, HTTPException
from app.api.v1.endpoints import user
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.api.deps import get_db


api_router = APIRouter()

@api_router.get("/")
async def get_status():
    return {"status": "ok", "version": "v1"}

@api_router.get("/health")
async def get_health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Datebase connected fail: {str(e)}"
        )
    return {"db": "connected"}

api_router.include_router(user.router, prefix="/users", tags=["users"])