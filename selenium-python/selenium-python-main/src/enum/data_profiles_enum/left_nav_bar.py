from enum import Enum


class LeftNavBar(Enum):
    GENERAL_SETTINGS = "General Settings"
    DISPLAY_FIELDS = "Display Fields"
    SORT_FIELDS = "Sort Fields"
    FILTER_FIELDS = "Filter Fields"
    STATISTIC_FIELDS = "Statistic Fields"

    def get_value(self):
        return self.value
