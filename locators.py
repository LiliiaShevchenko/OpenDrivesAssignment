class Locators:
    TYPE_FIELD = "input.form-control"
    ADD_BUTTON = ".submit.submit"
    MARK_DONE = "//span[contains(text(),'[  ]')] [1]"
    MARK_UNDONE = "//span[contains(text(),'[X]')] [1]"
    DELETE = "//button[contains(text(),'×')]"
    TASK_NAME = "//div[contains(text(),'sample_text')] [1]"
