from google import genai
from google.genai import types

from config import (
    GEMINI_API_KEY,
    TTS_MODEL,
)

from services.audio_composer import AudioComposer


class AudioService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(
        self,
        lesson,
        transcript: str,
        output_file: str,
    ):
        """
        Generate a two-speaker conversation audio from a Lesson.
        """

        speaker_configs = self._build_voice_config(
            lesson.speaker1,
            lesson.speaker2,
        )

        pcm = self._generate_audio(
            transcript,
            speaker_configs,
        )

        composer = AudioComposer()
        composer.add_audio(pcm)
        composer.save(output_file)

        lesson.conversation_audio = output_file

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
        transcript,
        speaker_configs,
    ):

        response = self.client.models.generate_content(
            model=TTS_MODEL,
            contents=transcript,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                        speaker_voice_configs=speaker_configs
                    )
                ),
            ),
        )

        return response.candidates[0].content.parts[0].inline_data.data