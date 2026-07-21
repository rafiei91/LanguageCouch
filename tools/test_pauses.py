import wave

from google import genai
from google.genai import types

from config import (
    GEMINI_API_KEY,
    TTS_MODEL,
    SAMPLE_RATE,
    CHANNELS,
    SAMPLE_WIDTH,
)

client = genai.Client(api_key=GEMINI_API_KEY)


def generate(text):

    response = client.models.generate_content(
        model=TTS_MODEL,
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Achird"
                    )
                )
            ),
        ),
    )

    return response.candidates[0].content.parts[0].inline_data.data


def silence(seconds):

    return b"\x00" * (
        SAMPLE_RATE
        * CHANNELS
        * SAMPLE_WIDTH
        * seconds
    )


audio = (
    generate("Hej.")
    + silence(3)
    + generate("Hvordan går det?")
)

with wave.open("audio/shadow_test.wav", "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_WIDTH)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(audio)

print("Done.")