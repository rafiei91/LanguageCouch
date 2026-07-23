from pathlib import Path

from google import genai
from google.genai import types

from app.core.config import settings
from app.schemas.lesson import Lesson
from app.services.audio_composer import AudioComposer


class RealTtsService:

    def __init__(self):
        self.client = genai.Client(api_key=settings.gemini_api_key)

    # ----------------------------------------------------------

    def generate(
        self,
        transcript: str,
        lesson: Lesson,
        output_path: Path,
    ) -> None:

        speaker_configs = self._build_voice_config(
            lesson.speaker1,
            lesson.speaker2,
        )

        pcm = self._generate_audio(
            transcript,
            speaker_configs,
        )
        #print(transcript)
        #print("\n==============================")

        composer = AudioComposer()
        composer.add_audio(pcm)
        composer.save(str(output_path))

    # ----------------------------------------------------------

    def _build_voice_config(
        self,
        speaker1,
        speaker2,
    ):

        return [
            types.SpeakerVoiceConfig(
                speaker=speaker1.name,
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=speaker1.voice
                    )
                ),
            ),
            types.SpeakerVoiceConfig(
                speaker=speaker2.name,
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=speaker2.voice
                    )
                ),
            ),
        ]

    # ----------------------------------------------------------

    def _generate_audio(
        self,
        transcript: str,
        speaker_configs,
    ) -> bytes:

        response = self.client.models.generate_content(
            model=settings.tts_model,
            contents=transcript,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                        speaker_voice_configs=speaker_configs,
                    )
                ),
            ),
        )

        return response.candidates[0].content.parts[0].inline_data.data