from base_object.base import BaseObject
from locators import Locators as l

with open('/Users/liliiashevchenko/PycharmProjects/OpenDrivesAssignment/test_data.txt') as test:
    test_data = test.read()


class Homepage(BaseObject):
    """
    functions for homepage
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def type_new_task(self):
        self.type("css", l.TYPE_FIELD, test_data)

    def add_new_task(self):
        self.click("css", l.ADD_BUTTON)

    def assert_new_task(self):
        expected = test_data
        actual = self.get_text("xpath", l.TASK_NAME)
        self.equal(actual, expected)
