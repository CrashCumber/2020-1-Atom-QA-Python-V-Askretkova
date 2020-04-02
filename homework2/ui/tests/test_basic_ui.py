import time
import pytest
import selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base_ui import BaseCase
from ui.fixtures import *


class TestUI(BaseCase):

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_good_authorization(self):
        user = 'asktechnoatom@mail.ru'
        password = 'asktechnoatom'
        self.base_page.authorization(user, password)
        res = self.base_page.find(self.base_page.locators.MY_DATA_IN_CORNER).is_displayed()
        assert 'https://target.my.com/campaigns/list' == self.driver.current_url

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_bad_authorization(self):
        user = 'asktechnoatom@mail.ru'
        password = 'asktechnoatofwfwfwfwfwfwfwfwfwfwm'
        self.base_page.authorization(user, password)
        assert 'https://target.my.com/campaigns/list' != self.driver.current_url

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_create_segment(self, auto):
        self.base_page = auto
        self.campaign_page.get_segments_page()
        self.segments_page.create_segment()
        name = self.create_segment_page.create_segment()
        NEW_SEGMENT = (By.XPATH, f'//a[@title="{name}"]')
        assert self.base_page.find(NEW_SEGMENT, timeout=10).is_displayed()

    @pytest.mark.UI
    def test_delete_segment(self, auto):
        self.base_page = auto
        self.campaign_page.get_segments_page()
        self.segments_page.create_segment()
        name = self.create_segment_page.create_segment()
        NEW_SEGMENT = (By.XPATH, f'//a[@title="{name}"]')
        elem = self.base_page.find(self.segments_page.locators.DELETE_SEGMENT_BUTTON_KRESTIKS, timeout=10)
        if type(elem) is type(list()):
            elem = elem[-1]
        elem.click()
        self.base_page.find(self.segments_page.locators.DELETE_SEGMENT_BUTTON).click()
        time.sleep(2)
        try:
            assert not self.base_page.find(NEW_SEGMENT).is_displayed()
        except selenium.common.exceptions.TimeoutException:
            pass

    @pytest.mark.UI
    def test_create_campaign(self, auto):
        self.base_page = auto
        self.campaign_page.get_create_campaign_page()
        name = self.create_campaign_page.create_campaign()
        TITLE_CAMPAIGN = (By.XPATH, f'//a[@class="campaigns-tbl-cell__campaign-name" and @title="{name}"]')
        assert self.base_page.find(TITLE_CAMPAIGN, timeout=10).is_displayed()








