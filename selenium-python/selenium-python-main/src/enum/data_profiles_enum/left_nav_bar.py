from enum import Enum
from src.until.get_value_enum import GetValueEnum


class LeftNavBar(Enum, GetValueEnum):
    GENERAL_SETTINGS = "General Settings"
    DISPLAY_FIELDS = "Display Fields"
    SORT_FIELDS = "Sort Fields"
    FILTER_FIELDS = "Filter Fields"
    STATISTIC_FIELDS = "Statistic Fields"

    def get_value(self):
        return self.value
