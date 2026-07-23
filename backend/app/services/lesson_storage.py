from pathlib import Path

from app.schemas.lesson import Lesson


class LessonStorage:
    def __init__(self):
        self.base_dir = Path("data/lessons")

    def save(self, lesson: Lesson) -> None:
        lesson_dir = self.base_dir / lesson.id
        lesson_dir.mkdir(parents=True, exist_ok=True)

        (lesson_dir / "audio").mkdir(exist_ok=True)

        lesson_file = lesson_dir / "lesson.json"

        lesson_file.write_text(
            lesson.model_dump_json(indent=2),
            encoding="utf-8",
        )
        
    def list(self) -> list[Lesson]:
        lessons = []

        if not self.base_dir.exists():
            return lessons

        for lesson_file in self.base_dir.glob("*/lesson.json"):
            lesson = Lesson.model_validate_json(
                lesson_file.read_text(encoding="utf-8")
            )
            lessons.append(lesson)

        lessons.sort(key=lambda l: l.id)

        return lessons
    
    def get(self, lesson_id: str) -> Lesson:
        lesson_file = self.base_dir / lesson_id / "lesson.json"

        if not lesson_file.exists():
            raise FileNotFoundError(f"Lesson '{lesson_id}' not found.")

        return Lesson.model_validate_json(
            lesson_file.read_text(encoding="utf-8")
        )