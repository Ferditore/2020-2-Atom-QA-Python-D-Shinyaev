import time

from selenium.common.exceptions import TimeoutException
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import MakeCompanyLocators
from pathlib import Path

from ui.pages.segment_page import SegPage


class CompPage(BasePage):
    locators = MakeCompanyLocators()
    IMAGE_PATH = Path.cwd()/'picture'/'image.png'

    def make_company(self, url, name):
        try:
            self.click(self.locators.MAKE_CORP_NEW)
        except TimeoutException:
            self.click(self.locators.MAKE_CORP)
        self.click(self.locators.TRAFFIC)
        self.input(self.locators.PLACEHOLDER, url)
        self.click(self.locators.COMPANY_CLEAR)
        self.input(self.locators.COMPANY_NAME, name)
        self.input(self.locators.BUDGET_PER_DAY, '100')
        self.input(self.locators.BUDGET_TOTAL, '1000')
        self.click(self.locators.BANNER)
        self.input(self.locators.PICT_LOAD, str(self.IMAGE_PATH))
        time.sleep(5)
        self.click(self.locators.CREATE_COMPANY)

    def open_segments(self):
        self.click(self.locators.AUDITOR)
        return SegPage(self.driver)
