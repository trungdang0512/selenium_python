import allure
from ddt import ddt, data, unpack

from src.model import page
from src.page.create_new_page_panel import CreateNewPagePanel
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.until.StringHelper import StringHelper
from tests.test_base import TestBase


@ddt
class test_DA_MP_TC017(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    create_new_page = CreateNewPagePanel()

    parent_page_name = 'Parent_Page_' + StringHelper.generate_name()
    child_page_name = 'Child_Page_' + StringHelper.generate_name()

    parent_page = page.Page(parent_page_name)
    child_page = page.Page(child_page_name, parent_page, None, None, None)

    @allure.title("Verify that the newly added main parent page is positioned at the location specified as set with 'Displayed After' field of 'New Page' form on the main page bar 'Parent Page' dropped down menu")
    @data(("administrator", "", parent_page, child_page))
    @unpack
    def test_DA_MP_TC017(self, user_name, password, parent_page, child_page):
        self.login_page.login(user_name, password)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(parent_page)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(child_page)

        self.dashboard_page.open_page(parent_page)
        self.dashboard_page.select_global_setting_menu("Delete")
        self.assertEqual(self.dashboard_page.get_alert_text(), "Are you sure you want to remove this page?")
        self.dashboard_page.accept_alert()
        self.assertEqual(self.dashboard_page.get_alert_text(), "Cannot delete page '" + parent_page.name + "' since it has child page(s).\n")
        self.dashboard_page.accept_alert()

        self.dashboard_page.delete_selected_page(child_page)
        self.assertEqual(self.dashboard_page.get_alert_text(), "Are you sure you want to remove this page?")
        self.dashboard_page.accept_alert()
        self.assertFalse(self.dashboard_page.check_the_page_deleted(child_page))
        self.dashboard_page.delete_selected_page(parent_page)
        self.assertEqual(self.dashboard_page.get_alert_text(), "Are you sure you want to remove this page?")
        self.dashboard_page.accept_alert()
        self.assertFalse(self.dashboard_page.check_the_page_deleted(parent_page))
