import random
from enum import Enum
from src.until.get_value_enum import GetValueEnum


class Styles(Enum, GetValueEnum):
    _2D = "2D"
    _3D = "3D"

    @staticmethod
    def default_style():
        return Styles._2D

    def get_value(self):
        return self.value
