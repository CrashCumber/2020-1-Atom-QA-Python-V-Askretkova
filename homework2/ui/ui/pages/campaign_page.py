import time
from .base_page import BasePage
from ui.locators.locators import CampaignPageLocators


class CampaignPage(BasePage):
    locators = CampaignPageLocators()

    def get_segments_page(self):
        self.find(self.locators.GET_SEGMENTS_PAGE_BUTTON).click()

    def get_create_campaign_page(self):
        try:
            self.find(self.locators.CREATE_CAMPAIGN_BUTTON, timeout=10).is_displayed()
            self.find(self.locators.CREATE_CAMPAIGN_BUTTON).click()
        except:
            self.find(self.locators.CREATE_FIRST_CAMPAIGN_BUTTON, timeout=10).click()

