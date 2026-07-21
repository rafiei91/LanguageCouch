from pydantic import BaseModel


class VocabularyResponse(BaseModel):
    danish: str
    english: str
    example: str


class VocabularyListResponse(BaseModel):
    vocabulary: list[VocabularyResponse]