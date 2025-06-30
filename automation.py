from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from build_pipeline import build_task_pipeline, build_task_pipeline_japanese
from study_manager import StudyManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
study_manager = StudyManager(driver)

# For Debug
# study_manager.open_website("https://uxreveal.tobii.com/en/studies/index")

# study_manager.delete_recent_study()
study_manager.create_study()
task_pipeline = build_task_pipeline_japanese()
study_manager.edit_recent_study(task_pipeline)
study_manager.start_new_data_collection()

input("All done. Press Enter to exit.")
