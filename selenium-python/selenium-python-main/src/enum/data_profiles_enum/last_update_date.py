import random
from enum import Enum
from src.until.get_value_enum import GetValueEnum


class LastUpdateDateValue(Enum, GetValueEnum):
    TODAY = "Today"
    YESTERDAY = "Yesterday"
    THIS_WEEK = "This week"
    LAST_WEEK = "Last week"
    THIS_MONTH = "This month"
    LAST_MONTH = "Last month"
    LAST_3_MONTHS = "Last 3 months"
    DATE_RANGE = "Date Range"
    BEFORE = "Before"
    AFTER = "After"
    CHOOSE_DATE = "Choose Date"

    def get_value(self):
        return self.value
