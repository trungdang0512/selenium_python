from enum import Enum

class DataLabelsCheckBoxes(Enum):
    SERIES= "Series"
    CATEGORIES= "Categories"
    VALUE= "Value"
    PERCENTAGE= "Percentage"

    def get_value(self):
        return self.value