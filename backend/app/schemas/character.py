from pydantic import BaseModel


class Character(BaseModel):
    name: str
    gender: str
    voice: str