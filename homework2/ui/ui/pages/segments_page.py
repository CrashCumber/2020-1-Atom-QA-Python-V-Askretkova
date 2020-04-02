from .base_page import BasePage
from ui.locators.locators import SegmentsPageLocators


class SegmentsPage(BasePage):
    locators = SegmentsPageLocators()

    def create_segment(self):
        if self.find(self.locators.CREATE_SEGMENTS_BUTTON).is_displayed():
            self.find(self.locators.CREATE_SEGMENTS_BUTTON).click()
        else:
            self.find(self.locators.CREATE_FIRST_SEGMENTS_BUTTON).click()
