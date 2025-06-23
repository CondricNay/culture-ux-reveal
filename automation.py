import sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import TASK_LIST


# Setup Edge driver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Open a page
WEBSITE = "https://uxreveal.tobii.com/en/studies/index"

USERNAME = "naytitorn21@gmail.com"
PASSWORD = "TobiiPassword0!"            # Password Specific - OK for public use

driver.get(WEBSITE)

driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)

login_button = driver.find_element(By.NAME, "action")
login_button.click()

time.sleep(1)

# DEBUG TODO
# planning_link = driver.find_element(By.LINK_TEXT, "Planning")
# planning_link.click()

# delete_old_study_button = driver.find_element(By.CSS_SELECTOR, 'div.modalButton.btn-delete')
# delete_old_study_button.click()

# time.sleep(2)

# delete_old_study_confirm_button = driver.find_element(By.ID, 'modal-button')
# delete_old_study_confirm_button.click()
# END DEBUG

# Create new Study (TODO extract encapsulation)
try: 
    new_study_link = driver.find_element(By.CSS_SELECTOR, '#tourNewStudy a')
    new_study_link.click()

    new_study_title_field = driver.find_element(By.ID, "tourStudyTitleLabel")
    new_study_title_field.send_keys(TASK_LIST.STUDY_NAME)

    new_study_participant_dropdown = Select(driver.find_element(By.ID, "StudyNumberParticipants"))
    new_study_participant_dropdown.select_by_value("3")

    save_new_study_button = driver.find_element(By.ID, "addStudy")
    save_new_study_button.click()

except NoSuchElementException:
    print("Can't create new study, try deleting old ones.")
    sys.exit()

time.sleep(1)

# Populate with the tasks
# 1) Add Pre-experiment instructions
add_element_button = driver.find_element(By.ID, "last-add")
add_element_button.click()

add_text_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addText')
add_text_button.click()

editable_div = driver.find_element(By.CSS_SELECTOR, "div.note-editable.panel-body")
editable_div.send_keys(TASK_LIST.PRE_EXPERIMENT_TEXT)

button_text_input = driver.find_element(By.ID, "TextButtonText")
button_text_input.clear()
button_text_input.send_keys(TASK_LIST.PRE_EXPERIMENT_BUTTON_TEXT)

save_button = driver.find_element(By.ID, "saveText")
save_button.click()

time.sleep(1)

# 2) Add Task 1
add_element_button = driver.find_element(By.ID, "last-add")
add_element_button.click()

add_text_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addText')
add_text_button.click()

editable_div = driver.find_element(By.CSS_SELECTOR, "div.note-editable.panel-body")
editable_div.send_keys(TASK_LIST.TASK1_TEXT)

button_text_input = driver.find_element(By.ID, "TextButtonText")
button_text_input.clear()
button_text_input.send_keys(TASK_LIST.TASK_START_TEXT)

save_button = driver.find_element(By.ID, "saveText")
save_button.click()

time.sleep(1)

# 3) Add Website
add_element_button = driver.find_element(By.ID, "last-add")
add_element_button.click()

add_web_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addWeb')
add_web_button.click()

website_input_field = driver.find_element(By.ID, "WebUrl")
website_input_field.send_keys(TASK_LIST.WEBSITE_URL_1)

save_button = driver.find_element(By.ID, "saveWeb")
save_button.click()

time.sleep(1)

# # 4) Add Task 2
# add_element_button = driver.find_element(By.ID, "last-add")
# add_element_button.click()

# add_text_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addText')
# add_text_button.click()

# editable_div = driver.find_element(By.CSS_SELECTOR, "div.note-editable.panel-body")
# editable_div.send_keys(TASK_LIST.TASK2_TEXT)

# button_text_input = driver.find_element(By.ID, "TextButtonText")
# button_text_input.clear()
# button_text_input.send_keys(TASK_LIST.TASK_START_TEXT)

# save_button = driver.find_element(By.ID, "saveText")
# save_button.click()

# time.sleep(1)

# # 5) Add Website
# add_element_button = driver.find_element(By.ID, "last-add")
# add_element_button.click()

# add_web_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addWeb')
# add_web_button.click()

# website_input_field = driver.find_element(By.ID, "WebUrl")
# website_input_field.send_keys(TASK_LIST.WEBSITE_URL_1)

# save_button = driver.find_element(By.ID, "saveWeb")
# save_button.click()

# time.sleep(1)

# # 6) Add Task 4
# add_element_button = driver.find_element(By.ID, "last-add")
# add_element_button.click()

# add_text_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addText')
# add_text_button.click()

# editable_div = driver.find_element(By.CSS_SELECTOR, "div.note-editable.panel-body")
# editable_div.send_keys(TASK_LIST.TASK4_TEXT)

# button_text_input = driver.find_element(By.ID, "TextButtonText")
# button_text_input.clear()
# button_text_input.send_keys(TASK_LIST.TASK_START_TEXT)

# save_button = driver.find_element(By.ID, "saveText")
# save_button.click()

# time.sleep(1)

# # 7) Add Website
# add_element_button = driver.find_element(By.ID, "last-add")
# add_element_button.click()

# add_web_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addWeb')
# add_web_button.click()

# website_input_field = driver.find_element(By.ID, "WebUrl")
# website_input_field.send_keys(TASK_LIST.WEBSITE_URL_1)

# save_button = driver.find_element(By.ID, "saveWeb")
# save_button.click()

# time.sleep(1)

# # 8) Add Task 6
# add_element_button = driver.find_element(By.ID, "last-add")
# add_element_button.click()

# add_text_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addText')
# add_text_button.click()

# editable_div = driver.find_element(By.CSS_SELECTOR, "div.note-editable.panel-body")
# editable_div.send_keys(TASK_LIST.TASK6_TEXT)

# button_text_input = driver.find_element(By.ID, "TextButtonText")
# button_text_input.clear()
# button_text_input.send_keys(TASK_LIST.TASK_START_TEXT)

# save_button = driver.find_element(By.ID, "saveText")
# save_button.click()

# time.sleep(1)

# # 9) Add Website
# add_element_button = driver.find_element(By.ID, "last-add")
# add_element_button.click()

# add_web_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addWeb')
# add_web_button.click()

# website_input_field = driver.find_element(By.ID, "WebUrl")
# website_input_field.send_keys(TASK_LIST.WEBSITE_URL_1)

# save_button = driver.find_element(By.ID, "saveWeb")
# save_button.click()

# time.sleep(1)

# 10) Add Post-experiment instructions
add_element_button = driver.find_element(By.ID, "last-add")
add_element_button.click()

add_text_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addText')
add_text_button.click()

editable_div = driver.find_element(By.CSS_SELECTOR, "div.note-editable.panel-body")
editable_div.send_keys(TASK_LIST.POST_EXPERIMENT_TEXT)

button_text_input = driver.find_element(By.ID, "TextButtonText")
button_text_input.clear()
button_text_input.send_keys("Done")

save_button = driver.find_element(By.ID, "saveText")
save_button.click()

time.sleep(2)

# Start data collection
start_collection_button = driver.find_element(By.CSS_SELECTOR, 'button[data-studyid]')
driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", start_collection_button)

time.sleep(1)

confirm_collection_button = driver.find_element(By.ID, "modal-button")
confirm_collection_button.click()

input()