import time
from .base_page import BasePage
from ui.locators.locators import CampaignPageLocators


class CampaignPage(BasePage):
    locators = CampaignPageLocators()

    def get_segments_page(self):
        self.find(self.locators.GET_SEGMENTS_PAGE_BUTTON).click()

    def get_create_campaign_page(self):
        time.sleep(3)
        if self.find(self.locators.CREATE_CAMPAIGN_BUTTON).is_displayed():
            self.find(self.locators.CREATE_CAMPAIGN_BUTTON).click()

        else:
            self.find(self.locators.CREATE_FIRST_CAMPAIGN_BUTTON).click()

