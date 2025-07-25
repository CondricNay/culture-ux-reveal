import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

"""
Pipeline Architecture for adding tasks to a study
"""
class TaskAction:
    def execute(self, driver):
        raise NotImplementedError()

class AddTextTask(TaskAction):
    def __init__(self, text, button_label):
        self.text = text
        self.button_label = button_label

    def execute(self, driver):
        driver.find_element(By.ID, "last-add").click()
        driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addText').click()
        driver.find_element(By.CSS_SELECTOR, "div.note-editable.panel-body").send_keys(self.text)

        time.sleep(1)

        btn = driver.find_element(By.ID, "TextButtonText")
        btn.clear()
        btn.send_keys(self.button_label)

        driver.find_element(By.ID, "saveText").click()


class AddWebTask(TaskAction):
    def __init__(self, url):
        self.url = url

    def execute(self, driver):
        driver.find_element(By.ID, "last-add").click()
        driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addWeb').click()
        driver.find_element(By.ID, "WebUrl").send_keys(self.url)
        driver.find_element(By.ID, "saveWeb").click()


class AddQuestionTask(TaskAction):
    def __init__(self, question, button_label):
        self.question = question
        self.button_label = button_label

    def execute(self, driver):
        driver.find_element(By.ID, "last-add").click()
        driver.find_element(By.CSS_SELECTOR, "div.addContextIcon.addQuestion").click()
        driver.find_element(By.CSS_SELECTOR, "div.note-editable.panel-body").send_keys(self.question)

        time.sleep(1)

        select_element = driver.find_element(By.ID, "QuestionRowsTextField")
        Select(select_element).select_by_value("1")

        time.sleep(1)

        input_box = driver.find_element(By.ID, "QuestionButtonText")
        input_box.clear()
        input_box.send_keys(self.button_label)

        save_button = driver.find_element(By.ID, "saveQuestion")
        save_button.click()
