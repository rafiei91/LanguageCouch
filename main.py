from services.lesson_generator import LessonGenerator
from services.vocabulary_generator import VocabularyGenerator
from services.audio_script_builder import AudioScriptBuilder
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

    audio_service = AudioService()
    lesson_storage = LessonStorage()

    builder = AudioScriptBuilder()

    conversation = builder.conversation(lesson)

    audio_service.generate(
        lesson,
        conversation,
        "audios/conversation.wav",
    )

    lesson.conversation_audio = "audios/conversation.wav"

    shadowing = builder.shadowing(lesson)

    audio_service.generate(
        lesson,
        shadowing,
        "audios/shadowing.wav",
    )

    lesson.shadowing_audio = "audios/shadowing.wav"

    learning = builder.learning(lesson)

    audio_service.generate(
        lesson,
        learning,
        "audios/learning.wav",
    )

    lesson.learning_audio = "audios/learning.wav"

    lesson_storage.save(
        lesson,
        "lessons/lesson.json",
    )


if __name__ == "__main__":
    main()