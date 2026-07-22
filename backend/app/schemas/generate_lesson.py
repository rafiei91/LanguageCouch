from pydantic import BaseModel


class GenerateLessonRequest(BaseModel):
    topic: str
    level: str