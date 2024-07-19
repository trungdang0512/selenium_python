from dataclasses import dataclass


@dataclass
class Page:
    def __init__(self, name, parent =None, number_of_columns=None, display_after=None, public=None):
        self._name = name
        self._parent = parent
        self._number_of_columns = number_of_columns
        self._display_after = display_after
        self._public = public

    def get_name(self):
        return self._name

    def get_parent(self):
        return self._parent

    def get_number_of_columns(self):
        return self._number_of_columns

    def get_display_after(self):
        return self._display_after

    def get_public(self):
        return self._public

    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    def set_parent(self, value):
        if not isinstance(value, str):
            raise ValueError("Parent must be a string")
        self._parent = value

    def set_number_of_columns(self, value):
        if not isinstance(value, int):
            raise ValueError("Number of Column must be a number")
        self._number_of_columns = value

    def set_display_after(self, value):
        if not isinstance(value, str):
            raise ValueError("Display after must be a string")
        self._display_after = value

    def set_public(self, value):
        if not isinstance(value, bool):
            raise ValueError("Public after must be a boolean")
        self._public = value

    def info(self):
        print(f"Page: {self._name}, {self._parent}, {self._number_of_columns}, {self._display_after}, {self._public}")

    @property
    def public(self):
        return self._public

    @property
    def display_after(self):
        return self._display_after

    @property
    def number_of_columns(self):
        return self._number_of_columns

    @property
    def parent(self):
        return self._parent

    @property
    def name(self):
        return self._name