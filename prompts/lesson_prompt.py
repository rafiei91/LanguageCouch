class LessonPrompt:

    @staticmethod
    def build(
        topic: str,
        level: str,
        speaker1: str,
        speaker2: str,
    ) -> str:

        return f"""
You are an expert Danish language teacher.

Create a natural and engaging Danish dialogue for language learners.

Requirements:

- Topic: {topic}
- CEFR level: {level}
- Exactly 6 dialogue lines.
- The two speakers are:
  - {speaker1}
  - {speaker2}
- Alternate naturally between the two speakers.
- Use realistic spoken Danish.
- Keep the language appropriate for the requested CEFR level.
- Stay focused on the topic.
- Avoid repeating the same sentence structure.
- Make the conversation sound authentic and useful for daily life.

For each dialogue line, provide an English translation with the same speaker.
"""