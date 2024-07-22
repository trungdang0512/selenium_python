from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition

from src.automation import Selenium


def _waiter():
    return WebDriverWait(Selenium.driver.get_webdriver(), 5)


def _driver():
    return Selenium.driver.get_webdriver()


class Element:
    def __init__(self, by: By, value):
        self._by = by
        self._value = value

    @staticmethod
    def id(value):
        return Element(By.ID, value)

    @staticmethod
    def class_name(value):
        return Element(By.CLASS_NAME, value)

    @staticmethod
    def name(value):
        return Element(By.NAME, value)

    @staticmethod
    def xpath(value):
        return Element(By.XPATH, value)

    def find_visible(self) -> WebElement:
        return _waiter().until(condition.visibility_of_element_located(
            (str(self._by), self._value)))

    def find(self) -> WebElement:
        return _waiter().until(condition.presence_of_element_located(
            (str(self._by), self._value)))

    def enter(self, value):
        self.find_visible().send_keys(value)

    def click(self):
        self.find_visible().click()

    def hover(self):
        hover = ActionChains(_driver()).move_to_element(self.find_visible())
        hover.perform()

    def get_text(self):
        self.find().__getattribute__('innerText')

    def is_displayed(self):
        try:
            return self.find().is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def select_by_text(self, text):
        select = Select(self.find())
        select.select_by_visible_text(text)

    def select_by_index(self, index):
        select = Select(self.find_visible())
        select.select_by_index(index)

    def select_by_value(self, value):
        select = Select(self.find_visible())
        select.select_by_value(value)