from config import TEXT_MODEL

from models.lesson import Lesson, DialogueLine
from models.lesson_response import LessonResponse
from prompts.lesson_prompt import LessonPrompt
from services.character_service import CharacterService
from services.gemini_service import GeminiService


class LessonGenerator:

    def __init__(self):
        self.gemini = GeminiService()
        self.character_service = CharacterService()

    def generate(self, topic: str, level: str) -> Lesson:

        speaker1, speaker2 = self.character_service.random_pair()

        prompt = LessonPrompt.build(
            topic=topic,
            level=level,
            speaker1=speaker1.name,
            speaker2=speaker2.name,
        )

        lesson_data: LessonResponse = self.gemini.generate(
            model=TEXT_MODEL,
            prompt=prompt,
            response_schema=LessonResponse,
        )

        lesson = Lesson(
            topic=topic,
            level=level,

            speaker1=speaker1,
            speaker2=speaker2,

            dialogue=[
                DialogueLine(**line.model_dump())
                for line in lesson_data.dialogue
            ],

            translation=[
                DialogueLine(**line.model_dump())
                for line in lesson_data.translation
            ],
        )

        return lesson