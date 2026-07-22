from pydantic import BaseModel


class GeneratedLesson(BaseModel):
    topic: str
    level: str
    dialogue: list[str]