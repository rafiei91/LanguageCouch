from google import genai
from google.genai import types

from app.ai.gemini_service import BaseGeminiService
from app.core.config import settings
from app.prompts.lesson_prompt import LessonPrompt
from app.schemas.lesson import Lesson, DialogueLine
from app.schemas.lesson_response import LessonResponse
from app.services.character_service import CharacterService

class RealGeminiService(BaseGeminiService):
    def __init__(self):
        self.client = genai.Client(api_key=settings.gemini_api_key)
        self.character_service = CharacterService()

    def generate(
        self,
        model: str,
        prompt: str,
        response_schema,
    ):
        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
            ),
        )

        return response.parsed

    def generate_lesson(
        self,
        topic: str,
        level: str,
    ) -> Lesson:

        speaker1, speaker2 = self.character_service.random_pair()

        prompt = LessonPrompt.build(
            topic=topic,
            level=level,
            speaker1=speaker1.name,
            speaker2=speaker2.name,
        )

        lesson_data: LessonResponse = self.generate(
            model=settings.text_model,
            prompt=prompt,
            response_schema=LessonResponse,
        )

        return Lesson(
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