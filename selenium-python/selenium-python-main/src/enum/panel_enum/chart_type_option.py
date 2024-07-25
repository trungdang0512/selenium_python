import random
from enum import Enum



class ChartTypeOptions(Enum):
    PIE = "Pie"
    SINGLE_BAR = "Single Bar"
    STACKED_BAR = "Stacked Bar"
    GROUP_BAR = "Group Bar"
    LINE = "Line"

    def select_random(self):
        values = list(ChartTypeOptions)
        random_option = random.choice(values)
        return random_option

    def get_value(self):
        return self.value
