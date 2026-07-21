import random

from models.character import Character


class CharacterService:

    def __init__(self):

        self.characters = [
            # Male characters
            Character("Mikkel", "male", "Achird"),
            Character("Lars", "male", "Algenib"),
            Character("Jonas", "male", "Algieba"),
            Character("Oliver", "male", "Alnilam"),
            Character("Magnus", "male", "Charon"),
            Character("Emil", "male", "Enceladus"),
            Character("William", "male", "Orus"),
            Character("Noah", "male", "Puck"),
            Character("Lucas", "male", "Rasalgethi"),

            # Female characters
            Character("Sofie", "female", "Achernar"),
            Character("Emma", "female", "Aoede"),
            Character("Freja", "female", "Autonoe"),
            Character("Anna", "female", "Callirrhoe"),
            Character("Clara", "female", "Despina"),
            Character("Ida", "female", "Erinome"),
            Character("Laura", "female", "Fenrir"),
            Character("Alma", "female", "Kore"),
            Character("Josefine", "female", "Laomedeia"),
            Character("Sara", "female", "Leda"),
            Character("Ella", "female", "Sulafat"),
        ]

    def random_pair(self):

        speaker1, speaker2 = random.sample(self.characters, 2)

        return speaker1, speaker2