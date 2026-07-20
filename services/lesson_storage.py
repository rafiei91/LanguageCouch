import json
from dataclasses import asdict

from models.lesson import Lesson


class LessonStorage:

    def save(self, lesson: Lesson, filename: str):

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(
                asdict(lesson),
                f,
                ensure_ascii=False,
                indent=4
            )