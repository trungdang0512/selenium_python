from abc import abstractmethod

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver:
    def __init__(self, options):
        self._config = None
        self._driver = None
        self._options = options

    def get_options(self):
        if self._config.headless:
            self._options.add_argument("--disable-notifications")
            self._options.add_argument("--disable-infobars")
            self._options.add_argument("--disable-extensions")
            self._options.add_argument("--start-maximized")
            self._options.add_argument("--incognito")
            self._options.add_argument("--disable-popup-blocking")
            self._options.add_argument("--disable-features=EnableEphemeralFlashPermission")
            self._options.add_argument("--disable-features=InfiniteSessionRestore")
            self._options.add_experimental_option("excludeSwitches", ["enable-automation"])
            self._options.add_experimental_option('useAutomationExtension', False)
            self._options.add_argument("--headless")
        return self._options

    @abstractmethod
    def create(self, config):
        pass

    def get_webdriver(self) -> WebDriver:
        return self._driver

    def navigate(self, url):
        self.get_webdriver().get(url)

    def maximize(self):
        self.get_webdriver().maximize_window()

    def close_notification(self):
        try:
            close_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close']"))
            )
            close_button.click()
            print("Notification closed.")
        except TimeoutException:
            print("No notification found to close.")

    def quit(self):
        self.get_webdriver().quit()
