import unittest

import pytest

from src.automation import Selenium


class TestBase(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def before_test(self, input_config):
        Selenium.navigate(input_config)
        yield Selenium
        Selenium.quit()
