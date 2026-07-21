from dataclasses import dataclass, field

from models.character import Character


@dataclass
class DialogueLine:
    speaker: str
    text: str


@dataclass
class Lesson:
    topic: str
    level: str

    speaker1: Character
    speaker2: Character

    dialogue: list[DialogueLine]
    translation: list[DialogueLine]

    vocabulary: list = field(default_factory=list)
    grammar: list = field(default_factory=list)
    quiz: list = field(default_factory=list)

    conversation_audio: str = ""
    learning_audio: str = ""
    shadowing_audio: str = ""