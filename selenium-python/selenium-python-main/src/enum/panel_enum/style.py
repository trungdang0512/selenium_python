import random
from enum import Enum


class Styles(Enum):
    _2D = "2D"
    _3D = "3D"

    @staticmethod
    def default_style():
        return Styles._2D

    def get_value(self):
        return self.value
