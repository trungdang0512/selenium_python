import allure
from ddt import ddt, data, unpack

from src.model import page
from src.page.create_new_page_dialog import CreateNewPageDialog
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.until.string_helper import StringHelper
from tests.test_base import TestBase


@ddt
class test_DA_MP(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    create_new_page = CreateNewPageDialog()

    page1 = page.Page('Page1_' + StringHelper.generate_name())
    page2 = page.Page('Page2_' + StringHelper.generate_name(), None, None, page1, None)

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
        self.dashboard_page.accept_alert()
        self.dashboard_page.delete_selected_page(page1)
        self.dashboard_page.accept_alert()

    parent_page = page.Page('Parent_Page_' + StringHelper.generate_name())
    child_page = page.Page('Child_Page_' + StringHelper.generate_name(), parent_page)

    @allure.title("Verify that user can remove any main parent page except 'Overview' page successfully and the order of pages stays persistent as long as there is not children page under it")
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

        self.dashboard_page.click_on_delete_link(child_page)
        self.assertEqual(self.dashboard_page.get_alert_text(), "Are you sure you want to remove this page?")
        self.dashboard_page.accept_alert()
        self.assertFalse(self.dashboard_page.check_the_page_deleted(child_page))
        self.dashboard_page.click_on_delete_link(parent_page)
        self.assertEqual(self.dashboard_page.get_alert_text(), "Are you sure you want to remove this page?")
        self.dashboard_page.accept_alert()
        self.assertFalse(self.dashboard_page.check_the_page_deleted(parent_page))


    overview_page = page.Page("Overview")
    parent_pageTC020 = page.Page('Parent_Page_' + StringHelper.generate_name(), overview_page)
    child_pageTC020 = page.Page('Child_Page_' + StringHelper.generate_name(), parent_pageTC020)

    @allure.title("Verify that user is able to delete sibbling page as long as that page has not children page under it")
    @data(("administrator", "", parent_pageTC020, child_pageTC020))
    @unpack
    def test_DA_MP_TC020(self, user_name, password, parent_pageTC020, child_pageTC020):
        self.login_page.login(user_name, password)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(parent_pageTC020)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(child_pageTC020)

        self.dashboard_page.open_page(parent_pageTC020)
        self.dashboard_page.select_global_setting_menu("Delete")
        self.dashboard_page.accept_alert()
        self.assertEqual(self.dashboard_page.get_alert_text(), "Cannot delete page '" + parent_pageTC020.name + "' since it has child page(s).\n")
        self.dashboard_page.accept_alert()

        self.dashboard_page.click_on_delete_link(child_pageTC020)
        self.dashboard_page.accept_alert()
        self.assertFalse(self.dashboard_page.check_the_page_deleted(child_pageTC020))

        self.dashboard_page.delete_selected_page(parent_pageTC020)

    new_page_name = 'Parent_Page_New_Name' + StringHelper.generate_name()

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
        self.dashboard_page.delete_selected_page(parent_page)

    @allure.title("Verify that 'Bread Crums' navigation is correct")
    @data(("administrator", "", parent_page, child_page))
    @unpack
    def test_DA_MP_TC024(self, user_name, password, parent_page, child_page):
        self.login_page.login(user_name, password)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(parent_page)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(child_page)

        self.dashboard_page.open_page(parent_page)
        self.assertEqual(self.dashboard_page.get_page_tilte(), parent_page.name)
        self.dashboard_page.open_page(child_page)
        self.assertEqual(self.dashboard_page.get_page_tilte(), child_page.name)

        self.dashboard_page.delete_selected_page(child_page)
        self.dashboard_page.delete_selected_page(parent_page)
