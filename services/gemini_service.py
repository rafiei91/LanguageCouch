import json

from google import genai

from config import GEMINI_API_KEY
from models.lesson import Lesson, DialogueLine


class GeminiService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_lesson(self, topic: str, level: str) -> Lesson:

        prompt = f"""
You are an expert Danish teacher.

Create a Danish lesson.

Requirements:
- Topic: {topic}
- Level: {level}
- Exactly 6 dialogue lines.
- Two speakers only: Mikkel and Sofie.
- Natural everyday Danish.

Return ONLY valid JSON in exactly this format:

{{
  "dialogue": [
    {{
      "speaker": "Mikkel",
      "text": "Hej!"
    }}
  ],
  "translation": [
    {{
      "speaker": "Mikkel",
      "text": "Hi!"
    }}
  ]
}}
"""

        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        data = json.loads(response.text)

        dialogue = [
            DialogueLine(
                speaker=line["speaker"],
                text=line["text"]
            )
            for line in data["dialogue"]
        ]

        translation = [
            DialogueLine(
                speaker=line["speaker"],
                text=line["text"]
            )
            for line in data["translation"]
        ]

        return Lesson(
            topic=topic,
            level=level,
            dialogue=dialogue,
            translation=translation
        )