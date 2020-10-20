from random import choice
from string import ascii_letters
from tests.base import BaseCase
import pytest

from ui.locators.basic_locators import MakeCompanyLocators, MakeSegmentLocators
from ui.pages.comp_page import CompPage

login = 'qza34340@eoopy.com'
password = 'qza34340-'


@pytest.mark.UI
class Test(BaseCase):
    @pytest.fixture(scope='function')
    def authorization(self):
        self.driver.get(self.auth_page.URL)
        self.auth_page.login(login, password)
        return CompPage(self.driver)

    def test_pos_auth(self):
        self.driver.get(self.auth_page.URL)
        self.auth_page.login(login, password)
        self.auth_page.find(self.auth_page.locators.LINK_POS_AUTH, timeout=10)
        assert 'Кампании' in self.driver.page_source

    def test_neg_auth(self):
        self.driver.get(self.auth_page.URL)
        self.auth_page.login('hjkhk@mail.ru', 'kjhkj')
        assert 'Invalid login or password' in self.driver.page_source

    def test_create_comp(self, authorization):
        name = ''.join(choice(ascii_letters) for i in range(60))
        url = 'github.com'
        auto = authorization
        auto.make_company(url=url, name=name)
        auto.find(MakeCompanyLocators.TABLE_COMPANY)
        assert name in self.driver.page_source

    def test_create_segment(self, authorization):
        name = ''.join(choice(ascii_letters) for i in range(60))
        auto = authorization.open_segments()
        auto.make_segment(name)
        auto.find(MakeSegmentLocators.TABLE_SEGMENT)
        assert name in self.driver.page_source

    def test_delete_segment(self, authorization):
        name = ''.join(choice(ascii_letters) for i in range(60))
        auto = authorization.open_segments()
        auto.make_segment(name)
        auto.delete_segment(name)
        assert name not in self.driver.page_source
