import allure
from ddt import ddt, data, unpack

from src.model import page
from src.page.create_new_page_dialog import CreateNewPageDialog
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.until.string_helper import StringHelper
from tests.test_base import TestBase


@ddt
class test_DA_PANEL(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
