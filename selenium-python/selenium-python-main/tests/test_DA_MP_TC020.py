import allure
from ddt import ddt, data, unpack

from src.model import page
from src.page.create_new_page_panel import CreateNewPagePanel
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.until.StringHelper import StringHelper
from tests.test_base import TestBase


@ddt
class test_DA_MP_TC020(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    create_new_page = CreateNewPagePanel()

    parent_page_name = 'Parent_Page_' + StringHelper.generate_name()
    child_page_name = 'Child_Page_' + StringHelper.generate_name()

    overview_page = page.Page("Overview")
    parent_page = page.Page(parent_page_name, overview_page)
    child_page = page.Page(child_page_name, parent_page)

    @allure.title("Verify that user is able to delete sibbling page as long as that page has not children page under it")
    @data(("administrator", "", overview_page, parent_page, child_page))
    @unpack
    def test_DA_MP_TC020(self, user_name, password, overview_page, parent_page, child_page):
        self.login_page.login(user_name, password)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(parent_page)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(child_page)

        self.dashboard_page.open_page(parent_page)
        self.dashboard_page.select_global_setting_menu("Delete")
        self.dashboard_page.accept_alert()
        self.assertEqual(self.dashboard_page.get_alert_text(), "Cannot delete page '" + parent_page.name + "' since it has child page(s).\n")
        self.dashboard_page.accept_alert()

        self.dashboard_page.delete_selected_page(child_page)
        self.dashboard_page.accept_alert()
        self.assertFalse(self.dashboard_page.check_the_page_deleted(child_page))

        self.dashboard_page.delete_selected_page(child_page)
        self.dashboard_page.accept_alert()
        self.dashboard_page.delete_selected_page(parent_page)
        self.dashboard_page.accept_alert()