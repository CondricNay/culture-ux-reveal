import sys
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import TASK_LIST
from study_manager import StudyManager


# Setup Edge driver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
study_manager = StudyManager(driver)

# study_manager.create_study()
# study_manager.delete_recent_study()
time.sleep(1)

# Populate with the tasks

study_manager.open_website("https://uxreveal.tobii.com/en/studies/index")
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

time.sleep(10000)

# # 2) Add Task 1
# add_element_button = driver.find_element(By.ID, "last-add")
# add_element_button.click()

# add_text_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addText')
# add_text_button.click()

# editable_div = driver.find_element(By.CSS_SELECTOR, "div.note-editable.panel-body")
# editable_div.send_keys(TASK_LIST.TASK1_TEXT)

# button_text_input = driver.find_element(By.ID, "TextButtonText")
# button_text_input.clear()
# button_text_input.send_keys(TASK_LIST.TASK_START_TEXT)

# save_button = driver.find_element(By.ID, "saveText")
# save_button.click()

# time.sleep(1)

# # 3) Add Website
# add_element_button = driver.find_element(By.ID, "last-add")
# add_element_button.click()

# add_web_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addWeb')
# add_web_button.click()

# website_input_field = driver.find_element(By.ID, "WebUrl")
# website_input_field.send_keys(TASK_LIST.WEBSITE_URL_1)

# save_button = driver.find_element(By.ID, "saveWeb")
# save_button.click()

# time.sleep(1)

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
# add_element_button = driver.find_element(By.ID, "last-add")
# add_element_button.click()

# add_text_button = driver.find_element(By.CSS_SELECTOR, 'div.addContextIcon.addText')
# add_text_button.click()

# editable_div = driver.find_element(By.CSS_SELECTOR, "div.note-editable.panel-body")
# editable_div.send_keys(TASK_LIST.POST_EXPERIMENT_TEXT)

# button_text_input = driver.find_element(By.ID, "TextButtonText")
# button_text_input.clear()
# button_text_input.send_keys("Done")

# save_button = driver.find_element(By.ID, "saveText")
# save_button.click()

# time.sleep(2)

# # Start data collection
# start_collection_button = driver.find_element(By.CSS_SELECTOR, 'button[data-studyid]')
# driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", start_collection_button)

# time.sleep(1)

# confirm_collection_button = driver.find_element(By.ID, "modal-button")
# confirm_collection_button.click()

input()