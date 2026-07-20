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

    print("Lesson saved successfully!")


if __name__ == "__main__":
    main()