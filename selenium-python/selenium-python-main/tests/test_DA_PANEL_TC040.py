import allure
import softest
from ddt import ddt, data, unpack

from src.constants.constants import Constants
from src.enum.panel_enum.chart_type_option import ChartTypeOptions
from src.enum.panel_enum.data_label_checkboxes import DataLabelsCheckBoxes
from src.model.page import Page
from src.page.choose_panels_page import ChoosePanelsPage
from src.page.create_new_page_dialog import CreateNewPageDialog
from src.page.create_new_panel_dialog import CreateNewPanelDialog
from src.page.dashboard_page import DashboardPage
from src.page.data_profile_page import DataProfilePage
from src.page.login_page import LoginPage
from src.page.panels_page import PanelsPage
from src.until.string_helper import StringHelper
from tests.test_base import TestBase
from src.until.soft_assert import SoftAssert


@ddt
class test_DA_PANEL_TC040(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    choose_panels_page = ChoosePanelsPage()
    create_new_page = CreateNewPageDialog()
    new_panel_dialog = CreateNewPanelDialog()
    panel_page = PanelsPage()
    data_profile_page = DataProfilePage()

    new_page = Page('Page_' + StringHelper.generate_name())

    @allure.title(
        "Verify that all 'Data Labels' check boxes are enabled and disabled correctly corresponding to each type of 'Chart Type'")
    @data(("administrator", "", new_page))
    @unpack
    def test_DA_PANEL_TC040(self, user_name, password, new_page):
        self.login_page.login(user_name, password)
        self.dashboard_page.select_global_setting_menu('Add Page')
        self.create_new_page.create_new_page(new_page)
        self.dashboard_page.open_choose_panels_page()
        self.choose_panels_page.click_on_create_new_panel_button()

        self.new_panel_dialog.select_chart_type_selection(ChartTypeOptions.PIE)
        SoftAssert.soft_assert(
            self.assertTrue(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.CATEGORIES),
                            "VP01.1: Categories checkbox is not disabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.SERIES),
                             "VP01.2: Series checkbox is not enabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.VALUE),
                             "VP01.3: Value checkbox is not enabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.PERCENTAGE),
                             "VP01.4: Percentage checkbox is not enabled"))

        self.new_panel_dialog.select_chart_type_selection(ChartTypeOptions.SINGLE_BAR)
        SoftAssert.soft_assert(
            self.assertTrue(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.CATEGORIES),
                            "VP02.1: Categories checkbox is not disabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.SERIES),
                             "VP02.2: Series checkbox is not enabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.VALUE),
                             "VP02.3: Value checkbox is not enabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.PERCENTAGE),
                             "VP02.4: Percentage checkbox is not enabled"))

        self.new_panel_dialog.select_chart_type_selection(ChartTypeOptions.STACKED_BAR)
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.CATEGORIES),
                             "VP03.1: Categories checkbox is not enabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.SERIES),
                             "VP03.2: Series checkbox is not enabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.VALUE),
                             "VP03.3: Value checkbox is not enabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.PERCENTAGE),
                             "VP03.4: Percentage checkbox is not enabled"))

        self.new_panel_dialog.select_chart_type_selection(ChartTypeOptions.GROUP_BAR)
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.CATEGORIES),
                             "VP04.1: Categories checkbox is not enabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.SERIES),
                             "VP04.2: Series checkbox is not enabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.VALUE),
                             "VP04.3: Value checkbox is not enabled"))
        SoftAssert.soft_assert(
            self.assertFalse(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.PERCENTAGE),
                             "VP04.4: Percentage checkbox is not enabled"))

        self.new_panel_dialog.select_chart_type_selection(ChartTypeOptions.LINE)
        SoftAssert.soft_assert(
            self.assertTrue(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.CATEGORIES),
                            "VP05.1: Categories checkbox is not disabled"))
        SoftAssert.soft_assert(
            self.assertTrue(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.SERIES),
                            "VP05.2: Series checkbox is not disabled"))
        SoftAssert.soft_assert(
            self.assertTrue(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.VALUE),
                            "VP05.3: Value checkbox is not disabled"))
        SoftAssert.soft_assert(
            self.assertTrue(self.new_panel_dialog.is_data_label_is_disabled(DataLabelsCheckBoxes.PERCENTAGE),
                            "VP05.4: Percentage checkbox is not disabled"))

        SoftAssert.assert_all()
