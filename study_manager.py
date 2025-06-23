import sys
import TASK_LIST

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# EDGE_DRIVER = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# class StudyManager():
#     def __init__(self, driver=EDGE_DRIVER):
#         self.driver = driver

#     def create(self):
#         try: 
#             new_study_link = self.driver.find_element(By.CSS_SELECTOR, '#tourNewStudy a')
#             new_study_link.click()

#             new_study_title_field = self.driver.find_element(By.ID, "tourStudyTitleLabel")
#             new_study_title_field.send_keys(TASK_LIST.STUDY_NAME)

#             new_study_participant_dropdown = Select(self.driver.find_element(By.ID, "StudyNumberParticipants"))
#             new_study_participant_dropdown.select_by_value("3")

#             save_new_study_button = self.driver.find_element(By.ID, "addStudy")
#             save_new_study_button.click()

#         except NoSuchElementException:
#             print("Can't create new study, try deleting old ones.")
#             sys.exit()