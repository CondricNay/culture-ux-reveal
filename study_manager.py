import sys
import time
import TASK_LIST

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

USERNAME = "naytitorn21@gmail.com"
PASSWORD = "TobiiPassword0!"            # Password Specific - OK for public use

class StudyManager():
    def __init__(self, driver):
        self.driver = driver

    def open_website(self, website, username=USERNAME, password=PASSWORD):
        self.driver.get(website)

        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)

        login_button = self.driver.find_element(By.NAME, "action")
        login_button.click()

    def create_study(self):
        self.open_website("https://uxreveal.tobii.com/en/studies/index")

        try: 
            new_study_link = self.driver.find_element(By.CSS_SELECTOR, '#tourNewStudy a')
            new_study_link.click()

            new_study_title_field = self.driver.find_element(By.ID, "tourStudyTitleLabel")
            new_study_title_field.send_keys(TASK_LIST.STUDY_NAME)

            new_study_participant_dropdown = Select(self.driver.find_element(By.ID, "StudyNumberParticipants"))
            new_study_participant_dropdown.select_by_value("3")

            save_new_study_button = self.driver.find_element(By.ID, "addStudy")
            save_new_study_button.click()

        except NoSuchElementException:
            print("Error: Can't create new study.")
            sys.exit()
            
    # TODO add delete by id
    def delete_recent_study(self):
        self.open_website("https://uxreveal.tobii.com/en/studies/open")

        time.sleep(1)

        try:
            delete_old_study_button = self.driver.find_element(By.CSS_SELECTOR, 'div.modalButton.btn-delete')
            delete_old_study_button.click()

            delete_old_study_confirm_button = self.driver.find_element(By.ID, 'modal-button')
            delete_old_study_confirm_button.click()

        except NoSuchElementException:
            print("Error: Can't delete study.")
            sys.exit()
