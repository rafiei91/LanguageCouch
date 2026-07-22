from services.pause_builder import PauseBuilder


class AudioScriptBuilder:

    @staticmethod
    def conversation(lesson):

        transcript = ""

        for line in lesson.dialogue:
            transcript += f"{line.speaker}: {line.text}\n"

        return transcript.strip()

    # ----------------------------------------------------------

    @staticmethod
    def shadowing(
        lesson,
        pause=3,
    ):

        transcript = ""

        for line in lesson.dialogue:

            transcript += f"{line.speaker}: {line.text}\n\n"

            transcript += PauseBuilder.build(pause)

            transcript += "\n\n"

        return transcript.strip()

    # ----------------------------------------------------------

    @staticmethod
    def learning(
        lesson,
        short_pause=1,
        long_pause=3,
    ):

        transcript = ""

        for dialogue, translation in zip(
            lesson.dialogue,
            lesson.translation,
        ):

            transcript += dialogue.text
            transcript += "\n\n"

            transcript += PauseBuilder.build(short_pause)

            transcript += "\n\n"

            transcript += translation.text

            transcript += "\n\n"

            transcript += PauseBuilder.build(short_pause)

            transcript += "\n\n"

            transcript += dialogue.text

            transcript += "\n\n"

            transcript += PauseBuilder.build(long_pause)

            transcript += "\n\n"

        return transcript.strip()