from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

import allure
from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from src.automation import Selenium
from src.automation.element import Element


class LoginPage:
    def __init__(self):
        self.driver = Selenium
        self.txt_username = Element.xpath("//input[@id='username']")
        self.txt_password = Element.xpath("//input[@id='password']")
        self.btn_login = Element.xpath("//div[@class='btn-login']")

    @allure.step("Login to system")
    def login(self, username, password):
        self.txt_username.enter(username)
        self.txt_password.enter(password)
        self.btn_login.click()

    @allure.step("Click on the Login button")
    def click_login_button(self):
        self.btn_login.click()

    def get_alert_text(self):
        try:
            WebDriverWait(Selenium.driver.get_webdriver(), 10).until(EC.alert_is_present())
            alert = Selenium.driver.get_webdriver().switch_to.alert
            alert_text = alert.text
            alert.accept()
            print(alert_text)
            return alert_text
        except TimeoutException:
            return "No alert present"
