from dataclasses import dataclass


@dataclass(frozen=True)
class Character:
    name: str
    gender: str
    voice: str