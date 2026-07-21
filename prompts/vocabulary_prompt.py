from models.lesson import Lesson


class VocabularyPrompt:

    @staticmethod
    def build(lesson: Lesson) -> str:

        dialogue = "\n".join(
            f"{line.speaker}: {line.text}"
            for line in lesson.dialogue
        )

        return f"""
You are creating vocabulary for a Danish language learner.

Below is a Danish dialogue.

{dialogue}

Extract the 10 most useful vocabulary entries for a CEFR {lesson.level} learner.

Rules:

- Only use words or short expressions that actually appear in the dialogue.
- Prefer useful everyday vocabulary.
- Do NOT include people's names.
- Do NOT invent new vocabulary.
- Each example sentence must come directly from the dialogue.
- Translate naturally into English.
- Return only the requested structured response.
"""