import allure
from ddt import ddt, data, unpack

from src.model import page
from src.page.create_new_page_panel import CreateNewPagePanel
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.until.StringHelper import StringHelper

from tests.test_base import TestBase

@ddt
class test_DA_MP_TC013(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    create_new_page = CreateNewPagePanel()

    page_name1 = 'Page1_' + StringHelper.generate_name()
    page_name2 = 'Page2_' + StringHelper.generate_name()

    page1 = page.Page(page_name1)
    page2 = page.Page(page_name2, None, None, page1._name, None)

    @allure.title("Verify that the newly added main parent page is positioned at the location specified as set with 'Displayed After' field of 'New Page' form on the main page bar 'Parent Page' dropped down menu")
    @data(("administrator", "", page1, page2))
    @unpack
    def test_DA_MP_TC013(self, user_name, password, page1, page2):
        self.login_page.login(user_name, password)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(page1)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(page2)
        assert self.dashboard_page.check_page_after(page1, page2)
        self.dashboard_page.delete_selected_page(page2)
        self.dashboard_page.delete_selected_page(page1)
