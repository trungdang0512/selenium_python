from enum import Enum


class DriverType(Enum):
    CHROME = 1
    FIREFOX = 2
    EDGE = 3


class SeleniumConfig:
    def __init__(self, browser=DriverType.CHROME, url=None, headless=False):
        self.headless = headless
        self.remote_url = None
        self.browser = browser
        self.url = url

    @staticmethod
    def chrome_config():
        config = SeleniumConfig()
        return config
