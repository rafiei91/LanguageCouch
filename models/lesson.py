from dataclasses import dataclass


@dataclass
class Lesson:
    topic: str
    level: str
    content: str