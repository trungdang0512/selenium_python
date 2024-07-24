import allure
from ddt import ddt, data, unpack

from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from tests.test_base import TestBase


@ddt
class test_DA_LOGIN(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()

    @allure.title("Verify that user can login specific repository successfully via Dashboard login page with correct credentials")
    @data(("administrator", ""))
    @unpack
    def test_DA_LOGIN_TC001(self, user_name, password):
        self.login_page.login(user_name, password)
        assert self.dashboard_page.is_displayed()

    @data(("abc", "abc"))
    @unpack
    @allure.title("Verify that user fails to login specific repository successfully via Dashboard login page with incorrect credentials")
    def test_DA_LOGIN_TC002(self, user_name, password):
        self.login_page.login(user_name, password)
        self.assertEqual(self.login_page.get_alert_text(), "Username or password is invalid")
        self.login_page.accept_alert()

    @allure.title("Verify that the page works correctly for the case when no input entered to Password and Username field")
    def test_DA_LOGIN_TC003(self):
        self.login_page.click_login_button()
        self.assertEqual(self.login_page.get_alert_text(), "Please enter username")