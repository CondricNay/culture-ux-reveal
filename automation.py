from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from task_actions import AddTextTask, AddWebTask
from study_manager import StudyManager
import TASK_LIST


# === Task setup pipeline ===
task_pipeline = [
    AddTextTask(TASK_LIST.PRE_EXPERIMENT_TEXT, TASK_LIST.PRE_EXPERIMENT_BUTTON_TEXT),
    AddTextTask(TASK_LIST.TASK1_TEXT, TASK_LIST.TASK_START_TEXT),
    AddWebTask(TASK_LIST.WEBSITE_URL_1),
    AddTextTask(TASK_LIST.TASK2_TEXT, TASK_LIST.TASK_START_TEXT),
    AddWebTask(TASK_LIST.WEBSITE_URL_1),
    AddTextTask(TASK_LIST.TASK4_TEXT, TASK_LIST.TASK_START_TEXT),
    AddWebTask(TASK_LIST.WEBSITE_URL_1),
    AddTextTask(TASK_LIST.TASK6_TEXT, TASK_LIST.TASK_START_TEXT),
    AddWebTask(TASK_LIST.WEBSITE_URL_1),
    AddTextTask(TASK_LIST.POST_EXPERIMENT_TEXT, "Done"),
]
# ===========================

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
study_manager = StudyManager(driver)

# study_manager.delete_recent_study()
study_manager.create_study()
study_manager.edit_recent_study(task_pipeline)
study_manager.start_new_data_collection()

input("All done. Press Enter to exit.")
