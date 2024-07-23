import allure
from ddt import ddt, data, unpack

from src.model import page
from src.page.create_new_page_panel import CreateNewPagePanel
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.until.StringHelper import StringHelper
from tests.test_base import TestBase


@ddt
class test_DA_MP_TC023(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    create_new_page = CreateNewPagePanel()

    parent_page_name = 'Parent_Page_' + StringHelper.generate_name()
    child_page_name = 'Child_Page_' + StringHelper.generate_name()
    new_page_name = 'Parent_Page_New_Name' + StringHelper.generate_name()

    parent_page = page.Page(parent_page_name)
    child_page = page.Page(child_page_name, parent_page)

    @allure.title("Verify that user is able to edit the parent page of the sibbling page successfully")
    @data(("administrator", "", parent_page, child_page, new_page_name))
    @unpack
    def test_DA_MP_TC023(self, user_name, password, parent_page, child_page, new_page_name):
        self.login_page.login(user_name, password)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(parent_page)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(child_page)

        self.dashboard_page.open_page(parent_page)
        self.dashboard_page.select_global_setting_menu("Edit")
        self.create_new_page.edit_page_name(parent_page, new_page_name)

        self.assertEqual(new_page_name, parent_page.name)

        self.dashboard_page.delete_selected_page(child_page)
        self.dashboard_page.accept_alert()
        self.dashboard_page.delete_selected_page(parent_page)
        self.dashboard_page.accept_alert()

