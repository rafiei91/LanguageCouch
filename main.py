from services.lesson_generator import LessonGenerator
from services.lesson_storage import LessonStorage
from services.audio_service import AudioService
from services.transcript_builder import TranscriptBuilder

def main():

    # Create services
    lesson_generator = LessonGenerator()
    storage = LessonStorage()
    audio = AudioService()

    # Generate lesson
    lesson = lesson_generator.generate(
        topic="Restaurant",
        level="A1",
    )

    # Generate conversation audio
    transcript = TranscriptBuilder.conversation(lesson)

    audio.generate(
        lesson=lesson,
        transcript=transcript,
        output_file="audio/lesson_001_conversation.wav",
    )

    lesson.conversation_audio = "audio/lesson_001_conversation.wav"

    # Save lesson (including audio filename)
    storage.save(
        lesson,
        "lessons/lesson_001.json"
    )

    # Display lesson
    print(f"Topic: {lesson.topic}")
    print(f"Level: {lesson.level}")

    print("\nDialogue")
    print("-" * 30)

    for line in lesson.dialogue:
        print(f"{line.speaker}: {line.text}")

    print("\nTranslation")
    print("-" * 30)

    for line in lesson.translation:
        print(f"{line.speaker}: {line.text}")

    print("\nConversation audio:")
    print(lesson.conversation_audio)

    print("\nLesson saved successfully!")


if __name__ == "__main__":
    main()