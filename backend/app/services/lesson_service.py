from app.ai.mock_gemini_service import MockGeminiService
from app.schemas.generated_lesson import GeneratedLesson
from app.schemas.lesson import LessonSummary


class LessonService:
    def __init__(self):
        self.gemini = MockGeminiService()

    def list_lessons(self) -> list[LessonSummary]:
        return [
            LessonSummary(
                id=1,
                topic="Introducing yourself",
                level="A1",
            )
        ]

    def generate_lesson(self, topic: str, level: str) -> GeneratedLesson:
        return self.gemini.generate_lesson(topic, level)