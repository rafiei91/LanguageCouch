from fastapi import APIRouter

from app.schemas.generate_lesson import GenerateLessonRequest
from app.schemas.lesson import Lesson
from app.services.lesson_service import LessonService

router = APIRouter(prefix="/lessons", tags=["Lessons"])

lesson_service = LessonService()


@router.get("/", response_model=list[Lesson])
def list_lessons():
    return lesson_service.list_lessons()


@router.post("/generate", response_model=Lesson)
def generate_lesson(request: GenerateLessonRequest):
    return lesson_service.generate_lesson(
        topic=request.topic,
        level=request.level,
    )
    
@router.get("/{lesson_id}", response_model=Lesson)
def get_lesson(lesson_id: str):
    return lesson_service.get_lesson(lesson_id)