import allure
from ddt import ddt, data, unpack

from src.model import page
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.until import StringHelper

from tests.test_base import TestBase

@ddt
class test_DA_MP_TC013(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()

    page_name1 = 'Page1_' + StringHelper.StringHelper.generate_name()
    page_name2 = 'Page2_' + StringHelper.StringHelper.generate_name()

    page1 = page.Page(page_name1)
    page2 = page.Page(page_name2, None, None, page1._name, None)

    @allure.title("Verify that the newly added main parent page is positioned at the location specified as set with 'Displayed After' field of 'New Page' form on the main page bar 'Parent Page' dropped down menu")
    @data(("administrator", "", page1, page2))
    @unpack
    def test_DA_MP_TC013(self, user_name, password, page1, page2):
        self.login_page.login(user_name, password)
        # self.dashboard_page.select_global_setting_menu('Add Page')
        # self.dashboard_page.create_new_page(page1)
        # self.dashboard_page.select_global_setting_menu('Add Page')
        # self.dashboard_page.create_new_page(page2)
        self.dashboard_page.get_page_sibling("Page1_zkgzBUJCDl")