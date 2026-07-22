from fastapi import APIRouter

from app.services.lesson_service import LessonService
from app.schemas.lesson import LessonSummary
from app.schemas.generate_lesson import GenerateLessonRequest
from app.schemas.generated_lesson import GeneratedLesson

router = APIRouter(prefix="/lessons", tags=["Lessons"])


@router.get("/", response_model=list[LessonSummary])
def list_lessons():
    return LessonService.list_lessons()

@router.post("/generate", response_model=GeneratedLesson)
def generate_lesson(request: GenerateLessonRequest):
    return GeneratedLesson(
        topic=request.topic,
        level=request.level,
        dialogue=[
            "Hej!",
            "Hej! Hvordan har du det?",
            "Jeg har det godt.",
        ],
    )