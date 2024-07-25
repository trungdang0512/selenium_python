import time

import allure

from src.automation.element import Element
from src.enum.panel_enum.panel_type import PanelType
from src.enum.panel_enum.series_options import SeriesOptions
from src.model.data_profile import DataProfile
from src.model.page import Page
from src.model.panel.chart_settings import ChartSettings
from src.model.panel.display_settings import DisplaySettings
from src.model.panel.panel import Panel
from src.page.base_page import BasePage


class CreateNewPanelDialog(BasePage):
    def __init__(self):
        super().__init__()
        # Create New/Edit Panel Modal
        self.dataProfileSelection = Element.xpath("//select[@id='cbbProfile']")
        self.displayNameTextBox = Element.xpath("//input[@id= 'txtDisplayName']")
        self.chartTitleTextBox = Element.xpath("//input[@id= 'txtChartTitle']")
        self.showTitleCheckBox = Element.xpath("//input[@id= 'chkShowTitle']")
        self.chartTypeSelection = Element.xpath("//select[@id= 'cbbChartType']")
        self.styleRadioButtons = Element.xpath("//td[contains(text(), 'Style')]/following-sibling::td/input[@value='{}']")
        self.categorySelection = Element.xpath("//select[@id= 'cbbCategoryField']")
        self.categoryCaptionTextBox = Element.xpath("//input[@id= 'txtCategoryXAxis']")
        self.seriesSelection = Element.xpath("//select[@id= 'cbbSeriesField']")
        self.seriesCaptionTextBox = Element.xpath("//input[@id= 'txtValueYAxis']")
        self.legendsRadioButton = Element.xpath("//input[@name= 'radPlacement' and @value= '{}']")
        self.dataLabelCheckBox = Element.xpath("//label[contains(text(),'{}')]/input[@type='checkbox']")
        self.addNewPanelOkButton = Element.xpath("//div[@class ='ui-dialog-container']//input[contains(@onclick, 'Dashboard.addPanel(')]")
        self.panelSettingForm = Element.xpath("//fieldset[@id='fdSettings']")
        self.panelSettingFormTitle = Element.xpath("//fieldset[@id='fdSettings']/legend")

        # Panel Configuration Modal
        self.panelConfigurationOkButton = Element.xpath("//div[@id='div_panelConfigurationDlg']//input[@id='OK']")
        self.heightTextBox = Element.xpath("//input[@id='txtHeight']")
        self.selectFolderButtonOnPanelConfigurationModal = Element.xpath("//a[contains(@href, 'javascript:Dashboard.treeFolder();')]")

        self.panelTypeRadioButtonsXpath = "//td[text()='Type']/following-sibling::td/label[contains(text(), '{}')]"


    def select_panel_type(self, panel_type: PanelType):
            if panel_type is not None:
                panelTypeRadioButtons = Element.xpath(self.panelTypeRadioButtonsXpath)
                panelTypeRadioButtons.value = panelTypeRadioButtons.value.replace('{}', panel_type.get_value(), 1)
                panelTypeRadioButtons.click()

    def select_data_profile(self, data_profile: str):
        if data_profile is not None:
            self.dataProfileSelection.select_by_text(data_profile)

    def fill_display_name(self, display_name: str):
        self.displayNameTextBox.enter(display_name)

    def select_series(self, series: SeriesOptions):
        if series is not None:
            self.seriesSelection.select_by_text(series.get_value())

    def click_on_OK_button_of_new_panel_dialog(self):
        self.addNewPanelOkButton.click()

    def click_on_OK_button_of_confiuration(self):
        self.panelConfigurationOkButton.click()

    def fill_display_settings(self, display_setting: DisplaySettings):
        # self.select_panel_type(display_setting.panelType)
        # self.select_data_profile(display_setting.dataProfile)
        self.fill_display_name(display_setting.display_name)

    def fill_chart_settings(self, chart_setting: ChartSettings):
        self.select_series(chart_setting.series)

    def fill_new_panel_info(self, new_panel: Panel):
        time.sleep(2)
        self.fill_display_settings(new_panel.displaySettings)
        self.fill_chart_settings(new_panel.displaySettings)

    def create_new_panel(self, new_panel: Panel):
        self.fill_new_panel_info(new_panel)
        time.sleep(2)
        self.click_on_OK_button_of_new_panel_dialog()
        self.click_on_OK_button_of_confiuration()

    def get_panel_setting_form_title(self):
        time.sleep(1)
        return self.panelSettingFormTitle.get_text()

    def is_panel_setting_form_displayed_under_display_name_field(self):
        if self.panelSettingForm is not None and self.displayNameTextBox is not None:
            element1_top = self.panelSettingForm.location()['y']
            print(element1_top)
            element2_bottom = (self.displayNameTextBox.location()['y'] +
                               self.displayNameTextBox.size()['height'])
            print(element2_bottom)
            return element1_top > element2_bottom
        else:
            return False

    def is_data_profile_populated_under_the_drop_down_menu(self, data_profile: DataProfile):
        self.dataProfileSelection.click()
        return self.dataProfileSelection.has_option_with_text(data_profile.dataProfileName)

