import os
import wave

from app.core.config import settings


class AudioComposer:

    def __init__(self):
        self._pcm = bytearray()

    def add_audio(self, pcm: bytes):
        self._pcm.extend(pcm)

    def add_silence(self, seconds: float):
        num_bytes = int(
            settings.sample_rate
            * settings.channels
            * settings.sample_width
            * seconds
        )

        self._pcm.extend(b"\x00" * num_bytes)

    def save(self, filename: str):
        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True,
        )

        with wave.open(filename, "wb") as wf:
            wf.setnchannels(settings.channels)
            wf.setsampwidth(settings.sample_width)
            wf.setframerate(settings.sample_rate)
            wf.writeframes(self._pcm)