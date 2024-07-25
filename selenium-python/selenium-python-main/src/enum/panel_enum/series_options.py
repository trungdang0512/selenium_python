import random
from enum import Enum


class SeriesOptions(Enum):
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

    @classmethod
    def select_random_series(cls):
        return random.choice(list(cls))

    def get_value(self):
        return self.value
