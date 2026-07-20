from dataclasses import dataclass


@dataclass
class DialogueLine:
    speaker: str
    text: str


@dataclass
class Lesson:
    topic: str
    level: str
    dialogue: list[DialogueLine]
    translation: list[DialogueLine]