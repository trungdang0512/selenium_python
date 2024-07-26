import time
from telnetlib import EC

import allure
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from src.automation import Selenium
from src.automation.element import Element


class BasePage:
    def __init__(self):
        self.usersMenu = Element.xpath("//a[@href=\"#Welcome\"]")
        self.logoutBtn = Element.xpath("//a[@href=\"logout.do\"]")
        self.administerMenu = Element.xpath("//a[contains(@href,'#Administer')]")
        self.panelsPageLink = Element.xpath("//a[contains(@href,'panels.jsp')]")
        self.dataProfileLink = Element.xpath("//a[contains(@href,'profiles.jsp')]")
        self.globalSettingMenu = Element.xpath("//div[@id='main-menu']//li[@class='mn-setting']")

        self.itemsOnGlobalSettingMenuXpath = "//div[@id='main-menu']//li[@class='mn-setting']//following-sibling::li/a[text()='{}']"

    @allure.step("Log Out")
    def log_out(self):
        time.sleep(1)
        self.logoutBtn.scroll_to()
        self.logoutBtn.click()

    @allure.step("Select Global Setting Menu")
    def select_global_setting_menu(self, option):
        time.sleep(5)
        itemsOnGlobalSettingMenu = Element.xpath(self.itemsOnGlobalSettingMenuXpath)
        self.globalSettingMenu.click()
        itemsOnGlobalSettingMenu.value = itemsOnGlobalSettingMenu.value.replace('{}', option, 1)
        itemsOnGlobalSettingMenu.click()

    @allure.step("Open Panels Page")
    def open_panels_page(self):
        time.sleep(1)
        self.administerMenu.hover()
        time.sleep(1)
        self.panelsPageLink.click()

    @allure.step("Open Data Profile Page")
    def open_data_profile_page(self):
        self.administerMenu.hover()
        time.sleep(1)
        self.dataProfileLink.click()
        time.sleep(1)

    @allure.step("Check if User Menu Disabled")
    def is_user_menu_disabled(self):
        return self.usersMenu.is_disabled()

    @allure.step("Get Text On Alert Box")
    def get_alert_text(self):
        try:
            WebDriverWait(Selenium.driver.get_webdriver(), 10).until(EC.alert_is_present())
            alert = Selenium.driver.get_webdriver().switch_to.alert
            alert_text = alert.text
            return alert_text
        except TimeoutException:
            return "No alert present"

    @allure.step("Accept The Alert")
    def accept_alert(self):
        try:
            WebDriverWait(Selenium.driver.get_webdriver(), 10).until(EC.alert_is_present())
            alert = Selenium.driver.get_webdriver().switch_to.alert
            alert.accept()
        except TimeoutException:
            return "No alert present"
