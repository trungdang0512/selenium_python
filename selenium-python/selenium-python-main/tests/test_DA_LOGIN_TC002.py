import allure
from ddt import ddt, data, file_data, idata, unpack

from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage

from tests.test_base import TestBase

@ddt
class test_DA_LOGIN_TC002(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()

    @data(("abc", "abc"))
    @unpack
    @allure.title("Verify that user fails to login specific repository successfully via Dashboard login page with incorrect credentials")
    def test_DA_LOGIN_TC002(self, user_name, password):
        self.login_page.login(user_name, password)
        self.assertEqual(self.login_page.get_alert_text(), "Username or password is invalid")
