class PauseBuilder:

    @staticmethod
    def build(seconds: int) -> str:
        """
        Build an approximate pause for Gemini TTS.

        Example:
            1 ->
                (1 seconds pause)

            2 ->
                (1 seconds pause)
                (1 seconds pause)

            3 ->
                (1 seconds pause)
                (1 seconds pause)
                (1 seconds pause)
        """

        if seconds <= 0:
            return ""

        pauses = []

        for _ in range(seconds - 1):
            pauses.append("(1 seconds pause)")

        pauses.append("(1 seconds pause)")

        return "\n".join(pauses)