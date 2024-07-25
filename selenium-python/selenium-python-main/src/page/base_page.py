from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from src.automation import Selenium
from src.automation.element import Element


class BasePage:
    def __init__(self):
        self.usersMenu = Element.xpath("//a[@href=\"#Welcome\"]")
        self.administerMenu = Element.xpath("//a[contains(@href,'#Administer')]")
        self.panelsPageLink = Element.xpath("//a[contains(@href,'panels.jsp')]")
        self.dataProfileLink = Element.xpath("//a[contains(@href,'profiles.jsp')]")

    def open_panels_page(self):
        self.administerMenu.hover()
        self.panelsPageLink.click()

    def open_data_profile_page(self):
        self.administerMenu.hover()
        self.dataProfileLink.click()

    def is_user_menu_disabled(self):
        return self.usersMenu.is_displayed()

    def get_alert_text(self):
        try:
            WebDriverWait(Selenium.driver.get_webdriver(), 10).until(EC.alert_is_present())
            alert = Selenium.driver.get_webdriver().switch_to.alert
            alert_text = alert.text
            return alert_text
        except TimeoutException:
            return "No alert present"

    def accept_alert(self):
        try:
            WebDriverWait(Selenium.driver.get_webdriver(), 10).until(EC.alert_is_present())
            alert = Selenium.driver.get_webdriver().switch_to.alert
            alert.accept()
        except TimeoutException:
            return "No alert present"
