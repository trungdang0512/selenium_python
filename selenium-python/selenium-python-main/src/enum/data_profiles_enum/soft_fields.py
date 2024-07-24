from enum import Enum
from src.until.get_value_enum import GetValueEnum


class SortFields(Enum, GetValueEnum):
    DEFAULT = "--- Select field ---"
    NAME = "Name"
    LOCATION = "Location"
    DESCRIPTION = "Description"
    RECENT_RESULT = "Recent result"
    SOURCE = "Source"
    REVISION_TIMESTAMP = "Revision Timestamp"
    ASSIGNED_USER = "Assigned user"
    PRIORITY = "Priority"
    STATUS = "Status"
    LAST_UPDATE_DATE = "Last update date"
    LAST_UPDATE_BY = "Last updated by"
    CREATION_DATE = "Creation date"
    CREATED_BY = "Created by"
    NOTES = "Notes"
    CHECK_OUT_BY = "Check out by"
    URL = "URL"

    @staticmethod
    def default_legend():
        return SortFields.DEFAULT

    def get_value(self):
        return self.value
