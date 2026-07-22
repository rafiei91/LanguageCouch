from pydantic import BaseModel


class Vocabulary(BaseModel):
    danish: str
    english: str
    example: str