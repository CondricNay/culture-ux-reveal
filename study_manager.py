import sys
import time
import yaml

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from task_actions import TaskAction

# TODO check no study for CRUD (no C)

USERNAME = "naytitorn21@gmail.com"
PASSWORD = "TobiiPassword0!"            # Password Specific - OK for public use

with open("task_list.yaml", "r", encoding="utf-8") as f:
    TASK_LIST = yaml.safe_load(f)
    STUDY_NAME = TASK_LIST["STUDY_NAME"]

class StudyManager():
    def __init__(self, driver):
        self.driver = driver

    def open_website(self, website, username=USERNAME, password=PASSWORD):
        self.driver.get(website)

        try:
            # Check for login popup
            self.driver.find_element(By.NAME, "username").send_keys(username)
            self.driver.find_element(By.NAME, "password").send_keys(password)
            self.driver.find_element(By.NAME, "action").click()

        except NoSuchElementException:
            # Username field not found — probably already logged in
            pass

    def create_study(self, study_name=STUDY_NAME):
        self.open_website("https://uxreveal.tobii.com/en/studies/index")

        try: 
            new_study_link = self.driver.find_element(By.CSS_SELECTOR, '#tourNewStudy a')
            new_study_link.click()

            new_study_title_field = self.driver.find_element(By.ID, "tourStudyTitleLabel")
            new_study_title_field.send_keys(study_name)

            new_study_participant_dropdown = Select(self.driver.find_element(By.ID, "StudyNumberParticipants"))
            new_study_participant_dropdown.select_by_value("3")

            save_new_study_button = self.driver.find_element(By.ID, "addStudy")
            save_new_study_button.click()

        except NoSuchElementException:
            print("Error: Can't create new study.")
            input(1000)     # TODO handle
            sys.exit()

    # TODO add delete by id
    def delete_recent_study(self):
        """
        Pre-condition: the study exists
        """
        self.open_website("https://uxreveal.tobii.com/en/studies/open")
        time.sleep(1)

        try:
            delete_old_study_button = self.driver.find_element(By.CSS_SELECTOR, 'div.modalButton.btn-delete')
            delete_old_study_button.click()

            time.sleep(1)

            delete_old_study_confirm_button = self.driver.find_element(By.ID, 'modal-button')
            delete_old_study_confirm_button.click()

        except NoSuchElementException:
            print("Error: Can't delete study.")
            sys.exit()
    
    # TODO add edit by id
    # TODO also check the edit button in "https://uxreveal.tobii.com/en/studies/active" if this doesn't work
    # Note: This works by clearing all the old tasks, then adding the new tasks  #TODO implement task clearing
    def edit_recent_study(self, task_pipeline: list[TaskAction]):
        """
        Pre-condition: the study exists and the tasks are empty
        """
        self.open_website("https://uxreveal.tobii.com/en/studies/open")
        time.sleep(1)

        try:
            first_edit_button = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="/en/studies/editElements/"]')
            self.driver.execute_script("arguments[0].click();", first_edit_button)

            for action in task_pipeline:
                print(f"[Adding task] {action.__class__.__name__}")
                action.execute(self.driver)
                time.sleep(1)

        except NoSuchElementException:
            print("Error: Can't edit study.")
            sys.exit()

    # TODO by ID
    def start_new_data_collection(self):
        """
        Pre-condition: the study exists and the tasks are NOT empty
        """
        self.open_website("https://uxreveal.tobii.com/en/studies/open")
        
        try:
            start_collection_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-studyid]')
            self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", start_collection_button)

            # start_collection_button = self.driver.find_element(By.CSS_SELECTOR, 'div[data-state="open"]')
            # start_collection_button.click()

            time.sleep(1)

            confirm_collection_button = self.driver.find_element(By.ID, "modal-button")
            confirm_collection_button.click()

        except NoSuchElementException:
            print("Error: Can't start new data collection, trying to start existing data collection...")
            self.start_existing_data_collection()


    # TODO by ID
    def stop_data_collection(self):
        self.open_website("https://uxreveal.tobii.com/en/studies/active")
        
        try:
            start_collection_button = self.driver.find_element(By.CSS_SELECTOR, 'div[data-state="endStudy"]')
            start_collection_button.click()

            time.sleep(1)

            confirm_collection_button = self.driver.find_element(By.ID, "modal-button")
            confirm_collection_button.click()

        except NoSuchElementException:
            print("Error: Can't stop data collection because data collection hasn't started, trying to start existing data collection...")
            self.start_existing_data_collection()


    # TODO by ID
    def start_existing_data_collection(self):
        self.open_website("https://uxreveal.tobii.com/en/studies/completed")

        restart_collection_button = self.driver.find_element(By.CSS_SELECTOR, 'div[data-state="reopenStudy"]')
        restart_collection_button.click()

        time.sleep(1)

        confirm_collection_button = self.driver.find_element(By.ID, "modal-button")
        confirm_collection_button.click()
