from enum import Enum


class Operators(Enum):
    EQUAL = "="
    LIKE = "~"
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL = ">="
    LESS_THAN = "<"
    LESS_THAN_OR_EQUAL = "<="
    NOT_EQUAL = "<>"
