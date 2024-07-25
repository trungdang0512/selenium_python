from enum import Enum


class FilterFields(Enum):
    RECENT_RESULT = "Recent result"
    LAST_UPDATE_DATE = "Last update date"

    def get_value(self):
        return self.value
