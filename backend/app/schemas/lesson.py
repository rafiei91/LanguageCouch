from pydantic import BaseModel, Field
from uuid import uuid4

from app.schemas.character import Character
from app.schemas.vocabulary import Vocabulary


class DialogueLine(BaseModel):
    speaker: str
    text: str

class Lesson(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    topic: str
    level: str

    speaker1: Character
    speaker2: Character

    dialogue: list[DialogueLine]
    translation: list[DialogueLine]

    vocabulary: list[Vocabulary] = Field(default_factory=list)

    conversation_audio: str = ""
    learning_audio: str = ""
    shadowing_audio: str = ""