import time

from src.automation.element import Element
from src.model.panel.panel import Panel
from src.page.base_page import BasePage
from src.until.page_loader import PageLoader


class PanelsPage(BasePage):
    def __init__(self):
        super().__init__()
        self.addNewLink = Element.xpath("//a[@href=\"javascript:Dashboard.openAddPanel('');\"]")

        self.panelEditButtonXpath = "//a[text()='{}']/parent::td/following-sibling::td/a[text()='Edit']"

    def open_add_new_panel_dialog(self):
        time.sleep(1)
        self.addNewLink.click()

    def open_edit_panel_dialog(self, panel: Panel):
        panelEditButton = Element.xpath(self.panelEditButtonXpath)
        panelEditButton.value = panelEditButton.value.replace('{}', panel.displaySettings.display_name)
        time.sleep(1)
        panelEditButton.click()