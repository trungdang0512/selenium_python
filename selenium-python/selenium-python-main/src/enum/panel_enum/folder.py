import random
from enum import Enum
from src.until.get_value_enum import GetValueEnum

class Folder(Enum, GetValueEnum):
    CAR_RENTAL= "Car Rental"
    MUSIC_LIBRARY= "Music Library"
    SCRIPTING_TECHNIQUES= "Scripting techniques sample"
    SCRUM_BOARD= "Scrum Board"

    def select_random(self):
        values = list(Folder)
        random_option = random.choice(values)
        return random_option

    def get_value(self):
        return self.value