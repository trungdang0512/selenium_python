from enum import Enum

class Field(Enum):
    ASSIGNED_USER = "assigned"
    STATUS = "status"
    UPDATED_BY = "updated by"
    CREATED_BY = "created by"
    NAME = "name"
    LOCATION = "location"
    DESCRIPTION = "description"
    REVISION_TIMESTAMP = "revision timestamp"
    UPDATE_DATE = "update date"
    CREATION_DATE = "creation date"
    NOTES = "notes"
    CHECK_OUT_USER = "check out user"
    URL = "url"

    def value(self):
        return self.value