from enum import Enum
from src.until.get_value_enum import GetValueEnum


class FilterFields(Enum, GetValueEnum):
    RECENT_RESULT = "Recent result"
    LAST_UPDATE_DATE = "Last update date"

    def get_value(self):
        return self.value
