from .base_page import BasePage
from ui.ui.locators.locators import CreateSegmentPageLocators
import time


class CreateSegmentPage(BasePage):
    locators = CreateSegmentPageLocators()

    def create_segment(self):
        self.find(self.locators.ADD_AUDIENCE_BUTTON).click()
        self.scroll_to_element(self.find(self.locators.CHOICE_SEGMENT_MAIL))
        self.find(self.locators.CHOICE_SEGMENT_VK).click()
        self.find(self.locators.ADD_VK_GROUP_TO_SEGMENT).click()
        self.find(self.locators.ADD_SEGMENTS_BUTTON).click()

        name_field = self.find(self.locators.NAME_SEGMENT)
        name_field.clear()
        name = f'new_segment {time.ctime()}'
        name_field.send_keys(name)
        self.find(self.locators.CREATE_SEGMENTS_BUTTON_NEW).click()

        return name
