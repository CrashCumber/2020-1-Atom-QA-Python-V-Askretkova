from selenium.webdriver.common.by import By


class BaseLocators:
    ENTER_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    INPUT_NAME = (By.XPATH,  '//input[@name="email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    AUTHORIZATION_BUTTON = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')
    MY_DATA_IN_CORNER = (By.CLASS_NAME, 'right-module-rightWrap-3lL6mf')


class CampaignPageLocators(BaseLocators):
    GET_SEGMENTS_PAGE_BUTTON = (By.XPATH, '//a[@href="/segments"]')

    CREATE_FIRST_CAMPAIGN_BUTTON = (By.PARTIAL_LINK_TEXT, 'создайте')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//span[contains(text(), "Создать кампанию")]')


class CreateCampaignPageLocators(BaseLocators):
    PRODUCT_MAIL_RU_BUTTON = (By.XPATH, '//div[contains(text(), "Продукты Mail.ru Group")]')

    INPUT_LINK = (By.XPATH, '//input[@type="text" and @maxlength="1000"]')

    INPUT_TITLE_AD = (By.XPATH, '//input[@data-gtm-id="banner_form_title"]')
    INPUT_TEXT_AD = (By.XPATH, '//textarea[@data-gtm-id="banner_form_text"]')
    INPUT_URL_AD = (By.XPATH, '//input[@data-gtm-id="banner_form_url"]')

    PHOTO_FIELD = (By.XPATH, '//input[@class="input__inp input__inp_file js-form-element" and @data-gtm-id="load_image_btn_256_256"]')
    SAVE_PICTURE_BUTTON = (By.XPATH, '//input[@value="Сохранить изображение"]')

    VIDEO_FIELD = (By.XPATH, '//input[@class="input__inp input__inp_file js-form-element" and @data-gtm-id="load_video_btn_640"]')

    ADD_AD_BUTTON = (By.XPATH, '//div[contains(text(),"Добавить объявление")]')

    INPUT_TITLE_CAMPAIGN = (By.XPATH, '//input[@type="text" and @maxlength="255"]')
    ADD_CAMPAIGN_BUTTON = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')

    TITLE_CAMPAIGN = (By.XPATH, '//a[@class="campaigns-tbl-cell__campaign-name" and @title="new cam"]')


class SegmentsPageLocators(BaseLocators):
    CREATE_FIRST_SEGMENTS_BUTTON = (By.PARTIAL_LINK_TEXT, 'Создайте')
    CREATE_SEGMENTS_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать сегмент")]')

    DELETE_SEGMENT_BUTTON_KRESTIKS = (By.XPATH, '//span[@class="icon-cross"]')
    DELETE_SEGMENT_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Удалить")]')


class CreateSegmentPageLocators(BaseLocators):
    ADD_AUDIENCE_BUTTON = (By.XPATH, '//span[@data-translated="Add audience segments..."]')
    CHOICE_SEGMENT_VK = (By.XPATH, '//div[contains(text(), "Группы (VK)")]')
    CHOICE_SEGMENT_MAIL = (By.XPATH, '//div[contains(text(),"Приложения (ОК и МойМир)")]')
    ADD_VK_GROUP_TO_SEGMENT = (By.CLASS_NAME, 'adding-segments-source__checkbox')
    ADD_SEGMENTS_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Добавить сегмент")]')
    NAME_SEGMENT = (By.XPATH, '//input[@type="text" and @maxlength=60]')
    CREATE_SEGMENTS_BUTTON_NEW = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать сегмент")]')



