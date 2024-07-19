from src.automation.config import SeleniumConfig
from src.automation.driver import driver_factory
from src.automation.driver import Driver


class Selenium:
    driver: Driver

    @staticmethod
    def navigate(selenium_config: SeleniumConfig):
        Selenium.driver = driver_factory.find(selenium_config.browser)
        Selenium.driver.create(selenium_config)
        Selenium.driver.navigate(selenium_config.url)

    @staticmethod
    def get_webdriver():
        return Selenium.driver.get_webdriver()

    @staticmethod
    def quit():
        return Selenium.driver.quit()

    @staticmethod
    def get():
        return Selenium.driver
