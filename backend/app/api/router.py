from fastapi import APIRouter

from app.api.health import router as health_router
from app.api.root import router as root_router
from app.api.lessons import router as lessons_router

api_router = APIRouter()

api_router.include_router(root_router)
api_router.include_router(health_router)
api_router.include_router(lessons_router)