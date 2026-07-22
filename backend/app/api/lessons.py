from fastapi import APIRouter

from app.services.lesson_service import LessonService
from app.schemas.lesson import LessonSummary

router = APIRouter(prefix="/lessons", tags=["Lessons"])


@router.get("/", response_model=list[LessonSummary])
def list_lessons():
    return LessonService.list_lessons()