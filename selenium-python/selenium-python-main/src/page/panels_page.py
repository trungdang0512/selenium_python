import time

from src.automation.element import Element
from src.page.base_page import BasePage


class PanelsPage(BasePage):
    def __init__(self):
        super().__init__()
        self.addNewLink = Element.xpath("//a[@href=\"javascript:Dashboard.openAddPanel('');\"]")

    def open_add_new_panel_dialog(self):
        time.sleep(1)
        self.addNewLink.click()
