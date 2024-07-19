from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions, EdgeOptions

from src.automation.driver import Driver
from src.automation.config import DriverType


class ChromeDriver(Driver):
    def create(self, config):
        self._config = config
        self._driver = webdriver.Chrome(self.get_options())

    def __init__(self):
        super().__init__(ChromeOptions())


class FirefoxDriver(Driver):
    def create(self, config):
        self._config = config
        self._driver = webdriver.Firefox(self.get_options())

    def __init__(self):
        super().__init__(FirefoxOptions())


class EdgeDriver(Driver):
    def create(self, config):
        self._config = config
        self._driver = webdriver.Edge(self.get_options())

    def __init__(self):
        super().__init__(EdgeOptions())


browsers = {
    DriverType.CHROME: ChromeDriver,
    DriverType.FIREFOX: FirefoxDriver,
    DriverType.EDGE: EdgeDriver
}


def find(driver_type: DriverType):
    instance = browsers.get(driver_type)
    if instance is None:
        raise Exception("Cannot find the factory for '%s'" % driver_type)
    else:
        return instance()
