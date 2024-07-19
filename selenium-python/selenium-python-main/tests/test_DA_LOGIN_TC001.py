import allure
from ddt import ddt, data, file_data, idata, unpack

from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage

from tests.test_base import TestBase

@ddt
class test_DA_LOGIN_TC001(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()

    @allure.title("Verify that user can login specific repository successfully via Dashboard login page with correct credentials")
    @data(("administrator", ""))
    @unpack
    def test_DA_LOGIN_TC001(self, user_name, password):
        self.login_page.login(user_name, password)
        assert self.dashboard_page.is_displayed()

