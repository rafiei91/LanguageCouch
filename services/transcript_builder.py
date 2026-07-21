class TranscriptBuilder:

    @staticmethod
    def conversation(lesson):
        """
        Build a conversation transcript from a Lesson object.
        """

        return "\n".join(
            f"{line.speaker}: {line.text}"
            for line in lesson.dialogue
        )