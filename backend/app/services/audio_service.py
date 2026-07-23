from pathlib import Path

from app.ai.real_tts_service import RealTtsService
from app.schemas.lesson import Lesson
from app.services.transcript_builder import TranscriptBuilder


class AudioService:

    def __init__(self):
        self.tts = RealTtsService()

    # ----------------------------------------------------------

    def generate(
        self,
        lesson: Lesson,
        lesson_dir: Path,
    ) -> Lesson:

        audio_dir = lesson_dir / "audio"

        conversation_audio = audio_dir / "conversation.wav"
        learning_audio = audio_dir / "learning.wav"
        shadowing_audio = audio_dir / "shadowing.wav"

        self.tts.generate(
            TranscriptBuilder.build_conversation(lesson),
            lesson,
            conversation_audio,
        )

        self.tts.generate(
            TranscriptBuilder.build_learning(lesson),
            lesson,
            learning_audio,
        )

        self.tts.generate(
            TranscriptBuilder.build_shadowing(lesson),
            lesson,
            shadowing_audio,
        )

        lesson.conversation_audio = (
            f"/media/{lesson.id}/audio/conversation.wav"
        )

        lesson.learning_audio = (
            f"/media/{lesson.id}/audio/learning.wav"
        )

        lesson.shadowing_audio = (
            f"/media/{lesson.id}/audio/shadowing.wav"
        )

        return lesson