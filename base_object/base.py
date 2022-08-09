from selenium.webdriver.support.ui import WebDriverWait
from base_object.error_messages import CustomErrors, CustomExceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class BaseObject:
    """
    base methods
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def __selenium_by(self, find_by):
        selectors_dict = {'css': By.CSS_SELECTOR,
                          'xpath': By.XPATH,
                          'id': By.ID,
                          'name': By.NAME,
                          'class': By.CLASS_NAME,
                          'partial_link_text': By.PARTIAL_LINK_TEXT,
                          'link_text': By.LINK_TEXT,
                          'tag_name': By.TAG_NAME}
        return selectors_dict[find_by]

    def is_visible(self, find_by, locator):
        """
        :param find_by: to find element by method
        :param locator: locator of the element
        :return: will return visible element
        """
        return self.wait.until(ec.visibility_of_element_located((self.__selenium_by(find_by), locator)))

    def is_invisible(self, find_by, locator):
        """
        :param find_by: to find element by method
        :param locator: locator of the element
        :return: will return invisible element
        """
        try:
            element = self.wait.until(ec.invisibility_of_element_located((self.__selenium_by(find_by), locator)))
            print(element)
            return element
        except Exception:
            raise Exception(CustomExceptions.AbsenceException)

    def type(self, find_by, locator, data):
        """
        :param find_by: to find element by method
        :param locator: locator of the element
        :param data: data to send
        """
        return self.wait.until(ec.visibility_of_element_located((self.__selenium_by(find_by), locator))).send_keys(data)

    def click(self, find_by, locator):
        """
        :param find_by: to find element by method
        :param locator: locator of the element
        """
        return self.wait.until(ec.visibility_of_element_located((self.__selenium_by(find_by), locator))).click()

    def get_text(self, find_by, locator):
        """
        :param find_by: to find element by method
        :param locator: locator of the element
        :return: will return text
        """
        return self.wait.until(ec.visibility_of_element_located((self.__selenium_by(find_by), locator))).text

    def equal(self, expected, actual):
        """
        :param expected: expected 1
        :param actual:  actual 1
        """
        assert expected == actual, CustomErrors.EQUAL
