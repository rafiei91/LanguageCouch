import json
import os
from dataclasses import asdict
from models.lesson import Lesson

class LessonStorage:

    def save(self, lesson: Lesson, filename: str):
        
        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True,
        )

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(
                asdict(lesson),
                f,
                ensure_ascii=False,
                indent=4
            )