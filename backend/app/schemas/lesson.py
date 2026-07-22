from pydantic import BaseModel


class LessonSummary(BaseModel):
    id: int
    topic: str
    level: str