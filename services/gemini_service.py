from google import genai
from config import GEMINI_API_KEY
from models.lesson import Lesson

class GeminiService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_lesson(self, topic, level):

        prompt = f"""
    You are an expert Danish teacher.

    Create a very short Danish lesson.

    Requirements:
    - Level: {level}
    - Topic: {topic}
    - Exactly 6 dialogue lines.
    - Two speakers: Mikkel and Sofie.
    - Natural everyday Danish.
    - After the dialogue, provide an English translation.

    Format:

    Mikkel:
    ...

    Sofie:
    ...

    English Translation:
    ...
    """

        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return Lesson(
            topic=topic,
            level=level,
            content=response.text
        )