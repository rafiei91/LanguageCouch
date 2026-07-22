from services.audio_service import AudioService
from models.character import Character
from models.lesson import Lesson

speaker1 = Character("Mikkel", "male", "Achird")
speaker2 = Character("Sofie", "female", "Aoede")

lesson = Lesson(
    topic="Test",
    level="A1",
    speaker1=speaker1,
    speaker2=speaker2,
    dialogue=[],
    translation=[],
)

audio = AudioService()

tests = {
    "pause_text.wav": """
Mikkel: Hej Sofie.

Sofie: Hej Mikkel.
""",
}

for filename, transcript in tests.items():
    print(f"Generating {filename}")

    audio.generate(
        lesson,
        transcript,
        f"audios/{filename}",
    )

print("Done.")