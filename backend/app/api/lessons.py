from fastapi import APIRouter

from app.schemas.lesson import LessonSummary

router = APIRouter(prefix="/lessons", tags=["Lessons"])


@router.get("/", response_model=list[LessonSummary])
def list_lessons():
    return [
        LessonSummary(
            id=1,
            topic="Introducing yourself",
            level="A1",
        )
    ]