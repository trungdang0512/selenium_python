from dataclasses import dataclass


@dataclass
class Page:
    def __init__(self, name, parent =None, number_of_columns=None, display_after=None, public=None):
        self._name = name
        self._parent = parent
        self._number_of_columns = number_of_columns
        self._display_after = display_after
        self._public = public

    def info(self):
        print(f"Page: {self._name}, {self._parent}, {self._number_of_columns}, {self._display_after}, {self._public}")

    @property
    def public(self):
        return self._public

    @public.setter
    def public(self, new_value):
        self._public = new_value

    @property
    def display_after(self):
        return self._display_after

    @display_after.setter
    def display_after(self, new_page):
        self._display_after = new_page

    @property
    def number_of_columns(self):
        return self._number_of_columns

    @number_of_columns.setter
    def number_of_columns(self, new_number):
        self._number_of_columns = new_number

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name