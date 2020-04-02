import pytest
from ui.fixtures import *
from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage
from ui.pages.create_segment_page import CreateSegmentPage
from ui.pages.segments_page import SegmentsPage
from ui.pages.create_campaign_page import CreateCampaignPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.campaign_page: CampaignPage = request.getfixturevalue('campaign_page')
        self.create_segment_page: CreateSegmentPage = request.getfixturevalue('create_segment_page')
        self.segments_page: SegmentsPage = request.getfixturevalue('segments_page')
        self.create_campaign_page: CreateCampaignPage = request.getfixturevalue('create_campaign_page')
