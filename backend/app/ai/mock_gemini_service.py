from app.ai.gemini_service import BaseGeminiService
from app.schemas.generated_lesson import GeneratedLesson


class MockGeminiService(BaseGeminiService):
    def generate_lesson(self, topic: str, level: str) -> GeneratedLesson:
        return GeneratedLesson(
            topic=topic,
            level=level,
            dialogue=[
                "Hej!",
                "Hej! Hvordan har du det?",
                "Jeg har det godt.",
            ],
        )