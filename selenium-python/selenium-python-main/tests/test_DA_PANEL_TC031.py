import allure
from ddt import ddt, data, unpack

from src.enum.panel_enum.panel_type import PanelType
from src.page.choose_panels_page import ChoosePanelsPage
from src.page.create_new_page_dialog import CreateNewPageDialog
from src.page.create_new_panel_dialog import CreateNewPanelDialog
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.page.panels_page import PanelsPage
from tests.test_base import TestBase
from src.until.soft_assert import SoftAssert


@ddt
class test_DA_PANEL_TC031(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    choose_panels_page = ChoosePanelsPage()
    create_new_page = CreateNewPageDialog()
    new_panel_dialog = CreateNewPanelDialog()
    panel_page = PanelsPage()

    @allure.title("Verify that correct panel setting form is displayed with corresponding panel type selected")
    @data(("administrator", ""))
    @unpack
    def test_DA_PANEL_TC031(self, user_name, password):
        self.login_page.login(user_name, password)
        self.dashboard_page.open_panels_page()
        self.panel_page.open_add_new_panel_dialog()

        SoftAssert.soft_assert(self.assertEqual(self.new_panel_dialog.get_panel_setting_form_title(), "Chart Settings",
                                                "Panel setting form is not displayed 'Chart Setting'"))
        SoftAssert.soft_assert(
            self.assertTrue(self.new_panel_dialog.is_panel_setting_form_displayed_under_display_name_field(),
                            "Chart panel setting form is not displayed under Display Name field"))

        self.new_panel_dialog.select_panel_type(PanelType.INDICATORS)
        SoftAssert.soft_assert(
            self.assertEqual(self.new_panel_dialog.get_panel_setting_form_title(), "Indicator Settings",
                             "Panel setting form is not displayed 'Indicator Setting'"))

        self.new_panel_dialog.select_panel_type(PanelType.HEAT_MAPS)
        SoftAssert.soft_assert(
            self.assertEqual(self.new_panel_dialog.get_panel_setting_form_title(), "Heat Map Settings",
                             "Panel setting form is not displayed 'Heat Map Setting'"))

        SoftAssert.assert_all()
