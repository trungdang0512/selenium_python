import random
from enum import Enum
from src.until.get_value_enum import GetValueEnum


class SeriesOptions(Enum, GetValueEnum):
    NAME = "name"
    LOCATION = "location"
    DESCRIPTION = "description"
    REVISION_TIMESTAMP = "revision timestamp"
    ASSIGNED_USER = "assigned"
    STATUS = "status"
    LAST_UPDATE_DATE = "update date"
    LAST_UPDATE_BY = "updated by"
    CREATION_DATE = "creation date"
    CREATED_BY = "created by"
    NOTES = "notes"
    URL = "url"
    DEFAULT = "Select a field..."

    def select_random(self):
        values = list(SeriesOptions)
        random_option = random.choice(values)
        return random_option

    def get_value(self):
        return self.value
