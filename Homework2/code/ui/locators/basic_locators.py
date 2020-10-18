from selenium.webdriver.common.by import By


class BasePageLocators(object):
    pass


class AuthLocators(BasePageLocators):
    LOG_IN = (By.XPATH, '//*[contains(@class, "responseHead-module-button")]')
    EMAIl = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    LOGIN_ENTER = (By.XPATH, '//*[contains(@class, "authForm-module-button")]')
    LINK_POS_AUTH = (By.XPATH, '//a[@href="/dashboard"]')


class MakeCompanyLocators(BasePageLocators):
    MAKE_CORP_NEW = (By.XPATH, '//a[text()="Создайте рекламную кампанию"]')
    MAKE_CORP = (By.XPATH, '//*[text()="Создать кампанию"]')
    TRAFFIC = (By.XPATH, '//div[@class="column-list-item _traffic"]')
    PLACEHOLDER = (By.XPATH, '//*[@placeholder="Введите ссылку"]')
    COMPANY_CLEAR = (By.XPATH, '//*[@class="input__clear js-input-clear"]')
    COMPANY_NAME = (By.XPATH, '//div[contains(@class, "input input_campaign-name")]/div/input')
    BUDGET_PER_DAY = (By.XPATH, '//input[@data-test="budget-per_day"]')
    BUDGET_TOTAL = (By.XPATH, '//input[@data-test="budget-total"]')
    BANNER = (By.XPATH, '//*[@cid="view685"]')
    PICT_LOAD = (By.XPATH, '//div[contains(@class, "roles-module-buttonWrap")]//input[@type="file"]')
    SAVE_IMG = (By.XPATH, '//input[@value="Сохранить изображение"]')
    CREATE_COMPANY = (By.XPATH, '//div[@class="footer__button js-save-button-wrap"]/button')
    TABLE_COMPANY = (By.XPATH, '//*[@title="Название"]')
    AUDITOR = (By.XPATH, '//a[text()="Аудитории"]')
    

class MakeSegmentLocators(BasePageLocators):
    SEGMENTS_LIST_NEW = (By.XPATH, '//*[text()="Создайте"]')
    SEGMENTS_LIST = (By.XPATH, '//div[text()="Создать сегмент"]')
    CHECKBOX = (By.XPATH, '//input[@type="checkbox"]')
    CHOOSE_SEGMENT = (By.XPATH, '//div[text()="Приложения и игры в соцсетях"]')
    ADD_SEGMENT = (By.XPATH, '//div[text()="Добавить сегмент"]')
    SEGMENT_NAME = (By.XPATH, '//div[contains(@class, "input input_create-segment-form")]/div/input')
    CREATE_SEGMENT = (By.XPATH, '//div[text()="Создать сегмент"]/parent::button')
    TABLE_SEGMENT = (By.XPATH, '//*[text()="Имя сегмента"]')


    DELETE_SEGMENT = (By.XPATH, './preceding-sibling::div/div/input')
    FIND_DELETE = (By.XPATH, '//span[text()="Действия"]')
    DELETE_BUTTON = (By.XPATH, '//li[@title="Удалить"]')


    @staticmethod
    def created_segment_name_node(name: str):
        return By.XPATH, f"//a[text()='{name}']/parent::div/parent::div"


