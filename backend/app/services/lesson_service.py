from app.ai.real_gemini_service import RealGeminiService
from app.schemas.lesson import Lesson
from app.services.audio_service import AudioService
from app.services.lesson_storage import LessonStorage


class LessonService:
    def __init__(self):
        self.gemini = RealGeminiService()
        self.storage = LessonStorage()
        self.audio = AudioService()

    def list_lessons(self) -> list[Lesson]:
        return self.storage.list()

    def get_lesson(self, lesson_id: str) -> Lesson:
        return self.storage.get(lesson_id)

    def generate_lesson(self, topic: str, level: str) -> Lesson:
        lesson = self.gemini.generate_lesson(topic, level)

        lesson_dir = self.storage.base_dir / lesson.id
        lesson_dir.mkdir(parents=True, exist_ok=True)

        lesson = self.audio.generate(
            lesson,
            lesson_dir,
        )

        self.storage.save(lesson)

        return lesson