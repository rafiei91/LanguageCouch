from app.schemas.lesson import Lesson
from app.services.pause_builder import PauseBuilder


class TranscriptBuilder:

    @staticmethod
    def build_conversation(
        lesson: Lesson,
    ) -> str:

        transcript = []

        for line in lesson.dialogue:
            transcript.append(
                f"{line.speaker}: {line.danish}"
            )

        return "\n".join(transcript)

    # ----------------------------------------------------------

    @staticmethod
    def build_shadowing(
        lesson: Lesson,
        pause: int = 5,
    ) -> str:

        transcript = []

        for line in lesson.dialogue:

            transcript.append(
                f"{line.speaker}: {line.danish}"
            )

            transcript.append(
                PauseBuilder.build(pause)
            )

        return "\n\n".join(transcript)

    # ----------------------------------------------------------

    @staticmethod
    def build_learning(
        lesson: Lesson,
        short_pause: int = 1,
        long_pause: int = 3,
    ) -> str:

        transcript = []

        for line in lesson.dialogue:

            transcript.append(
                f"{line.speaker}: {line.danish} {PauseBuilder.build(short_pause)} {line.english} {PauseBuilder.build(short_pause)} {line.danish} {PauseBuilder.build(long_pause)}"
            )

        return "\n\n".join(transcript)