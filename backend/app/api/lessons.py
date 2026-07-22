from fastapi import APIRouter

from app.schemas.generate_lesson import GenerateLessonRequest
from app.schemas.generated_lesson import GeneratedLesson
from app.schemas.lesson import LessonSummary
from app.services.lesson_service import LessonService

router = APIRouter(prefix="/lessons", tags=["Lessons"])

lesson_service = LessonService()


@router.get("/", response_model=list[LessonSummary])
def list_lessons():
    return lesson_service.list_lessons()


@router.post("/generate", response_model=GeneratedLesson)
def generate_lesson(request: GenerateLessonRequest):
    return lesson_service.generate_lesson(
        topic=request.topic,
        level=request.level,
    )