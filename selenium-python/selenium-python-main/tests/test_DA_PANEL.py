import allure
from ddt import ddt, data, unpack

from src.constants.constants import Constants
from src.enum.panel_enum.panel_type import PanelType
from src.enum.panel_enum.series_options import SeriesOptions
from src.model.page import Page
from src.model.panel.chart_settings import ChartSettings
from src.model.panel.panel import Panel
from src.page.choose_panels_page import ChoosePanelsPage
from src.page.create_new_page_dialog import CreateNewPageDialog
from src.page.create_new_panel_dialog import CreateNewPanelDialog
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.until.json_data_loader import JSONData_Loader
from src.until.list_until import ListUtils
from src.until.string_helper import StringHelper
from tests.test_base import TestBase


@ddt
class test_DA_PANEL(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    choose_panels_page = ChoosePanelsPage()
    create_new_page = CreateNewPageDialog()
    new_panel_dialog = CreateNewPanelDialog()

    new_page = Page('Page_' + StringHelper.generate_name())
    new_chart_setting = ChartSettings(
        # display_name='Panel_' + StringHelper.generate_name(),
        display_name='Panel_OdRqDAfzoV',
        series=SeriesOptions.select_random_series()
    )
    new_panel = Panel(
        new_chart_setting
    )

    expectedChartList = JSONData_Loader.get_data_list_from_json(Constants.PRESET_PANELS, "chart")
    expectedIndicatorList = JSONData_Loader.get_data_list_from_json(Constants.PRESET_PANELS, "indicator")
    expectedReports = JSONData_Loader.get_data_list_from_json(Constants.PRESET_PANELS, "reports")
    expectedHeatMaps = JSONData_Loader.get_data_list_from_json(Constants.PRESET_PANELS, "heat_maps")

    @allure.title(
        "Verify that the newly added main parent page is positioned at the location specified as set with 'Displayed After' field of 'New Page' form on the main page bar 'Parent Page' dropped down menu")
    @data(("administrator", "", new_page, new_panel, new_chart_setting, expectedChartList, expectedIndicatorList,
           expectedReports, expectedHeatMaps))
    @unpack
    def test_DA_MP_TC013(self, user_name, password, new_page, new_panel, new_chart_setting, expectedChartList,
                         expectedIndicatorList, expectedReports, expectedHeatMaps):
        # print(expectedChartList)
        # print(expectedIndicatorList)
        # print(expectedReports)
        # print(expectedHeatMaps)
        # print(new_page.name)
        # print(new_chart_setting.display_name)
        # print(new_chart_setting.series)
        # print(new_panel.displaySettings.display_name)

        self.login_page.login(user_name, password)
        # self.dashboard_page.select_global_setting_menu('Add Page')
        # self.create_new_page.create_new_page(new_page)
        # self.dashboard_page.select_global_setting_menu('Create Panel')
        # self.new_panel_dialog.create_new_panel(new_panel)
        self.dashboard_page.open_choose_panels_page()
        self.expectedChartList.append(self.new_panel.displaySettings.display_name)
        sorted_expected_chart_list = ListUtils.sort_string_list_ignore_case(self.expectedChartList)
        print(sorted_expected_chart_list)
        print(self.dashboard_page.choosePanelsButton.get_text())
        # print(self.choose_panels_page.get_panel_table_items('Chart'))