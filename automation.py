from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

# Setup Edge driver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Open a page
WEBSITE = "https://uxreveal.tobii.com/en/studies/editElements/2036005350"

USERNAME = "naytitorn21@gmail.com"
PASSWORD = "TobiiPassword0!"            # Password Specific - OK for public use

driver.get(WEBSITE)

driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)

login_button = driver.find_element(By.NAME, "action")
login_button.click()

input()
