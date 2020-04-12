import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from ui.ui.pages.base_page import BasePage
from ui.ui.pages.campaign_page import CampaignPage
from ui.ui.pages.create_segment_page import CreateSegmentPage
from ui.ui.pages.segments_page import SegmentsPage
from ui.ui.pages.create_campaign_page import CreateCampaignPage


@pytest.fixture(scope='function')
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope='function')
def campaign_page(driver):
    return CampaignPage(driver)


@pytest.fixture(scope='function')
def create_campaign_page(driver):
    return CreateCampaignPage(driver)


@pytest.fixture(scope='function')
def create_segment_page(driver):
    return CreateSegmentPage(driver)


@pytest.fixture(scope='function')
def segments_page(driver):
    return SegmentsPage(driver)


@pytest.fixture(scope="function")
def auto(driver):
    page = BasePage(driver)
    page.authorization(page.user, page.password)
    return BasePage(page.driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']
    if not selenoid:
        manager = ChromeDriverManager(version=version)
        driver = webdriver.Chrome(executable_path=manager.install())
    else:
        options = ChromeOptions()
        capabilities = {'acceptInsecureCerts': True,
                        'browserName': 'chrome',
                        'version': '80.0'}
        driver = webdriver.Remote(command_executor=selenoid,
                                  options=options,
                                  desired_capabilities=capabilities)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()


