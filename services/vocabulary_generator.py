from config import TEXT_MODEL

from models.lesson import Lesson
from models.vocabulary import Vocabulary
from models.vocabulary_response import VocabularyListResponse
from prompts.vocabulary_prompt import VocabularyPrompt
from services.gemini_service import GeminiService


class VocabularyGenerator:

    def __init__(self):
        self.gemini = GeminiService()

    def generate(self, lesson: Lesson) -> list[Vocabulary]:

        prompt = VocabularyPrompt.build(lesson)

        response: VocabularyListResponse = self.gemini.generate(
            model=TEXT_MODEL,
            prompt=prompt,
            response_schema=VocabularyListResponse,
        )

        vocabulary = [
            Vocabulary(**item.model_dump())
            for item in response.vocabulary
        ]

        return vocabulary