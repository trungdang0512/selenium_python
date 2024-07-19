from abc import abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver


class Driver:
    def __init__(self, options):
        self._config = None
        self._driver = None
        self._options = options

    def get_options(self):
        if self._config.headless:
            self._options.add_argument("--headless")
        return self._options

    @abstractmethod
    def create(self, config):
        pass

    def get_webdriver(self) -> WebDriver:
        return self._driver

    def navigate(self, url):
        self.get_webdriver().get(url)

    def quit(self):
        self.get_webdriver().quit()
