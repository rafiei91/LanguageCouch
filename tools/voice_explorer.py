from pathlib import Path
import sys
import wave

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from google import genai
from google.genai import types

from config import GEMINI_API_KEY, TTS_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)

OUTPUT_DIR = Path("voice_samples")
OUTPUT_DIR.mkdir(exist_ok=True)

voices = [
    "Achernar",
    "Achird",
    "Algenib",
    "Algieba",
    "Alnilam",
    "Aoede",
    "Autonoe",
    "Callirrhoe",
    "Charon",
    "Despina",
    "Enceladus",
    "Erinome",
    "Fenrir",
    "Kore",
    "Laomedeia",
    "Leda",
    "Orus",
    "Puck",
    "Rasalgethi",
    "Sulafat",
]

script = """
Hej!

Mit navn er Emil.

Jeg lærer dansk hver dag.

Jeg kan godt lide at læse bøger, drikke kaffe og gå en tur.

Tak fordi du lytter.
"""

for i, voice in enumerate(voices, start=1):

    print(f"Generating {voice}")

    response = client.models.generate_content(
        model=TTS_MODEL,
        contents=script,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=voice
                    )
                )
            ),
        ),
    )

    audio = response.candidates[0].content.parts[0].inline_data.data

    filename = OUTPUT_DIR / f"{i:02d}_{voice}.wav"

    with wave.open(str(filename), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(audio)

print("\nDone!")
print(f"Generated {len(voices)} voice samples.")