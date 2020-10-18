import time

from selenium.common.exceptions import TimeoutException
from ui.locators.basic_locators import MakeSegmentLocators
from ui.pages.base_page import BasePage


class SegPage(BasePage):
    locators = MakeSegmentLocators()

    def make_segment(self, name):
        try:
            self.click(self.locators.SEGMENTS_LIST_NEW, 5)
        except TimeoutException:
            self.click(self.locators.SEGMENTS_LIST)
        self.click(self.locators.CHOOSE_SEGMENT)
        self.click(self.locators.CHECKBOX)
        self.click(self.locators.ADD_SEGMENT)
        self.find(self.locators.SEGMENT_NAME).clear()
        self.input(self.locators.SEGMENT_NAME, name)
        self.click(self.locators.CREATE_SEGMENT)

    def delete_segment(self, name):
        elem = self.find(self.locators.created_segment_name_node(name))
        elem = elem.find_element(*self.locators.DELETE_SEGMENT)
        elem.click()
        self.click(self.locators.FIND_DELETE)
        self.click(self.locators.DELETE_BUTTON)
        time.sleep(5)
