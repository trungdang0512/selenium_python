import random
from enum import Enum
from src.until.get_value_enum import GetValueEnum


class Legends(Enum, GetValueEnum):
    NONE = "None"
    TOP = "Top"
    RIGHT = "Right"
    BOTTOM = "Bottom"
    LEFT = "Left"

    @staticmethod
    def default_legend():
        return Legends.BOTTOM

    def select_random(self):
        values = list(Legends)
        random_option = random.choice(values)
        return random_option

    def get_value(self):
        return self.value
