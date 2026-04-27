from fastapi import APIRouter, Depends, HTTPException
from app.api.v1.endpoints import user
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.api.deps import get_db
from app.core.logger import logger


api_router = APIRouter()

@api_router.get("/")
async def get_status():
    logger.info(f"\"/\" request status: 200")
    return {"status": "ok", "version": "v1"}

@api_router.get("/health")
async def get_health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        logger.info(f"Health check passed: Database connected")
        
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        logger.error(f"Health check failed: Database connection failed: {str(e)}")
        
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )

api_router.include_router(user.router, prefix="/users", tags=["users"])