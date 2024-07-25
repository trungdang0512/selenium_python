import allure
from ddt import ddt, data, unpack

from src.constants.constants import Constants
from src.enum.panel_enum.panel_type import PanelType
from src.enum.panel_enum.series_options import SeriesOptions
from src.model.data_profile import DataProfile
from src.model.page import Page
from src.model.panel.chart_settings import ChartSettings
from src.model.panel.panel import Panel
from src.page.choose_panels_page import ChoosePanelsPage
from src.page.create_new_page_dialog import CreateNewPageDialog
from src.page.create_new_panel_dialog import CreateNewPanelDialog
from src.page.dashboard_page import DashboardPage
from src.page.data_profile_page import DataProfilePage
from src.page.login_page import LoginPage
from src.page.panels_page import PanelsPage
from src.until.json_data_loader import JSONData_Loader
from src.until.list_until import ListUtils
from src.until.string_helper import StringHelper
from tests.test_base import TestBase
from src.until.soft_assert import SoftAssert


@ddt
class test_DA_PANEL_TC034(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    choose_panels_page = ChoosePanelsPage()
    create_new_page = CreateNewPageDialog()
    new_panel_dialog = CreateNewPanelDialog()
    panel_page = PanelsPage()
    data_profile_page = DataProfilePage()

    new_data_profile = DataProfile(dataProfileName='Data_Profile_' + StringHelper.generate_name())

    @allure.title(
        "Verify that the newly added main parent page is positioned at the location specified as set with 'Displayed After' field of 'New Page' form on the main page bar 'Parent Page' dropped down menu")
    @data(("administrator", "", new_data_profile))
    @unpack
    def test_DA_PANEL_TC034(self, user_name, password, new_data_profile):
        self.login_page.login(user_name, password)
        self.dashboard_page.open_data_profile_page()
        self.data_profile_page.click_on_add_new_link()
        self.data_profile_page.create_new_data_profile(new_data_profile)

        self.data_profile_page.open_panels_page()
        self.panel_page.open_add_new_panel_dialog()
        result = self.new_panel_dialog.is_data_profile_populated_under_the_drop_down_menu(self.new_data_profile)
        print(result)

