from fastapi import FastAPI
from app.api.v1.routers import api_router
from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.core.logger import logger

logger.info("Start project: Job Board API")
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Board API")
app.include_router(api_router, prefix="/api/v1")