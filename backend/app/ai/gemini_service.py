from abc import ABC, abstractmethod

from app.schemas.generated_lesson import GeneratedLesson


class BaseGeminiService(ABC):
    @abstractmethod
    def generate_lesson(self, topic: str, level: str) -> GeneratedLesson:
        """Generate a language lesson."""
        pass
    