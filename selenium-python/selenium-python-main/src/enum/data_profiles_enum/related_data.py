import random
from enum import Enum
from src.until.get_value_enum import GetValueEnum


class RelatedData(Enum, GetValueEnum):
    NONE = ""
    RELATED_TEST_RESULTS = "related test results"
    RELATED_BUGS = "related bugs"
    RELATED_TEST_CASES = "related test cases"

    @staticmethod
    def default_ralated_data():
        return RelatedData.NONE

    def get_value(self):
        return self.value
