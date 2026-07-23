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
                f"{line.speaker}: {line.text}"
            )

        return "\n".join(transcript)

    # ----------------------------------------------------------

    @staticmethod
    def build_shadowing(
        lesson: Lesson,
        pause: int = 3,
    ) -> str:

        transcript = []

        for line in lesson.dialogue:

            transcript.append(
                f"{line.speaker}: {line.text}"
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

        for dialogue, translation in zip(
            lesson.dialogue,
            lesson.translation,
        ):

            transcript.append(
                f"{dialogue.speaker}: {dialogue.text} {PauseBuilder.build(short_pause)} {translation.text} {PauseBuilder.build(short_pause)} {dialogue.text} {PauseBuilder.build(long_pause)}"
            )

        return "\n\n".join(transcript)