import os
from dotenv import load_dotenv

# ==========================================================
# Environment
# ==========================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY not found in .env")


# ==========================================================
# Gemini Models
# ==========================================================

TEXT_MODEL = "gemini-3.5-flash"

TTS_MODEL = "gemini-3.1-flash-tts-preview"


# ==========================================================
# Voices
# ==========================================================

VOICE_MIKKEL = "Kore"

VOICE_SOFIE = "Puck"

# Learning mode narrator

LEARNING_SPEAKER_NAME = "Teacher"

LEARNING_VOICE_NAME = "Kore"

# ==========================================================
# Audio
# ==========================================================

SAMPLE_RATE = 24000

CHANNELS = 1

SAMPLE_WIDTH = 2


# ==========================================================
# Folders
# ==========================================================

LESSONS_FOLDER = "lessons"

AUDIO_FOLDER = "audio"