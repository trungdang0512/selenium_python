import random
from enum import Enum
from src.until.get_value_enum import GetValueEnum


class ItemType(Enum, GetValueEnum):
    TEST_MODULE = "test module"
    TEST_CASES = "test case"
    TEST_OBJECTIVES = "test objective"
    DATA_SETS = "data set"
    ACTIONS = "action"
    INTERFACE_ENTITIES = "interface entity"
    TEST_RESULTS = "result"
    TEST_CASE_RESULTS = "test case result"
    TEST_SUITES = "test suite"
    BUGS = "bug"

    @staticmethod
    def default_item_type():
        return ItemType.TEST_MODULE

    def select_random(self):
        values = list(ItemType)
        random_option = random.choice(values)
        return random_option

    def get_value(self):
        return self.value
