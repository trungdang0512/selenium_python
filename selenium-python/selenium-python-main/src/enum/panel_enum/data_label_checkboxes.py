from enum import Enum
from src.until.get_value_enum import GetValueEnum

class DataLabelsCheckBoxes(Enum, GetValueEnum):
    SERIES= "Series"
    CATEGORIES= "Categories"
    VALUE= "Value"
    PERCENTAGE= "Percentage"

    def get_value(self):
        return self.value