from app.schemas.lesson import LessonSummary


class LessonService:
    @staticmethod
    def list_lessons() -> list[LessonSummary]:
        return [
            LessonSummary(
                id=1,
                topic="Introducing yourself",
                level="A1",
            )
        ]