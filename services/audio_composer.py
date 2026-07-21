import wave

from config import (
    SAMPLE_RATE,
    CHANNELS,
    SAMPLE_WIDTH,
)


class AudioComposer:

    def __init__(self):
        self._pcm = bytearray()

    # ----------------------------------------------------------

    def add_audio(self, pcm: bytes):

        self._pcm.extend(pcm)

    # ----------------------------------------------------------

    def add_silence(self, seconds: float):

        num_bytes = int(
            SAMPLE_RATE
            * CHANNELS
            * SAMPLE_WIDTH
            * seconds
        )

        self._pcm.extend(b"\x00" * num_bytes)

    # ----------------------------------------------------------

    def save(self, filename: str):

        with wave.open(filename, "wb") as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(SAMPLE_WIDTH)
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(self._pcm)