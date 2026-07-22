import random

from app.schemas.character import Character


class CharacterService:

    def __init__(self):

        self.characters = [
            # Male characters
            Character(name="Mikkel", gender="male", voice="Achird"),
            Character(name="Lars", gender="male", voice="Algenib"),
            Character(name="Jonas", gender="male", voice="Algieba"),
            Character(name="Oliver", gender="male", voice="Alnilam"),
            Character(name="Magnus", gender="male", voice="Charon"),
            Character(name="Emil", gender="male", voice="Enceladus"),
            Character(name="William", gender="male", voice="Orus"),
            Character(name="Noah", gender="male", voice="Puck"),
            Character(name="Lucas", gender="male", voice="Rasalgethi"),

            # Female characters
            Character(name="Sofie", gender="female", voice="Achernar"),
            Character(name="Emma", gender="female", voice="Aoede"),
            Character(name="Freja", gender="female", voice="Autonoe"),
            Character(name="Anna", gender="female", voice="Callirrhoe"),
            Character(name="Clara", gender="female", voice="Despina"),
            Character(name="Ida", gender="female", voice="Erinome"),
            Character(name="Laura", gender="female", voice="Fenrir"),
            Character(name="Alma", gender="female", voice="Kore"),
            Character(name="Josefine", gender="female", voice="Laomedeia"),
            Character(name="Sara", gender="female", voice="Leda"),
            Character(name="Ella", gender="female", voice="Sulafat"),
        ]

    def random_pair(self) -> tuple[Character, Character]:
        return tuple(random.sample(self.characters, 2))