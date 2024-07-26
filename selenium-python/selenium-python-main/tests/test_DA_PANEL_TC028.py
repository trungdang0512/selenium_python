import allure
from ddt import ddt, data, unpack

from src.page.choose_panels_page import ChoosePanelsPage
from src.page.create_new_page_dialog import CreateNewPageDialog
from src.page.create_new_panel_dialog import CreateNewPanelDialog
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.page.panels_page import PanelsPage
from tests.test_base import TestBase


@ddt
class test_DA_PANEL_TC028(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    choose_panels_page = ChoosePanelsPage()
    create_new_page = CreateNewPageDialog()
    new_panel_dialog = CreateNewPanelDialog()
    panel_page = PanelsPage()

    @allure.title("Verify that when 'Add New Panel' form is on focused all other control/form is disabled or locked.")
    @data(("administrator", ""))
    @unpack
    def test_DA_PANEL_TC028(self, user_name, password):
        self.login_page.login(user_name, password)
        self.dashboard_page.open_panels_page()
        self.panel_page.open_add_new_panel_dialog()
        self.assertTrue(self.panel_page.is_user_menu_disabled())
