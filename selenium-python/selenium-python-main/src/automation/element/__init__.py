from typing import List

from selenium.common import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.support import expected_conditions as EC


from src.automation import Selenium


def _waiter():
    return WebDriverWait(Selenium.driver.get_webdriver(), 20)


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

    def find_all(self) -> List[WebElement]:
        return _waiter().until(EC.presence_of_all_elements_located(
            (self._by, self._value)))

    def enter(self, value):
        self.find_visible().send_keys(value)

    def clear(self):
        self.find_visible().clear()

    def click(self):
        self.find_visible().click()

    def hover(self):
        hover = ActionChains(_driver()).move_to_element(self.find_visible())
        hover.perform()

    def get_text(self) -> str:
        element = self.find_visible()
        if element:
            print(f"Found element: {element}")  # In ra đối tượng WebElement
            print(f"Element text: {element.text}")  # In ra văn bản của phần tử
            return element.text
        else:
            print("Element not found")
            return ""

    def get_all_texts(self) -> List[str]:
        elements = self.find_all()
        return [elem.text for elem in elements]

    def is_displayed(self):
        try:
            return self.find().is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    def location(self):
        element = self.find()
        return element.location

    def size(self):
        element = self.find()
        return element.size

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def select_by_text(self, text):
        select = Select(self.find())
        for option in select.options:
            if text in option.text:
                select.select_by_visible_text(option.text)
                break

    def select_by_index(self, index):
        select = Select(self.find_visible())
        select.select_by_index(index)

    def select_by_value(self, value):
        select = Select(self.find_visible())
        select.select_by_value(value)

    def has_option_with_text(self, text: str) -> bool:
        select_element = self.find()
        options = select_element.find_elements(By.TAG_NAME, "option")
        for option in options:
            if text in option.text:
                return True
        return False

    def scroll_to(self):
        element = self.find()
        _driver().execute_script("arguments[0].scrollIntoView(true);", element)

    def is_disabled(self) -> bool:
        try:
            element = self.find_visible()
            return not element.is_enabled() or element.get_attribute("disabled") is not None or element.get_attribute("aria-disabled") == "true"
        except (NoSuchElementException, TimeoutException):
            return True

    def no_effect_on_click(self) -> bool:
        try:
            element = self.find()
            before_click = element.get_attribute("outerHTML")
            element.click()
            after_click = element.get_attribute("outerHTML")
            return before_click == after_click
        except ElementClickInterceptedException:
            return True
        except (NoSuchElementException, TimeoutException):
            return False

