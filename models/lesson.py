from dataclasses import dataclass, field

from models.character import Character
from models.vocabulary import Vocabulary


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

    vocabulary: list[Vocabulary] = field(default_factory=list)

    conversation_audio: str = ""
    learning_audio: str = ""
    shadowing_audio: str = ""