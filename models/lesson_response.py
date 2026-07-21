from pydantic import BaseModel


class DialogueLineResponse(BaseModel):
    speaker: str
    text: str


class LessonResponse(BaseModel):
    dialogue: list[DialogueLineResponse]
    translation: list[DialogueLineResponse]