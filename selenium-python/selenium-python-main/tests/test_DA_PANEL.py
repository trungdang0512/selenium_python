import allure
from ddt import ddt, data, unpack

from src.constants.constants import Constants
from src.enum.panel_enum.chart_type_option import ChartTypeOptions
from src.enum.panel_enum.data_label_checkboxes import DataLabelsCheckBoxes
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
class test_DA_PANEL(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    choose_panels_page = ChoosePanelsPage()
    create_new_page = CreateNewPageDialog()
    new_panel_dialog = CreateNewPanelDialog()
    panel_page = PanelsPage()
    data_profile_page = DataProfilePage()

    def setUp(self):
        SoftAssert.reset()

#DA_MP_TC027
#     new_page027 = Page('Page_' + StringHelper.generate_name())
#     new_chart_setting027 = ChartSettings(
#         display_name='Panel_' + StringHelper.generate_name(),
#         series=SeriesOptions.select_random_series()
#     )
#     new_panel027 = Panel(
#         new_chart_setting027
#     )
#
#     expectedChartList = JSONData_Loader.get_data_list_from_json(Constants.PRESET_PANELS, "chart")
#     expectedIndicatorList = JSONData_Loader.get_data_list_from_json(Constants.PRESET_PANELS, "indicator")
#     expectedReports = JSONData_Loader.get_data_list_from_json(Constants.PRESET_PANELS, "reports")
#     expectedHeatMaps = JSONData_Loader.get_data_list_from_json(Constants.PRESET_PANELS, "heat_maps")
#
#     @allure.title(
#         "Verify that the newly added main parent page is positioned at the location specified as set with 'Displayed After' field of 'New Page' form on the main page bar 'Parent Page' dropped down menu")
#     @data(("administrator", "", new_page027, new_panel027, expectedChartList, expectedIndicatorList,
#            expectedReports, expectedHeatMaps))
#     @unpack
#     def test_DA_MP_TC027(self, user_name, password, new_page, new_panel, expectedChartList,
#                          expectedIndicatorList, expectedReports, expectedHeatMaps):
#         self.login_page.login(user_name, password)
#         self.dashboard_page.select_global_setting_menu('Add Page')
#         self.create_new_page.create_new_page(new_page)
#         self.dashboard_page.select_global_setting_menu('Create Panel')
#         self.new_panel_dialog.create_new_panel(new_panel)
#         self.dashboard_page.open_choose_panels_page()
#
#         expectedChartList.append(self.new_panel027.displaySettings.display_name)
#         sorted_expected_chart_list = ListUtils.sort_string_list_ignore_case(self.expectedChartList)
#
#         SoftAssert.soft_assert(self.assertEqual,sorted_expected_chart_list,
#                                                         self.choose_panels_page.get_panel_table_items(PanelType.CHARTS),
#                                                         "chart_list fail")
#         SoftAssert.soft_assert(self.assertEqual,expectedIndicatorList,
#                                                         self.choose_panels_page.get_panel_table_items(
#                                                             PanelType.INDICATORS), "chart_list fail")
#         SoftAssert.soft_assert(self.assertEqual,expectedReports,
#                                                         self.choose_panels_page.get_panel_table_items(PanelType.REPORTS),
#                                              "chart_list fail")
#         SoftAssert.soft_assert(self.assertEqual,expectedHeatMaps,
#                                                         self.choose_panels_page.get_panel_table_items(PanelType.HEAT_MAPS),
#                                                 "chart_list fail")
#
#         try:
#             SoftAssert.assert_all()
#         finally:
#             self.choose_panels_page.log_out()
#
# # #DA_MP_TC028
#     @allure.title("Verify that when 'Add New Panel' form is on focused all other control/form is disabled or locked.")
#     @data(("administrator", ""))
#     @unpack
#     def test_DA_PANEL_TC028(self, user_name, password):
#         self.login_page.login(user_name, password)
#         self.dashboard_page.open_panels_page()
#         self.panel_page.open_add_new_panel_dialog()
#         self.assertTrue(self.panel_page.is_menu_locked())
#
# #DA_MP_TC031
#     @allure.title("Verify that correct panel setting form is displayed with corresponding panel type selected")
#     @data(("administrator", ""))
#     @unpack
#     def test_DA_PANEL_TC031(self, user_name, password):
#         self.login_page.login(user_name, password)
#         self.dashboard_page.open_panels_page()
#         self.panel_page.open_add_new_panel_dialog()
#
#         SoftAssert.soft_assert,self.assertEqual(self.new_panel_dialog.get_panel_setting_form_title(), "Chart Settings",
#                                                 "Panel setting form is not displayed 'Chart Setting'")
#         SoftAssert.soft_assert(
#             self.assertTrue,self.new_panel_dialog.is_panel_setting_form_displayed_under_display_name_field(),
#                             "Chart panel setting form is not displayed under Display Name field")
#
#         self.new_panel_dialog.select_panel_type(PanelType.INDICATORS)
#         SoftAssert.soft_assert(
#             self.assertEqual,self.new_panel_dialog.get_panel_setting_form_title(), "Indicator Settings",
#                              "Panel setting form is not displayed 'Indicator Setting'")
#
#         self.new_panel_dialog.select_panel_type(PanelType.HEAT_MAPS)
#         SoftAssert.soft_assert(
#             self.assertEqual,self.new_panel_dialog.get_panel_setting_form_title(), "Heat Map Settings",
#                              "Panel setting form is not displayed 'Heat Map Setting'")
#
#         try:
#             SoftAssert.assert_all()
#         finally:
#             self.new_panel_dialog.click_on_cancel_button()
#             self.choose_panels_page.log_out()
#
# # #DA_MP_TC034
#     new_data_profile34 = DataProfile(dataProfileName='Data_Profile_' + StringHelper.generate_name())
#     new_chart_setting34 = ChartSettings(
#         display_name='Panel_' + StringHelper.generate_name(),
#         series=SeriesOptions.select_random_series()
#     )
#     new_panel34 = Panel(
#         new_chart_setting34
#     )
#
#     @allure.title(
#         "Verify that the newly added main parent page is positioned at the location specified as set with 'Displayed After' field of 'New Page' form on the main page bar 'Parent Page' dropped down menu")
#     @data(("administrator", "", new_data_profile34, new_panel34))
#     @unpack
#     def test_DA_PANEL_TC034(self, user_name, password, new_data_profile, new_panel):
#         self.login_page.login(user_name, password)
#         self.dashboard_page.open_data_profile_page()
#         self.data_profile_page.click_on_add_new_link()
#         self.data_profile_page.create_new_data_profile(new_data_profile)
#
#         self.data_profile_page.open_panels_page()
#         self.panel_page.open_add_new_panel_dialog()
#         SoftAssert.soft_assert(self.assertTrue,
#             self.new_panel_dialog.is_data_profile_populated_under_the_drop_down_menu(self.new_data_profile34),
#             "Data profiles are not populated correctly")
#
#         self.new_panel_dialog.create_new_panel(new_panel)
#         self.panel_page.open_edit_panel_dialog(new_panel)
#         SoftAssert.soft_assert(self.assertTrue,
#             self.new_panel_dialog.is_data_profile_populated_under_the_drop_down_menu(self.new_data_profile34),
#             "Data profiles are not populated correctly")
#         self.new_panel_dialog.click_on_cancel_button()
#
#         try:
#             SoftAssert.assert_all()
#         finally:
#             self.panel_page.log_out()

#DA_PANEL_TC040
    new_page40 = Page('Page_' + StringHelper.generate_name())

    @allure.title(
        "Verify that all 'Data Labels' check boxes are enabled and disabled correctly corresponding to each type of 'Chart Type'")
    @data(("administrator", "", new_page40))
    @unpack
    def test_DA_PANEL_TC040(self, user_name, password, new_page):
        self.login_page.login(user_name, password)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(new_page)
        self.dashboard_page.open_choose_panels_page()
        self.choose_panels_page.click_on_create_new_panel_button()

        self.new_panel_dialog.select_chart_type_selection(ChartTypeOptions.PIE)
        SoftAssert.soft_assert(
            self.assertTrue,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.CATEGORIES),
                            "VP01.1: Categories checkbox is not disabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.SERIES),
                             "VP01.2: Series checkbox is not enabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.VALUE),
                             "VP01.3: Value checkbox is not enabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.PERCENTAGE),
                             "VP01.4: Percentage checkbox is not enabled")

        self.new_panel_dialog.select_chart_type_selection(ChartTypeOptions.SINGLE_BAR)
        SoftAssert.soft_assert(
            self.assertTrue,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.CATEGORIES),
                            "VP02.1: Categories checkbox is not disabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.SERIES),
                             "VP02.2: Series checkbox is not enabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.VALUE),
                             "VP02.3: Value checkbox is not enabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.PERCENTAGE),
                             "VP02.4: Percentage checkbox is not enabled")

        self.new_panel_dialog.select_chart_type_selection(ChartTypeOptions.STACKED_BAR)
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.CATEGORIES),
                             "VP03.1: Categories checkbox is not enabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.SERIES),
                             "VP03.2: Series checkbox is not enabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.VALUE),
                             "VP03.3: Value checkbox is not enabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.PERCENTAGE),
                             "VP03.4: Percentage checkbox is not enabled")

        self.new_panel_dialog.select_chart_type_selection(ChartTypeOptions.GROUP_BAR)
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.CATEGORIES),
                             "VP04.1: Categories checkbox is not enabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.SERIES),
                             "VP04.2: Series checkbox is not enabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.VALUE),
                             "VP04.3: Value checkbox is not enabled")
        SoftAssert.soft_assert(
            self.assertFalse,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.PERCENTAGE),
                             "VP04.4: Percentage checkbox is not enabled")

        self.new_panel_dialog.select_chart_type_selection(ChartTypeOptions.LINE)
        SoftAssert.soft_assert(
            self.assertTrue,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.CATEGORIES),
                            "VP05.1: Categories checkbox is not disabled")
        SoftAssert.soft_assert(
            self.assertTrue,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.SERIES),
                            "VP05.2: Series checkbox is not disabled")
        SoftAssert.soft_assert(
            self.assertTrue,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.VALUE),
                            "VP05.3: Value checkbox is not disabled")
        SoftAssert.soft_assert(
            self.assertTrue,self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.PERCENTAGE),
                            "VP05.4: Percentage checkbox is not disabled")

        try:
            SoftAssert.assert_all()
        finally:
            self.new_panel_dialog.click_on_cancel_button()
            self.choose_panels_page.log_out()
