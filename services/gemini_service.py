from google import genai
from google.genai import types

from config import GEMINI_API_KEY, TEXT_MODEL
from models.lesson import Lesson, DialogueLine
from models.lesson_response import LessonResponse
from prompts.lesson_prompt import LessonPrompt
from services.character_service import CharacterService


class GeminiService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.character_service = CharacterService()

    def generate_lesson(self, topic: str, level: str) -> Lesson:
        """
        Generate a Danish lesson using Gemini.
        """

        speaker1, speaker2 = self.character_service.random_pair()

        prompt = LessonPrompt.build(
            topic=topic,
            level=level,
            speaker1=speaker1.name,
            speaker2=speaker2.name,
        )

        response = self.client.models.generate_content(
            model=TEXT_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=LessonResponse,
            ),
        )

        lesson_data: LessonResponse = response.parsed

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