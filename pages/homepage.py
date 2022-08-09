from base_object.base import BaseObject


class Homepage(BaseObject):
    """
    functions for homepage
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
