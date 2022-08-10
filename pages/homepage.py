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
        self.equal(expected, actual)

    def mark_task_done(self):
        self.click("xpath", l.MARK_DONE)

    def mark_task_undone(self):
        self.click("xpath", l.MARK_UNDONE)

    def delete_task(self):
        self.click("xpath", l.DELETE)

    def verify_absence_done(self):
        return self.is_invisible("xpath", l.MARK_DONE)

    def verify_absence_undone(self):
        return self.is_invisible("xpath", l.MARK_UNDONE)

    def verify_absence_task(self):
        return self.is_invisible("xpath", l.DELETE)

    def assert_absence_done(self):
        expected_status = True
        actual_status = self.verify_absence_done()
        self.equal(expected_status, actual_status)

    def assert_absence_undone(self):
        expected_status = True
        actual_status = self.verify_absence_undone()
        self.equal(expected_status, actual_status)

    def assert_absence_task(self):
        expected_status = True
        actual_status = self.verify_absence_task()
        self.equal(expected_status, actual_status)
