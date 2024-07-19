import allure
from ddt import ddt, data, unpack

from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage

from tests.test_base import TestBase

@ddt
class test_DA_LOGIN_TC0010(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()

    @allure.title("Verify that the page works correctly for the case when no input entered to Password and Username field")
    def test_DA_LOGIN_TC002(self):
        self.login_page.click_login_button()
        self.assertEqual(self.login_page.get_alert_text(), "Please enter username")
