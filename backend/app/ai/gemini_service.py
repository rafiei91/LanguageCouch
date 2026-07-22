from abc import ABC, abstractmethod

from app.schemas.lesson import Lesson


class BaseGeminiService(ABC):
    @abstractmethod
    def generate_lesson(self, topic: str, level: str) -> Lesson:
        """Generate a language lesson."""
        pass
    