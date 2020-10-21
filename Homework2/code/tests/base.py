import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.auth_page import AuthPage
from ui.pages.comp_page import CompPage
from ui.pages.base_page import BasePage
from ui.pages.segment_page import SegPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.auth_page: AuthPage = request.getfixturevalue('auth_page')
        self.comp_page: CompPage = request.getfixturevalue('comp_page')
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.segment_page: SegPage = request.getfixturevalue('segment_page')
