from ddt import ddt

from src.model import page
from src.page.create_new_page_panel import CreateNewPagePanel
from src.page.dashboard_page import DashboardPage
from src.page.login_page import LoginPage
from src.until.StringHelper import StringHelper
from tests.test_base import TestBase


@ddt
class test_DA_MP_TC017(TestBase):
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    create_new_page = CreateNewPagePanel()

    parent_page_name = 'Parent_Page_' + StringHelper.generate_name()
    child_page_name = 'Child_Page_' + StringHelper.generate_name()

    parent_page = page.Page(parent_page_name)
    child_page = page.Page(child_page_name, parent_page.name, None, None, None)