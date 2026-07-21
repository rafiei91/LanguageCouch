from services.lesson_generator import LessonGenerator
from services.vocabulary_generator import VocabularyGenerator
from services.transcript_builder import TranscriptBuilder
from services.audio_service import AudioService
from services.lesson_storage import LessonStorage


def main():

    lesson_generator = LessonGenerator()
    vocabulary_generator = VocabularyGenerator()

    lesson = lesson_generator.generate(
        topic="Restaurant",
        level="A1",
    )

    lesson.vocabulary = vocabulary_generator.generate(lesson)

    transcript_builder = TranscriptBuilder()
    audio_service = AudioService()
    lesson_storage = LessonStorage()

    conversation = transcript_builder.conversation(lesson)

    audio_service.generate(
        lesson,
        conversation,
        "conversation.wav",
    )

    lesson_storage.save(
        lesson,
        "lessons/lesson.json"
    )


if __name__ == "__main__":
    main()