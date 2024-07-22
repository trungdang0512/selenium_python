from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from src.automation import Selenium


class BasePage:
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