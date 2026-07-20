from services.gemini_service import GeminiService
from services.lesson_storage import LessonStorage


def main():

    gemini = GeminiService()
    storage = LessonStorage()

    lesson = gemini.generate_lesson(
        topic="Introducing yourself",
        level="A1"
    )

    storage.save(
        lesson,
        "lessons/lesson_001.json"
    )

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

    print("\nLesson saved successfully!")


if __name__ == "__main__":
    main()