import pytest

from src.automation.config import SeleniumConfig, DriverType


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome",
                     action="store", help="browser driver to be used for testing")
    parser.addoption("--headless", action="store_true",
                     help="driver option to run in headless mode")
    parser.addoption("--url",
                     default="http://localhost/TADashboard/login.jsp",
                     action="store", help="url of application to be used for testing")


@pytest.fixture(autouse=True)
def input_config(request):
    headless = request.config.getoption("--headless")
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    return SeleniumConfig(DriverType[str(browser_name).upper()], url, headless)
