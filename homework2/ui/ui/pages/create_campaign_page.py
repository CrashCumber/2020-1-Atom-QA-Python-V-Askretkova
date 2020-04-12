import os
from .base_page import BasePage
from ui.ui.locators.locators import CreateCampaignPageLocators
import time


class CreateCampaignPage(BasePage):
    locators = CreateCampaignPageLocators()

    def create_campaign(self):
        self.find(self.locators.PRODUCT_MAIL_RU_BUTTON).click()
        link_field = self.find(self.locators.INPUT_LINK)
        link_field.clear()
        link_field.send_keys('mail.ru')

        title_ad_field = self.find(self.locators.INPUT_TITLE_AD, timeout=10)
        title_ad_field.clear()
        title_ad_field.send_keys('Заголовок')

        text_ad_field = self.find(self.locators.INPUT_TEXT_AD)
        text_ad_field.clear()
        text_ad_field.send_keys('Текст')

        url_ad_field = self.find(self.locators.INPUT_URL_AD)
        url_ad_field.clear()
        url_ad_field.send_keys('mail.ru')

        path_photo = os.path.join(os.path.dirname(__file__), "../data/photo.jpg")
        path_photo = os.path.abspath(path_photo)
        photo = self.find(self.locators.PHOTO_FIELD)
        photo.send_keys(path_photo)
        self.find(self.locators.SAVE_PICTURE_BUTTON, timeout=10).click()

        path_video = os.path.join(os.path.dirname(__file__), "../data/video.mp4")
        path_video = os.path.abspath(path_video)
        video_area = self.find(self.locators.VIDEO_FIELD)
        video_area.send_keys(path_video)
        self.find(self.locators.ADD_AD_BUTTON, timeout=10).click()

        name = f'new campaign {time.ctime()}'
        title_field = self.find(self.locators.INPUT_TITLE_CAMPAIGN)[-1]
        title_field.clear()
        title_field.send_keys(name)

        self.find(self.locators.ADD_CAMPAIGN_BUTTON).click()

        return name




