from google import genai
from google.genai import types

from config import GEMINI_API_KEY


class GeminiService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, model, prompt, response_schema):
        """
        Send a prompt to Gemini and return the parsed response.
        """

        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
            ),
        )

        return response.parsed