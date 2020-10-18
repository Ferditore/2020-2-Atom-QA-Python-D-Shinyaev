import pytest


from ui.pages.auth_page import AuthPage
from ui.pages.base_page import BasePage
from ui.pages.comp_page import CompPage
from ui.pages.segment_page import SegPage


login = 'qza34340@eoopy.com'
password = 'qza34340-'

@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)

@pytest.fixture
def comp_page(driver):
    return CompPage(driver=driver)

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def segment_page(driver):
    return SegPage(driver=driver)
