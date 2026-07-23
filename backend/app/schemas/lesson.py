from pydantic import BaseModel, Field
from uuid import uuid4

from app.schemas.character import Character
from app.schemas.vocabulary import Vocabulary


class DialogueLine(BaseModel):
    speaker: str
    danish: str
    english: str


class Lesson(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    topic: str
    level: str

    speaker1: Character
    speaker2: Character

    dialogue: list[DialogueLine]

    vocabulary: list[Vocabulary] = Field(default_factory=list)

    conversation_audio: str | None = None
    learning_audio: str | None = None
    shadowing_audio: str | None = None