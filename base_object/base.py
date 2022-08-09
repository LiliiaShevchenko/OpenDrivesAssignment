from selenium.webdriver.support.ui import WebDriverWait

class BaseObject:
    """
    base methods
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
